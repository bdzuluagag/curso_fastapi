from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from domain.models import Transaction, TransactionCreate, Customer
from infrastructure.db import SessionDep
from services.transaction_service import create_transaction, get_transactions

router = APIRouter(tags=['transactions'])

@router.post("/transactions", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction_endpoint(transaction_data: TransactionCreate, session: SessionDep):
    return create_transaction(transaction_data, session)

@router.get("/transactions", response_model=list[Transaction])
async def get_transactions_endpoint(session: SessionDep):
    return get_transactions(session)