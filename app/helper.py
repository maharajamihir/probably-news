from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.prompts import PromptTemplate
from langchain.llms import Bedrock
import boto3


model_name = "anthropic.claude-v2"


interest_to_link = {
    "Tech": "https://www.wsj.com/tech",
    "Politics": "https://www.wsj.com/politics",
    "Finance": "https://www.wsj.com/finance",
    "Arts&Culture": "https://www.wsj.com/arts-culture",
    "Business": "https://www.wsj.com/business",
    "Sports": "https://www.wsj.com/sports",
    "Lifestyle": "https://www.wsj.com/lifestyle",
    "Personal Finance": "https://www.wsj.com/personal-finance"
    # TODO erweitern
}

def _get_bedrock_llm():
    bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
    llm = Bedrock(model_id=model_name, client=bedrock_client, region_name="us-east-1")
    return llm

def get_headlines(interest):
    # Load HTML
    links = [interest_to_link.get(interest, "https://www.wsj.com/")]
    # links = ""
    loader = AsyncChromiumLoader(links)
    html = loader.load()

    # Transform
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html
                                                       # , tags_to_extract=["h3"]
                                                       , tags_to_extract=["span"]
                                                        )
    # Result
    site = docs_transformed[0].page_content[0:5000]
    with open("templates/get_headlines.txt") as f:
        prompt_headlines = f.read()
    prompt_template = PromptTemplate.from_template(
        prompt_headlines
    )
    prompt = prompt_template.format(num_headlines=3, interest=interest, site_text=site)
    llm = _get_bedrock_llm()
    res = llm(prompt)
    return res, links


def get_newsfeed(interest, age):
    headlines,_ = get_headlines(interest=interest)
    with open("templates/personalize_news_anchor.txt") as f:
        news_update = f.read()
    prompt_template = PromptTemplate.from_template(
        news_update
    )
    generation = ""

    if age < 13:
        generation = "Children"
    elif age < 24:
        generation = "Gen-Z"
    elif age < 35:
        generation = "Young Adults"
    elif age < 60: 
        generation = "Adults"
    else:
        generation = "Senior citizens"

    prompt = prompt_template.format(headlines=headlines, generation=generation)
    llm = _get_bedrock_llm()
    print(prompt)
    print("===========================")
    res = llm(prompt)
    return res

    
def t2speech(text, speaker):
    text = text.replace("\n", ".\n")
    client = boto3.client("polly")
    response = client.synthesize_speech(
        Engine='neural',
        LanguageCode='en-US',
        OutputFormat='mp3',
        Text=text,
        VoiceId=speaker
    )
    file = open('speech.mp3', 'wb')
    audio = response['AudioStream'].read()
    file.write(audio)
    file.close()
    return audio



def get_list_as_json(list):
    llm = _get_bedrock_llm()

    res = llm(f"""
        Give me this list of headlines in json format:
        
        {list}
    """)
    return res


def get_article_summary(articles, links):
    loader = AsyncChromiumLoader(links)
    html = loader.load()
    print(html)
    return articles[0]


if __name__ == "__main__":
    news = get_newsfeed("Tech", 8)
    print(news)