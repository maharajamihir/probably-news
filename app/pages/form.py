import streamlit as st

st.write("## Hi, enter your details, to get a personalized AI generated Newsfeed video!")

with st.form("my_form"):
   st.write("Let's get to know eachother!")
   email = st.text_input("Email") # email
   age = st.number_input('Age', min_value=0, max_value=200, step=1) # age
   gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=None, placeholder="Choose an option")
   interests = st.multiselect("Your interests (max 3)", ["World", "Business"], max_selections=3)
   sm_user = st.toggle("Active social media user", value=False)
   # marital_status = st.selectbox("Marital Status", ["Married", "Single", "its complicated"], index=None, placeholder="Choose an option")
   fav_celeb = st.multiselect("Your favourite celebs/characters (max 5)", ["Donald Trump", "Drake", "Mark Luxenhofer"], max_selections=5)

   checkbox_val = st.checkbox("I agree my info can be used for news generation")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("age", age, "checkbox", checkbox_val)