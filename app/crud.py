from .models import Transaction
from .database import get_db

def create_transaction(amount: float, description: str, category: str, date=None):
    if amount != 0 and description and category:
        return Transaction(
            amount=amount, 
            description=description, 
            category=category,
            date=date
        )
    return None

def save_transaction(transaction: Transaction):
    with get_db() as db:
        try:
            if transaction.category == "Income":
                transaction.amount = abs(transaction.amount)
            else:
                transaction.amount = -abs(transaction.amount)
            
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
            return db.query(Transaction).order_by(Transaction.date.asc(), Transaction.id.asc()).all()
        except Exception as e:
            print(f"Error retrieving transactions: {e}")
            return []

def delete_transaction(transaction_id: int):
    with get_db() as db:
        try:
            transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                db.delete(transaction)
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            print(f"Error deleting transaction: {e}")
            return False

def update_transaction_amount(transaction_id: int, amount: float):
    with get_db() as db:
        try:
            transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
            if transaction:
                if transaction.category == "Income":
                    transaction.amount = abs(amount)
                else:
                    transaction.amount = -abs(amount)
                
                db.commit()
                db.refresh(transaction)
                return transaction
            return None
        except Exception as e:
            db.rollback()
            print(f"Error updating transaction: {e}")
            return None