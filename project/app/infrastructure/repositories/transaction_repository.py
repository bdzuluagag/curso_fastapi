from domain.interfaces.repositories.Itransaction_repository import ITransactionRepository
from sqlmodel import select, Session
from domain.models import Transaction

class TransactionRepository(ITransactionRepository):

    def __init__(self, session = Session):
        self.session = session


    def create_transaction_repository(self, transaction_data: dict) -> Transaction:
        transaction = Transaction.model_validate(transaction_data)
        self.session.add(transaction)
        self.session.commit()
        self.session.refresh(transaction)
        return transaction
    
    
    def get_transactions_repository(self) -> list[Transaction]:
        return self.session.exec(select(Transaction)).all()