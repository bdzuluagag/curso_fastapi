from fastapi import HTTPException, status
from domain.models import TransactionCreate
from domain.interfaces.services.Itransaction_service import ITransactionService


class TransactionController:

    def __init__(self, service: ITransactionService):
        self.service = service


    def create_transaction_controller(self, transaction_data: TransactionCreate):
        response = self.service.create_transaction_service(transaction_data)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
        
        return response.data
    

    def get_transactions_controller(self):
        response = self.service.get_transactions_service()
        if not response.success:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
        
        return response.data