import streamlit as st

city_list = ["Seattle","Issaquah","Auburn","Snoqualmie","Spokane"]
user_city = st.selectbox("Put in the city you live closest to", city_list)

if user_city == "Seattle":
    st.link_button("Go To Seattle Page", "")
elif user_city == "Issaquah":
    st.link_button("Go To Issaquah Page")
elif user_city == "Auburn":
    st.link_button("Go To Auburn Page")
elif user_city == "Snoqualmie":
    st.link_button("Go To Snoqualmie Page")
elif user_city == "Spokane":
    st.link_button("Go To Spokane Page")
st.link_button("Go to the Birds Page")