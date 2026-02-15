import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import streamlit as st

Base = declarative_base()

def get_engine():
    db_name = st.session_state.get("db_name", "finance.db")
    return create_engine(f"sqlite:///./{db_name}", connect_args={"check_same_thread": False})

def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    if st.session_state.get("db_name") == "mock.db":
        ensure_mock_data()

def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

def ensure_mock_data():
    from .models import Transaction
    
    db = get_db()
    try:
        count = db.query(func.count(Transaction.id)).scalar()
        if count > 0:
            return

        start_date = datetime(2025, 12, 1)
        current_date = datetime.now()
        temp_date = start_date
        
        while temp_date <= current_date:
            if temp_date.day == 1:
                db.add(Transaction(amount=7200.0, description="Monthly Salary", category="Income", date=temp_date))
                db.add(Transaction(amount=-1500.0, description="Savings Transfer", category="Savings", date=temp_date))
            
            if random.random() < 0.7:
                num_expenses = random.randint(1, 2)
                for _ in range(num_expenses):
                    db.add(Transaction(
                        amount=-round(random.uniform(20, 300), 2),
                        description=random.choice(["Biedronka", "Lidl", "Fuel", "Netflix", "Gym", "Cinema"]),
                        category=random.choice(["Food", "Transport", "Entertainment"]),
                        date=temp_date + timedelta(hours=random.randint(9, 18))
                    ))
            temp_date += timedelta(days=1)
        
        db.commit()
    except Exception as e:
        print(f"Mock generation error: {e}")
        db.rollback()
    finally:
        db.close()