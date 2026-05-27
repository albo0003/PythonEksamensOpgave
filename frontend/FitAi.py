import streamlit as st


import requests
import matplotlib.pyplot as plt

from graph import make_graph



from auth import require_login

require_login()


#rest
st.title("FitAI")

st.subheader("Indtast dine oplysninger")

weight = st.number_input("Vægt (kg)", min_value=1.0)
height = st.number_input("Højde (cm)", min_value=1.0)

if st.button("Beregn BMI"):

    response = requests.get(
        "http://backend:8000/info",
        params={
            "username": st.session_state["user"],
            "weight": weight,
            "height": height
        }
    )

    result = response.json()

    st.success(f"BMI: {result['BMI']}")
    st.info(f"Dagligt kaloriebehov: {result['daily_calories']}")


st.subheader("Vægtudvikling")

make_graph()



