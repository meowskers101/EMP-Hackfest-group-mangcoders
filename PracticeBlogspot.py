import streamlit as st

st.set_page_config(page_title="BlogPost", page_icon="🤖")

st.write("Welcome to the blogspot where you share your reviews on restaurants that you like or dislike!")

Your_review = st.text_input("Put your food review here")
Reviews = []

st.header('Review')

# create 2 columns
col1, col2 = st.columns(2)

with col1:
    container1 = st.container()
    add_button = st.button('add')
    if add_button:
        Reviews.append(Your_review)

st.write(Reviews)

if st.button("Submit Review"):
    st.write("Review Submitted!")