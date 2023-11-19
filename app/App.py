import streamlit as st
import helper
import json
import os


REGION = 'us-east-1'
os.environ['AWS_DEFAULT_REGION'] = REGION # set region to us-east-1 because endpoint is there    
    


users = [
   helper.User(first_name="Alfred", last_name="Nguyen", interests=["Tech", "Sports"], age=21, gender="Male", fav_celebs=[], sm_user=False), 
   helper.User(first_name="Mia", last_name="Heinz", interests=["Politics", "Entertainment"], age=21, gender="Female", fav_celebs=[], sm_user=False), 
   helper.User(first_name="Mihir", last_name="Mahajan", interests=["Sports", "Tech", "Finance"], age=21, gender="Male", fav_celebs=[], sm_user=False), 
   helper.User(first_name="Hannah", last_name="TestUser", interests=["Personal Finance"], age=9, gender="Female"),
   helper.User(first_name="Bert", last_name="Test", interests=["Sports"], age=70, gender="Male")
    ]


st.header("AI news feed generator")

cur_user = st.selectbox(
    label='Who are you?',
    options=[None] + [u for u in users])

if cur_user is not None:
    st.write("## Welcome to your news feed ", cur_user)
    st.write("### From our data, we have analyzed that you are interested in ", str(cur_user.interests))
    st.write("We have prepared a custom news feed for you!")

    with st.spinner("Fetching newsfeed🤖"):
        news,audio = helper.get_newsfeed(cur_user)
        for i in range(len(news)):
            st.write(news[i])
            st.audio(audio[i])
            try:
                if cur_user.generation == "Gen-Z":
                    file = open(cur_user.interests[i]+'.mp3', 'wb')
                    file.write(audio[i])
                    file.close()
                    news_topic = cur_user.interests[i]
                    vid_file = helper.get_subway_surf_vid(news_topic,news_topic+".mp3", 'media/subway_surf.mp4')
                    video_file = open(vid_file, 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                else:
                    st.image(helper.gen_img(cur_user.interests[i], audio[i], cur_user))
            except Exception:
                pass


    # for i in cur_user.interests:
        # with st.spinner("Fetching newsfeed🤖"):
            # st.write(f"### {i}")
            # try:
                # news = helper.get_newsfeed(i, 65)
                # st.write(news)
                # audio = helper.t2speech(news, "Amy")
                # st.audio(audio)
            # except Exception as e:
                # with st.spinner("Looks like this is your first time here... setting up..."):
                    # os.system("playwright install")
                    # e
            # st.write("in json:")
            # ls_json = helper.get_list_as_json(ls)
            # st.write(ls_json)
            # ls_json = json.loads(ls_json)
            # article1 = helper.get_article_summary(ls_json,links)
            # st.write(article1)
