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
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_wpj8myqt.json")
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
        st.subheader("")
        st.title("﷽")
with st.container():
    st.write("---")
    st.header("PROFILE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(ramiz_profile)
    with text_column:
        st.subheader("MD. Ramiz Uddin")
        st.write(
            """
            - _I am a student._
            - _Live in Khulna,Bangladesh._
            - _Studies at Khulna Polytechnic Institute._
            - _Hobbies - Coding, Travelling, Video Games, Listening to Music_
            """
        )

    st.write("[FOLLOW ME ON FACEBOOK](https://www.facebook.com/moeen.u9)")
    st.write("[FOLLOW ME ON INSTAGRAM](https://www.facebook.com/moeen.u9)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Be Careful,Be Safe.")
        st.write("##")
        st.write(
            """
            1.  Protect Your Personal Information With Strong Passwords.
            2.  Keep Personal Information Private.
            3.  Make Sure Your Devices Are Secure.
            4.  Pay Attention to Software Updates.
            5.  Be Careful About Wifi.
            6.  Use Up Two-Factor Authentication.
            7.  Back Up Your Personal Data.
            """
        )
        st.write("[Learn More](https://safety.google/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PHOTOGRAPHY ----
with st.container():
    st.write("---")
    st.header("My Photography")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("_পড়ন্ত বিকেল_")
        st.write(
            """
            -  _Captured on: 3,March,2019._
            -  _Captured: Me_
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("_গোধূলি বেলা_")
        st.write(
            """
            -  _Captured on: 3,September,2022._
            -  _Captured: Me_
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(nxt_nxt)
    with text_column:
        st.subheader("_বৌদ্ধ বিহার_")
        st.write(
            """
            -  _Captured on: 31,December,2019._
            -  _Captured: Me_
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(flower_img)
    with text_column:
        st.subheader("_Chaina Rose_")
        st.write(
            """
            -  _Captured on: 19,August,2022._
            -  _Captured: Me_
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(chocolate_img)
    with text_column:
        st.subheader("_Chocolate_")
        st.write(
            """
            -  _Good Chocolate,Good Mood._
            """
        )
        st.empty()
