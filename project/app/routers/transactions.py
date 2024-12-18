from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from models import Transaction, TransactionCreate, Customer
from db import SessionDep

router = APIRouter(tags=['transactions'])


@router.post("/transactions", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_data: TransactionCreate, session: SessionDep):
    transaction_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_dict.get("customer_id"))
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    transaction = Transaction.model_validate(transaction_dict)
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction


@router.get("/transactions", response_model=list[Transaction])
async def get_transactions(session: SessionDep):
    return session.exec(select(Transaction)).all()

