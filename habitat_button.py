import streamlit as st
from trees import Fih, Bord
city_list = ["Seattle","Bellevue","Issaquah","Auburn","Snoqualmie","Spokane"]
user_city = st.selectbox("Put in the city you live closest to", city_list)

if st.button("Habitat Finder!"):
    if user_city == "Seattle":
        st.write("")
