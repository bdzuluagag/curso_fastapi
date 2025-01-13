from abc import ABC, abstractmethod
from domain.models import Customer

class ICustomerRepository(ABC):

    @abstractmethod
    def get_customer_repository(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_all_customers_repository(self) -> list[Customer]:
        pass

    @abstractmethod
    def get_customer_by_email_repository(self, email: str) -> Customer:
        pass

    @abstractmethod
    def create_customer_repository(self, customer_data: dict) -> Customer:
        pass

    @abstractmethod
    def update_customer_repository(self, customer_id: int, customer: dict) -> dict:
        pass

    @abstractmethod
    def delete_customer_repository(self, customer_id: int) -> dict:
        pass