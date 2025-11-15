import streamlit as st
from agent.prompts import BUYER_QUESTIONS, SELLER_QUESTIONS
from agent.logic import score_buyer, score_seller

st.title("🏡 Real Estate Lead Pre-Screener")

role = st.radio("Lead Type", ["Buyer", "Seller"])

answers = {}

if role == "Buyer":
    for q in BUYER_QUESTIONS:
        answers[q] = st.text_input(q)
else:
    for q in SELLER_QUESTIONS:
        answers[q] = st.text_input(q)

if st.button("Analyze Lead"):
    if role=="Buyer":
        score = score_buyer({
            "preapproved": answers[BUYER_QUESTIONS[0]],
            "budget": answers[BUYER_QUESTIONS[1]],
            "timeframe": answers[BUYER_QUESTIONS[2]],
        })
    else:
        score = score_seller({
            "reason": answers[SELLER_QUESTIONS[0]],
            "timeframe": answers[SELLER_QUESTIONS[1]],
        })

    st.success(f"Lead Score: {score}")
