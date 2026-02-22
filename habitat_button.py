import streamlit as st
import time
city_list = ["Seattle","Issaquah","Auburn","Snoqualmie","Spokane"]
user_city = st.selectbox("Put in the city you live closest to", city_list)
time.sleep(3)
if user_city == "Seattle":
    st.link_button("Go To Seattle Page", "https://emp-hackfest-group-mangcoders-hnljnmigsnxoxvm52apcv5.streamlit.app/")
elif user_city == "Issaquah":
    st.link_button("Go To Issaquah Page","https://emp-hackfest-group-mangcoders-gcmqn5hjqldkwqjrfovqbt.streamlit.app/")
elif user_city == "Auburn":
    st.link_button("Go To Auburn Page", "https://emp-hackfest-group-mangcoders-cajxpu62ca5y5cvk348uce.streamlit.app/")
elif user_city == "Snoqualmie":
    st.link_button("Go To Snoqualmie Page","https://emp-hackfest-group-mangcoders-xgikge9bcdydokvvqfwbue.streamlit.app/")
elif user_city == "Spokane":
    st.link_button("Go To Spokane Page", "https://emp-hackfest-group-mangcoders-gpufuyb7z9rukfadwwjyff.streamlit.app/")
st.link_button("Go to the Birds Page","https://emp-hackfest-group-mangcoders-mupryp8pmzxlthti4zcfgh.streamlit.app/")