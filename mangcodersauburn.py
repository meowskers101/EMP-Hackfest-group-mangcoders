import streamlit as st
st.title("Auburn Fish")
st.write("Here are some fish that primarily live in Auburn, and how you can help their habitats.")
st.image(
    "https://seagrant.oregonstate.edu/sites/seagrant.oregonstate.edu/files/styles/fluid_webp/public/2024-09/7mountain_whitefish_photo_brooke_penaluna_black.png.webp?itok=9uSf3fXj",
    width=615,
    caption="Mountain Whitefish"
)
st.write("The mountain whitefish is a unique species of fish that mainly resides in the rivers in Auburn. It plays a very important role in the ecosystem and serves as a critical nutrient transporter and also as a prey buffer for trout. A way you can help this species is supporting deep-water stream conservation efforts and making sure they have lots of woody debris for protection.")
st.page_link("habitat_button.py", label="Go back home", icon="🏠")