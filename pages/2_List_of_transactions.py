import streamlit as st
import pandas as pd
from app.crud import get_all_transactions

st.title("List of Transactions")
transactions = get_all_transactions()
if transactions:
    df = pd.DataFrame([{
        "Amount": t.amount,
        "Description": t.description,
        "Category": t.category,
        "Date": t.date.strftime("%Y-%m-%d")
    } for t in transactions])
    st.dataframe(df)