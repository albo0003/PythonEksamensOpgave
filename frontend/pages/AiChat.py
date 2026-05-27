import streamlit as st
import requests

from graph import make_graph


from auth import require_login

require_login()

st.title("AI Chat")

st.subheader("Vælg Data at Sende Med Til Ai")
infoAboutUser = make_graph()

st.subheader("Spørg AI")
question = st.text_input("Ai Assistent", placeholder="Skriv dit spørgsmål her...")



if st.button("Send"):

    response = requests.get(
        "http://backend:8000/ai",
        params={
            "info": infoAboutUser,
            "message": question
        }
    )

    result = response.json()

    st.info(result["ai_answer"])

