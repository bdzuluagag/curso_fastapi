from fastapi import APIRouter, status, Depends
from domain.models import Transaction, TransactionCreate
from infrastructure.db import SessionDep
from infrastructure.repositories.transaction_repository import TransactionRepository
from services.transaction_service import TransactionService
from infrastructure.repositories.customer_repository import CustomerRepository
from application.controllers.transaction_controller import TransactionController

router = APIRouter(tags=['transactions'])

def get_transaction_controller(session: SessionDep):
    repository = TransactionRepository(session)
    customer_repository = CustomerRepository(session)
    service = TransactionService(repository, customer_repository)
    return TransactionController(service)


@router.post("/transactions", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction_endpoint(transaction_data: TransactionCreate, controller: TransactionController = Depends(get_transaction_controller)):
    return controller.create_transaction_controller(transaction_data)

@router.get("/transactions", response_model=list[Transaction])
async def get_transactions_endpoint(controller: TransactionController = Depends(get_transaction_controller)):
    return controller.get_transactions_controller()