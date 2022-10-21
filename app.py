import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import datetime

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Ramiz", page_icon=":maple_leaf:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_qgah66oi.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
ramiz_profile = Image.open("images/ramiz_profile.png")
nxt_nxt = Image.open("images/nxt_nxt.png")
flower_img = Image.open("images/flower_img.png")
chocolate_img = Image.open("images/chocolate_img.png")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
    with right_column:
        st.subheader("﷽")
with st.container():
    st.write("---")
    st.header("")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(ramiz_profile)
    with text_column:
        st.subheader("MD Ramiz Uddin")
        st.write(
            """
            - _Fashion Model_
            - _Live in Dhaka,Bangladesh._
            - _Studies Bsc(Hons.) at Govt. P.C College, Bagherhat._
            - _Hobbies - Skydiving, Travelling, Plane spotting, Car Raching, Fashion Photography._
            """
        )

    st.write("[FOLLOW ME ON FACEBOOK](https://www.facebook.com/ramiz.uddin2002)")
    st.write("[FOLLOW ME ON INSTAGRAM](https://www.instagram.com/ramiz.uddin2002)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What are designers in fashion?")
        st.write("##")
        st.write(
            """
            Designers in fashion are professionals who create concepts of new and trending styles,
            build real-life prototypes of these designs and prepare the final products to sell to customers. 
            Fashion designers typically specialize in one type of field and stay updated on the trends within that area. 
            After graduating from their program of choice, a fashion designer can choose to create clothing, shoes or accessories. 
            There are several subsections within these categories that a designer can pursue depending on their skills and interests.
            """
        )
        st.write("[Learn More](https://vesperglobalsourcing.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        st.empty()
