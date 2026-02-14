import streamlit as st

amount = st.number_input("Amount", min_value=0.0, step=0.01)
description = st.text_input("short description", max_chars=65, help="Provide a brief description of the transaction.")
category = st.selectbox("Category", options=["Food", "Transport", "Entertainment",
                                            "Income", "Investment", "Savings",  "Health",
                                            "Education", "Utilities", "Personal Care",
                                            "Gifts & Donations", "Travel", "Subscriptions", "Other"])

st.button("Add Transaction", on_click=(lambda: st.success("Transaction added successfully!")))