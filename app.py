import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(page_title="Birthday Quiz 🎉")

st.title("🎉 Tajný narozeninový kvíz 🎉")

questions = [
    ("Město odkud pocházíš?", "Brno", "B"),
    ("První písmeno abecedy?", "A", "A"),
    ("Jaké zvíře vrní, ale není to kočka (je to divoký a začíná na r :) ?", "Rys", "R"),
    ("Kávový nápoj s mlékem?", "Cappuccino", "C"),
    ("Firma vyrábějící iPhone?", "Apple", "A"),

    ("České město Brno je na?", "Moravě", "M"),
    ("Opak slova ne?", "Ano", "A"),
    ("Opak slova ano?", "Ne", "N"),
    ("První písmeno slova auto?", "A", "A"),
    ("Pořad .... pro nevěstu?", "Růže", "R"),

    ("Kulaté písmeno abecedy?", "O", "O"),
    ("Zvíře se zebrovanými pruhy?", "Zebra", "Z"),
    ("Elektronická pošta anglicky?", "Email", "E"),
    ("Opak dne?", "Noc", "N"),
    ("Telefon od Applu?", "iPhone", "I"),

    ("Den po pondělí?", "Neděle", "N"),
    ("Anglicky „proč“", "Why", "Y")
]

secret = ""

all_correct = True

for i, (question, answer, letter) in enumerate(questions):

    user_answer = st.text_input(f"{i+1}. {question}")

    if user_answer:

        if user_answer.lower().strip() == answer.lower().strip():
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

if secret == "BARCAMANAROZENINY":

    st.balloons()

    st.success("🎉 Tajenka vyluštěna! 🎉")

    st.write("Naskenuj QR kód ❤️")

    GAME_URL = "https://birthday-heart-game-brhfapdpwkc9hx8vjkdtth.streamlit.app/"

    qr = qrcode.make(GAME_URL)

    qr.save("qr.png")

    image = Image.open("qr.png")

    st.image(image, width=300)
