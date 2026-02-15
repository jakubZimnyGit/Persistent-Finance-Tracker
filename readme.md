# 💰 Persistent Finance Tracker

A robust, full-stack personal finance dashboard built with **Python**, **Streamlit**, and **SQLAlchemy**. This application allows users to manage their finances, track expenses, and visualize their balance history with ease. It features a dual-database system for seamless switching between real personal data and a generated demo environment.

## 🌟 Key Features

* **Dual-Mode Database**: Toggle between your private `finance.db` and a pre-populated `mock.db` for demonstration purposes.
* **Automated Data Seeding**: The application automatically generates realistic financial data for the Mock mode—no manual setup required.
* **Interactive Dashboard**:
    * **2x2 Metric Grid**: Clear view of Current Balance, Total Income, Living Expenses, and Savings.
    * **Dynamic Timeline**: A Plotly-powered line chart with a range slider for deep-diving into transaction history.
    * **Expense Distribution**: A hollow pie chart showing spending by category.
* **Time-Range Filtering**: Analyze data for "All Time", "This Month", or the "Last 30 Days".
* **Containerized Environment**: Fully Dockerized for "one-click" local deployment.

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Database ORM**: SQLAlchemy
* **Data Analysis**: Pandas
* **Visualization**: Plotly
* **Deployment**: Docker & Docker Compose

## 🚀 Quick Start

### Using Docker (Recommended)
1. Clone the repository.
2. Run the following command in the terminal:
   `docker-compose up`
3. Open your browser at `http://localhost:8501`.

### Manual Setup
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the application:
   `streamlit run main.py`

## 📈 Future Roadmap

* **CSV/Excel Data Import**: Implement a file upload feature using `st.file_uploader` to allow users to bulk-import transactions from bank statements.
* **Budgeting Goals**: Set monthly spending limits per category and receive visual alerts when approaching them.
* **Predictive Analytics**: Use basic machine learning to forecast end-of-month balance based on spending habits.

## 📝 License
This project is open-source and available under the MIT License.