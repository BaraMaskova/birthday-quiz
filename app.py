import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(page_title="Birthday Quiz 🎉")

st.title("🎉 Tajný narozeninový kvíz 🎉")

questions = [
    ("Hlavní město Německa?", "Berlín", "B"),
    ("První písmeno abecedy?", "A", "A"),
    ("Jaké zvíře vrní?", "Rys", "R"),
    ("Nápoj z kávy?", "Cappuccino", "C"),
    ("Značka iPhonu?", "Apple", "A"),
]

secret = ""

all_correct = True

for i, (question, answer, letter) in enumerate(questions):

    user_answer = st.text_input(f"{i+1}. {question}")

    if user_answer:

        if user_answer.lower() == answer.lower():
            st.success(f"✅ Správně! Písmeno: {letter}")
            secret += letter
        else:
            st.error("❌ Špatně")
            all_correct = False
    else:
        all_correct = False

st.divider()

display_secret = " ".join(secret)

st.subheader(f"Tajenka: {display_secret}")

FULL_SECRET = "BARCA_MA_NAROZENINY"

if secret == "BARCA":

    st.balloons()

    st.success("🎉 Tajenka odhalena! 🎉")

    st.write("Naskenuj QR kód ❤️")

    GAME_URL = "https://SEM_DAS_SVOJI_STREAMLIT_URL"

    qr = qrcode.make(GAME_URL)

    qr.save("qr.png")

    image = Image.open("qr.png")

    st.image(image, width=300)