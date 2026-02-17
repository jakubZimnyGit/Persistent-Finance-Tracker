from app.crud import create_transaction

def test_create_transaction_valid_data():
    tx = create_transaction(100.0, "Kawa", "Living Expenses")
    assert tx is not None
    assert tx.amount == 100.0
    assert tx.description == "Kawa"

def test_create_transaction_invalid_data():
    assert create_transaction(0, "Opis", "Kategoria") is None
    assert create_transaction(100, "", "Kategoria") is None