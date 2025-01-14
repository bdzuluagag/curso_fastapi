from fastapi import HTTPException, status
from domain.models import Transaction, TransactionCreate
from domain.dto import Response
from domain.interfaces.repositories.Itransaction_repository import ITransactionRepository
from domain.interfaces.repositories.Icustomer_repository import ICustomerRepository
from domain.interfaces.services.Itransaction_service import ITransactionService


class TransactionService(ITransactionService):

    def __init__(self, repository: ITransactionRepository, customer_repository: ICustomerRepository):
        self.repository = repository
        self.customer_repository = customer_repository


    def create_transaction_service(self, transaction_data: TransactionCreate) -> Response:
        transaction_dict = transaction_data.model_dump()
        print(transaction_dict)

        transaction = self.repository.create_transaction_repository(transaction_dict)
        return Response(success=True, message= "Transaction done!", data=transaction)


    def get_transactions_service(self) -> Response:
        transactions= self.repository.get_transactions_repository()
        if not transactions:
            return Response(success=False, message= "No transactions yet", data=None)

        return Response(success=True, message= "Transactions retrieved", data=transactions)
