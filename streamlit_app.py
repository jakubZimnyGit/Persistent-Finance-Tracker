import streamlit as st
import pandas as pd
import plotly.express as px
from app.database import init_db
from app.crud import get_all_transactions

if __name__ == "__main__":
    if "db_name" not in st.session_state:
        st.session_state.db_name = "finance.db"

    st.sidebar.header("System Settings")
    
    db_choice = st.sidebar.selectbox(
        "Select Database Mode:",
        ["Standard (finance.db)", "Mock Data (mock.db)"],
        index=0 if st.session_state.db_name == "finance.db" else 1
    )

    new_db = "finance.db" if "Standard" in db_choice else "mock.db"
    
    if new_db != st.session_state.db_name:
        st.session_state.db_name = new_db
        init_db()
        st.rerun()

    init_db() 

    st.title("Persistent Finance Tracker")
    st.info(f"Connected to: **{st.session_state.db_name}**")
    
    if st.session_state.db_name == "mock.db":
        st.warning("⚠️ **Demo Mode:** You are viewing randomly generated mock data. No changes will be saved to your primary database.")
    
    transactions = get_all_transactions()
    
    if transactions:
        df_all = pd.DataFrame([{
            "ID": t.id,
            "Amount": t.amount,
            "Description": t.description,
            "Category": t.category,
            "Date": pd.to_datetime(t.date),
        } for t in transactions]).sort_values("ID")

        st.sidebar.header("Dashboard Filters")
        filter_option = st.sidebar.radio(
            "Select Time Range:", 
            ["All Time", "This Month", "Last 30 Days"]
        )

        df = df_all.copy()
        current_date = pd.Timestamp.now()

        if filter_option == "This Month":
            df = df_all[(df_all["Date"].dt.month == current_date.month) & (df_all["Date"].dt.year == current_date.year)]
        elif filter_option == "Last 30 Days":
            df = df_all[df_all["Date"] >= (current_date - pd.Timedelta(days=30))]

        st.divider()
        
        total_income = df[df["Amount"] > 0]["Amount"].sum()
        real_expenses = df[(df["Amount"] < 0) & (df["Category"] != "Savings")]["Amount"].sum()
        total_savings = df_all[df_all["Category"] == "Savings"]["Amount"].abs().sum()
        current_balance = df_all["Amount"].sum() 

        row1_col1, row1_col2 = st.columns(2)
        row1_col1.metric("Current Balance", f"{current_balance:,.2f} PLN")
        row1_col2.metric("Total Income", f"{total_income:,.2f} PLN")

        row2_col1, row2_col2 = st.columns(2)
        row2_col1.metric("Living Expenses", f"{abs(real_expenses):,.2f} PLN")
        row2_col2.metric("Total Savings", f"{total_savings:,.2f} PLN")
        
        st.divider()

        if not df.empty:
            df["Date_Str"] = df["Date"].dt.strftime("%Y-%m-%d")
            df_balance = df.copy()
            df_balance["Current Balance"] = df_balance["Amount"].cumsum()
            
            fig_balance = px.line(
                df_balance, 
                x=range(len(df_balance)), 
                y="Current Balance",
                markers=True, 
                title=f"Balance History ({filter_option})",
                hover_data={"Date_Str": True}
            )
            
            fig_balance.update_layout(
                height=500,
                xaxis=dict(
                    tickangle=-45,
                    nticks=10,
                    rangeslider=dict(visible=True),
                    tickmode='array',
                    tickvals=list(range(len(df_balance))),
                    ticktext=df_balance["Date_Str"],
                    title="Transaction Timeline"
                ),
                yaxis=dict(title="Balance (PLN)")
            )
            st.plotly_chart(fig_balance, use_container_width=True)

            expenses_df = df[df["Amount"] < 0].copy()
            if not expenses_df.empty:
                expenses_df["Abs_Amount"] = expenses_df["Amount"].abs()
                fig_pie = px.pie(
                    expenses_df, 
                    values='Abs_Amount', 
                    names='Category', 
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.RdBu
                )
                st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.warning("Database is empty. Add transactions to see the dashboard!")