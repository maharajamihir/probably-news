import streamlit as st

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))




# File path to your MP4 video
video_path = "data/download"

# Display the video
st.video(video_path)


