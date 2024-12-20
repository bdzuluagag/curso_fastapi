
from sqlmodel import select
from fastapi import HTTPException, status
from domain.models import Transaction, TransactionCreate, Customer
from infrastructure.db import SessionDep

def create_transaction(transaction_data: TransactionCreate, session: SessionDep) -> Transaction:
    transaction_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_dict.get("customer_id"))
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    transaction = Transaction.model_validate(transaction_dict)
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return transaction

def get_transactions(session: SessionDep) -> list[Transaction]:
    return session.exec(select(Transaction)).all()