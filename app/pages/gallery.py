import streamlit as st
import os

directory = r'assets/'
files = os.listdir(directory)
files = [f"assets/{f}" for f in files]
files.append("https://drive.google.com/file/d/1fqjX7G9yj1itOrY2fPLRImqMcnuosN3i/view?usp=drive_link")


cols = [[],[],[]]
for i in range(len(files)):
    f = files[i]
    idx = i % 3
    cols[idx].append(f)




st.write("# Gallery")

def fill_clm(assets):
    for fpath in assets:
        if ".mp4" in fpath or ".mov" in fpath:
            st.video(fpath)
        elif ".png" in fpath or ".jpg" in fpath or ".jpeg" in fpath:
            st.image(fpath)



controls = st.columns(3)
with controls[0]:
    fill_clm(cols[0])
with controls[1]:
    fill_clm(cols[1])
with controls[2]:
    fill_clm(cols[2])