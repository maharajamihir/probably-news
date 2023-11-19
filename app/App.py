import streamlit as st
import helper
import json
import os


REGION = 'us-east-1'
os.environ['AWS_DEFAULT_REGION'] = REGION # set region to us-east-1 because endpoint is there    
    


users = [
   helper.User(first_name="Alfred", last_name="Nguyen", interests=["Tech", "Sports"]), 
   helper.User(first_name="Mia", last_name="Heinz", interests=["Politics", "Entertainment", "Tech"]), 
   helper.User(first_name="Mihir", last_name="Mahajan", interests=["Sports", "Tech", "Finance"]), 
   helper.User(first_name="TestUser", last_name="TestUser", interests=["Tech"], age=21, gender="Male"),
   helper.User(first_name="Test2", last_name="Test2", interests=["Sports"])
    ]


st.header("AI news feed generator")

cur_user = st.selectbox(
    label='Who are you?',
    options=[None] + [u for u in users])

helper.get_streamlit(cur_user)