import streamlit as st
import os
import requests

from dotenv import load_dotenv

def read_env_file():
    load_dotenv()
    return os.getenv("API_KEY")

def make_api_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

# Streamlit app
st.title("SyncLabs API Request Example")

# Input fields
url = st.text_input("Enter API URL:", 'https://api.synclabs.so/video/f38c6133-0c9a-4857-ab0a-dc1c4663cb45')

api_key = read_env_file()

# Make the API request when the user clicks the button
if st.button("Make API Request"):
    headers = {
        'accept': 'application/json',
        'x-api-key': api_key
    }
    
    result = make_api_request(url, headers)
    
    # Display the result
    st.header("API Response:")
    st.json(result)



