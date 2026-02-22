import streamlit as st
st.title("Auburn Fish")
st.write("Here are some fish that primarily live in Auburn, and how you can help their habitats.")
st.image(
    "https://seagrant.oregonstate.edu/sites/seagrant.oregonstate.edu/files/styles/fluid_webp/public/2024-09/7mountain_whitefish_photo_brooke_penaluna_black.png.webp?itok=9uSf3fXj",
    width=615,
    caption="Mountain Whitefish"
)
st.write("Mountain Whitefish are crucial to river ecosystems as a primary food source for birds of prey like eagles and ospreys. They also are indicators of high water quality and, as fish that feed on the bottom of the stream, play a vital role in nutrient cycling, which helps improve stream quality. To help protect their habitats, you can protect their cold-water habitats, practice sustainable fishing, and support conservation that removes invasive species.")
st.sidebar.link_button("HI","a")