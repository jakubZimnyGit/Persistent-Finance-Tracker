from .models import Transaction
from .database import get_db

def create_transaction(amount, description, category):
    if amount > 0 and description and category:
        new_transaction = Transaction(amount=amount, description=description, category=category)
        return new_transaction
    
def save_transaction(transaction: Transaction):
    with get_db() as db:
        try:
            db.add(transaction)
            db.commit()
            db.refresh(transaction)
            return transaction
        except Exception as e:
            db.rollback()
            print(f"Error saving transaction: {e}")
            return None
        
def get_all_transactions():
    with get_db() as db:
        try:
            transactions = db.query(Transaction).order_by(Transaction.date.desc()).all()
            return transactions
        except Exception as e:
            print(f"Error retrieving transactions: {e}")
            return []