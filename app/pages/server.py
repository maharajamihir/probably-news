from dotenv import load_dotenv
import streamlit as st
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

def create_request_header():
    return {'accept': 'application/json','x-api-key': api_key}

def get_deepfake(id):
    try:
        response = requests.get(
            f"https://api.synclabs.so/video/{id}", 
            headers=create_request_header()
        )
        print(response)

        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

def post_deepfake(video_url, audio_url):
    try:
        response = requests.post(
            f"https://api.synclabs.so/video/", 
            headers=create_request_header(),
            json={
                "videoUrl": video_url,
                "audioUrl": audio_url,
                "synergize": True,
            }
        )

        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

# Streamlit app
st.title("SyncLabs API Request Example")

# Input fields
url = st.text_input("Enter API URL:", 'https://api.synclabs.so/video/f38c6133-0c9a-4857-ab0a-dc1c4663cb45')

# Make the API request when the user clicks the button
if st.button("Make API Request"):
    
    id = "5f605bfe-8759-40fd-b132-9630f5f237f3" # put your id here
    video_url= "https://playful-froyo-95db49.netlify.app/susanne.mp4"
    audio_url= "https://playful-froyo-95db49.netlify.app/trump_voice_2.mp3"
    # result = get_deepfake(id)
    result = post_deepfake(video_url, audio_url)
    
    # Display the result
    st.header("API Response:")
    st.json(result)



