import streamlit as st
import pandas as pd
from app.crud import get_all_transactions, update_transaction_amount, delete_transaction

st.title("List of Transactions")
transactions = get_all_transactions()
if transactions:
    df = pd.DataFrame([{
        "ID": t.id,
        "Amount": t.amount,
        "Description": t.description,
        "Category": t.category,
        "Date": t.date.strftime("%Y-%m-%d"),
    } for t in transactions])
    

    edited_df = st.data_editor(
        df, 
        disabled=["ID", "Description", "Category", "Date"],
        hide_index=True,
        key="my_editor"
    )

    st.sidebar.title("Manage Transactions")
    with st.sidebar:
        st.subheader("Delete Transaction")
        to_delete = st.selectbox(
                "Select to remove:",
                options=transactions,
                format_func=lambda x: f"{x.description} ({x.amount})"
            )

        if st.button("Delete Selected", type="primary", use_container_width=True):
            st.session_state["confirm_delete"] = True
        if st.session_state.get("confirm_delete"):
            st.error(f"Do you really want to delete this transaction?")
            col_yes, col_no = st.columns(2)

            with col_yes:
                if st.button("Yes", key="confirm_yes", use_container_width=True):
                    delete_transaction(to_delete.id)
                    st.session_state["confirm_delete"] = False
                    st.rerun()

            with col_no:
                if st.button("No", key="confirm_no", use_container_width=True):
                    st.session_state["confirm_delete"] = False
                    st.rerun()

        changes = st.session_state["my_editor"]["edited_rows"]
        if changes:
            st.divider()
            st.write("Changes detected:")
            if st.button("Save Changes"):
                for row_index, updated_values in changes.items():
                    trans_id = int(df.iloc[int(row_index)]["ID"])
                    new_amount = updated_values["Amount"]
                    update_transaction_amount(trans_id, new_amount)
                    st.success(f"Updated transaction ID {trans_id} to amount {new_amount}")

                st.rerun()
            st.success("Changes saved!")
            
else:
    st.info("No transactions found. Please add some transactions to see them here.")
    
    with st.sidebar:
        st.write("No actions available to perform.")