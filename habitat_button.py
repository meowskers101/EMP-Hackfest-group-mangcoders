import streamlit as st
import time
city_list = ["Seattle","Issaquah","Auburn","Snoqualmie","Spokane"]
user_city = st.selectbox("Put in the city you live closest to", city_list)
time.sleep(3)
if user_city == "Seattle":
    st.link_button("Go To Seattle Fish Page", "https://emp-hackfest-group-mangcoders-hnljnmigsnxoxvm52apcv5.streamlit.app/")
elif user_city == "Issaquah":
    st.link_button("Go To Issaquah Fish Page","https://emp-hackfest-group-mangcoders-gcmqn5hjqldkwqjrfovqbt.streamlit.app/")
elif user_city == "Auburn":
    st.link_button("Go To Auburn Fish Page", "https://emp-hackfest-group-mangcoders-cajxpu62ca5y5cvk348uce.streamlit.app/")
elif user_city == "Snoqualmie":
    st.link_button("Go To Snoqualmie Fish Page","https://emp-hackfest-group-mangcoders-xgikge9bcdydokvvqfwbue.streamlit.app/")
elif user_city == "Spokane":
    st.link_button("Go To Spokane Fish Page", "https://emp-hackfest-group-mangcoders-gpufuyb7z9rukfadwwjyff.streamlit.app/")
st.link_button("Go to the Birds Page","https://emp-hackfest-group-mangcoders-mupryp8pmzxlthti4zcfgh.streamlit.app/")
st.link_button("Go to the Animal Detector(Input An Image To Detect Animals!)","https://emp-hackfest-group-mangcoders-dbte3nemdvjykznmtxnqsa.streamlit.app/")
