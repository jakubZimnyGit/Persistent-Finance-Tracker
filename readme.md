![Tests Status](https://github.com/jakubZimnyGit/Persistent-Finance-Tracker/actions/workflows/tests.yml/badge.svg)

# 💰 Persistent Finance Tracker

A robust, full-stack personal finance dashboard built with **Python**, **Streamlit**, and **SQLAlchemy**. This application allows users to manage their finances, track expenses, and visualize their balance history with ease. It features a dual-database system for seamless switching between real personal data and a generated demo environment.

<img width="1778" height="862" alt="image" src="https://github.com/user-attachments/assets/a4f34a48-5d62-4e0a-8de3-fb1a95d267f2" />

## 🌟 Key Features

* **Dual-Mode Database**: Toggle between your private `finance.db` and a pre-populated `mock.db` for demonstration purposes.
* **Automated Data Seeding**: The application automatically generates realistic financial data for the Mock mode—no manual setup required.
* **Interactive Dashboard**:
    * **2x2 Metric Grid**: Clear view of Current Balance, Total Income, Living Expenses, and Savings.
    * **Dynamic Timeline**: A Plotly-powered line chart with a range slider for deep-diving into transaction history.
    * **Expense Distribution**: A hollow pie chart showing spending by category.
* **Time-Range Filtering**: Analyze data for "All Time", "This Month", or the "Last 30 Days".
* **Containerized Environment**: Fully Dockerized for "one-click" local deployment.
  
<img width="1511" height="639" alt="image" src="https://github.com/user-attachments/assets/f567a205-c8d1-46d4-8ea0-41b8bffa5930" />

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Database ORM**: SQLAlchemy
* **Data Analysis**: Pandas
* **Visualization**: Plotly
* **Infrastructure**: Docker & Docker Compose
* **Deployment**: Streamlit Community Cloud

## 🚀 Quick Start & Demo

### 🌐 Live Demo
You can access the live version of the application here:
[**CLICK HERE FOR LIVE DEMO**](https://finance-tracker-demo.streamlit.app/)

> [!IMPORTANT]
> **Data Persistence Note**: This demo uses a local SQLite database on a temporary cloud drive. 
> To prevent data loss or interference between users, please use the **Mock Mode** for testing. 
> Any data added to the **Standard Mode** will be visible to others and will be reset periodically when the server restarts.

### 🐳 Local Deployment (Docker)
If you want to run the project locally with all dependencies pre-configured:
1. Clone the repository.
2. Run: `docker-compose up`
3. Access at: `http://localhost:8501`

### 🐍 Manual Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `streamlit run main.py`
## 📈 Future Roadmap

* **CSV/Excel Data Import**: Implement a file upload feature using `st.file_uploader` to allow users to bulk-import transactions from bank statements.
* **Persistent Cloud Database**: Migrate from local SQLite to a managed PostgreSQL instance (e.g., Supabase or Neon) to ensure data remains persistent across app restarts.
* **User Authentication**: Add a secure login system to provide each user with a private, isolated environment for their financial data.
* **Budgeting Goals**: Set monthly spending limits per category and receive visual alerts when approaching them.
* **Predictive Analytics**: Use basic machine learning to forecast end-of-month balance based on spending habits.

## 📝 License
This project is open-source and available under the MIT License.
