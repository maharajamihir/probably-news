import streamlit as st
import sys
import os
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

import helper

cur_user = None
st.write("## Hi, enter your details, to get a personalized AI generated Newsfeed video!")




with st.form("my_form"):
   st.write("Let's get to know eachother!")
   first_name = st.text_input("First Name") # fname
   last_name = st.text_input("Last Name") # lname
   email = st.text_input("Email") # email
   age = st.number_input('Age', min_value=0, max_value=200, step=1) # age
   gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=None, placeholder="Choose an option")
   interests = st.multiselect("Your interests (max 3)", helper.interest_to_link.keys(), max_selections=3)
   sm_user = st.toggle("Active social media user", value=False)
   # marital_status = st.selectbox("Marital Status", ["Married", "Single", "its complicated"], index=None, placeholder="Choose an option")
   fav_celeb = st.multiselect("Your favourite celebs/characters (max 5)", ["Donald Trump", "Drake", "Mark Luxenhofer"], max_selections=5)

   checkbox_val = st.checkbox("I agree my info can be used for news generation")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("")
       cur_user = helper.User(first_name=first_name,last_name=last_name, age=age, gender=gender, interests=interests, fav_celebs=fav_celeb, sm_user=sm_user)
helper.get_streamlit(cur_user)
# if cur_user is not None:
    # st.write("## Welcome to your news feed ", cur_user)
    # st.write("### From our data, we have analyzed that you are interested in ", str(cur_user.interests))
    # st.write("We have prepared a custom news feed for you!")

    # with st.spinner("Fetching newsfeed🤖"):
        # news,audio = helper.get_newsfeed(cur_user)
        # for i in range(len(news)):
            # st.write(news[i])
            # st.audio(audio[i])
            # try:
                # if cur_user.generation == "Gen-Z":
                    # file = open(cur_user.interests[i]+'.mp3', 'wb')
                    # file.write(audio[i])
                    # file.close()
                    # news_topic = cur_user.interests[i]
                    # vid_file = helper.get_subway_surf_vid(news_topic,news_topic+".mp3", 'media/subway_surf.mp4')
                    # video_file = open(vid_file, 'rb')
                    # video_bytes = video_file.read()
                    # st.video(video_bytes)
                # else:
                    # st.image(helper.gen_img(cur_user.interests[i], audio[i], cur_user))
            # except Exception:
                # pass