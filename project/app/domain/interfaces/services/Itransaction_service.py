from abc import ABC, abstractmethod
from domain.dto import Response
from domain.models import Transaction, TransactionCreate


class ITransactionService(ABC):

    @abstractmethod
    def create_transaction_service(self, transaction_data: TransactionCreate) -> Response:
        pass


    @abstractmethod
    def get_transactions_service(self) -> Response:
        pass