import pytest
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.crud import create_transaction, save_transaction, get_all_transactions, delete_transaction

@pytest.fixture(autouse=True)
def setup_db(monkeypatch):
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    @contextmanager
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    monkeypatch.setattr("app.crud.get_db", override_get_db)

def test_full_transaction_lifecycle():
    """Test sprawdza pełny cykl życia transakcji: Tworzenie -> Zapis -> Pobieranie -> Usuwanie."""
    
    tx_expense = create_transaction(amount=50.0, description="Lunch", category="Food")
    saved_expense = save_transaction(tx_expense)
    
    assert saved_expense is not None
    assert saved_expense.amount == -50.0 

    tx_income = create_transaction(amount=1000.0, description="Salary", category="Income")
    saved_income = save_transaction(tx_income)
    
    assert saved_income.amount == 1000.0

    all_tx = get_all_transactions()
    assert len(all_tx) == 2
    
    expense_id = saved_expense.id
    delete_success = delete_transaction(expense_id)
    
    assert delete_success is True
    assert len(get_all_transactions()) == 1

def test_create_transaction_validation():
    """Test sprawdza czy nie da się stworzyć pustej transakcji."""
    invalid_tx = create_transaction(amount=0, description="Nic", category="Income")
    assert invalid_tx is None