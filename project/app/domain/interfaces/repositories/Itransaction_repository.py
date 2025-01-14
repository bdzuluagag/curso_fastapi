from abc import ABC, abstractmethod
from sqlmodel import Session, select
from domain.models import Transaction


class ITransactionRepository(ABC):

    @abstractmethod
    def create_transaction_repository(self, transaction_data: dict) -> Transaction:
        pass

    @abstractmethod
    def get_transactions_repository(self) -> list[Transaction]:
        pass