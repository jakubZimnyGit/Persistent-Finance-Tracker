import streamlit as st
from app.crud import create_transaction, save_transaction
from app.config import CATEGORIES


amount = st.number_input("Amount", min_value=0.0, step=0.01, value=None)
description = st.text_input("short description", max_chars=65, help="Provide a brief description of the transaction.")
category = st.selectbox("Category", options=CATEGORIES)

if st.button("Add Transaction"):
    transaction = create_transaction(amount, description, category)

    transaction = save_transaction(transaction)
    
    if transaction:
        st.success("Transaction added successfully!")
    else:
        st.error("Failed to add transaction. Please check your input.")




