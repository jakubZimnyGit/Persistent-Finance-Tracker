from .models import Transaction
from .database import get_db

def create_transaction(amount, description, category):
    if amount > 0 and description and category:
        new_transaction = Transaction(amount=amount, description=description, category=category)
        return new_transaction
    
def save_transaction(transaction: Transaction):
    pass