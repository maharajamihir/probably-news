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

helper.get_streamlit(cur_user)