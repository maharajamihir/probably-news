import helper
import json
import os

class User:
    def __init__(self, first_name, last_name, interests):
        self.first_name = first_name
        self.last_name = last_name
        self.interests = interests

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


users = [
   User(first_name="Alfred", last_name="Nguyen", interests=["Tech", "Cars", "Sports"]), 
   User(first_name="Mia", last_name="Heinz", interests=["Politics", "Entertainment", "Tech"]), 
   User(first_name="Mihir", last_name="Mahajan", interests=["Sports", "Tech", "Finance"]), 
   User(first_name="TestUser", last_name="TestUser", interests=["Tech"])
    ]


st.header("AI news feed generator")

cur_user = st.selectbox(
    label='Who are you?',
    options=[None] + [u for u in users])

if cur_user is not None:
    st.write("## Welcome to your news feed ", cur_user)
    st.write("### From our data, we have analyzed that you are interested in ", str(cur_user.interests))
    st.write("We have prepared a custom news feed for you!")


    for i in cur_user.interests:
        with st.spinner("Fetching newsfeed🤖"):
            st.write(f"### {i}")
            try:
                news = helper.get_newsfeed(i, 65)
                st.write(news)
                audio = helper.t2speech(news, "Amy")
                st.audio(audio)
            except Exception as e:
                with st.spinner("Looks like this is your first time here... setting up..."):
                    os.system("playwright install")
                    e
            # st.write("in json:")
            # ls_json = helper.get_list_as_json(ls)
            # st.write(ls_json)
            # ls_json = json.loads(ls_json)
            # article1 = helper.get_article_summary(ls_json,links)
            # st.write(article1)
