import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Transaction

MOCK_DATABASE_URL = "sqlite:///./mock.db"

def generate_mock_data():
    engine = create_engine(MOCK_DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Parametry symulacji
    start_date = datetime(2025, 12, 1) # Startujemy od grudnia 2025
    end_date = datetime(2026, 2, 15)   # Do dzisiaj
    
    current_date = start_date
    print("Generating structured mock data...")

    while current_date <= end_date:
        if current_date.day == 1:
            # Wypłata
            db.add(Transaction(
                amount=7200.0,
                description="Monthly Salary - Tech Corp",
                category="Salary",
                date=current_date
            ))
            db.add(Transaction(
                amount=-1500.0,
                description="Transfer to Emergency Fund",
                category="Savings",
                date=current_date + timedelta(hours=2)
            ))
            db.add(Transaction(
                amount=-2500.0,
                description="Apartment Rent & Utilities",
                category="Rent",
                date=current_date + timedelta(days=2)
            ))
            db.add(Transaction(
                amount=-60.0,
                description="Internet & Spotify",
                category="Entertainment",
                date=current_date + timedelta(days=3)
            ))

        if random.random() < 0.7:
            num_expenses = random.randint(1, 3) 
            for _ in range(num_expenses):
                cat = random.choice(["Food", "Transport", "Food", "Entertainment"]) 
                
                if cat == "Food":
                    amount = -round(random.uniform(20, 150), 2)
                    desc = random.choice(["Biedronka", "Lidl", "Dinner Out", "UberEats"])
                elif cat == "Transport":
                    amount = -round(random.uniform(10, 80), 2)
                    desc = random.choice(["Fuel", "Bolt", "Parking", "Bus Ticket"])
                else:
                    amount = -round(random.uniform(30, 200), 2)
                    desc = random.choice(["Cinema", "Gym", "Pharmacy", "Bookstore"])

                db.add(Transaction(
                    amount=amount,
                    description=desc,
                    category=cat,
                    date=current_date + timedelta(hours=random.randint(9, 20))
                ))

        current_date += timedelta(days=1)

    db.commit()
    db.close()
    print("Success! 'mock.db' generated with a realistic financial rhythm.")

if __name__ == "__main__":
    generate_mock_data()