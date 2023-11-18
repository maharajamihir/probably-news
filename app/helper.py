from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.llms import Bedrock
import boto3


model_name = "anthropic.claude-v2"


interest_to_link = {
    "Tech": "https://www.focus.de/digital/",
    "Politics": "https://www.focus.de/politik/",
    "Finance": "https://www.focus.de/finanzen/",
    "Cars": "https://www.focus.de/auto/",
    "Entertainment": "https://www.focus.de/kultur/",
    "Sports": "https://www.focus.de/sport/"
    # TODO erweitern
}

def get_newsfeed(interest):
    # Load HTML
    links = [interest_to_link.get(interest, "https://www.focus.de/")]
    # links = "https://www.wsj.com/"
    loader = AsyncChromiumLoader(links)
    html = loader.load()

    # Transform
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html
                                                       , tags_to_extract=["h3"]
                                                       # , tags_to_extract=["span"]
                                                        )
    # Result
    site = docs_transformed[0].page_content[0:5000]

    llm = Bedrock(model_id=model_name, credentials_profile_name="default", region_name="us-east-1")

    res = llm(f"""
        Give me the top five news headlines from this news website, that fit into the category {interest}:

        
        {site}
    """)

    return res, links

def t2speech(text):

    text = text.replace("\n", ".\n")
    client = boto3.client("polly")
    response = client.synthesize_speech(
        Engine='neural',
        LanguageCode='de-DE',
        OutputFormat='mp3',
        Text=text,
        VoiceId='Vicki'
    )
    file = open('speech.mp3', 'wb')
    audio = response['AudioStream'].read()
    file.write(audio)
    file.close()
    return audio



def get_list_as_json(list):
    llm = Bedrock(model_id=model_name, credentials_profile_name="default", region_name="us-east-1")

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