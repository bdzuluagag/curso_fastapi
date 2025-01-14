from abc import ABC, abstractmethod
from domain.dto import Response
from domain.models import CustomerCreate, CustomerUpdate


class ICustomerService(ABC):

    @abstractmethod
    def create_customer_service(self, customer_data: CustomerCreate) -> Response:
        pass

    @abstractmethod
    def get_customer_service(self, customer_id: int) -> Response:
        pass

    @abstractmethod
    def delete_customer_service(self, customer_id: int) -> Response:
        pass
    
    @abstractmethod
    def update_customer_service(self, customer_id: int, customer_data: CustomerUpdate) -> Response:
        pass
    
    @abstractmethod
    def get_all_customers_service(self) -> Response:
        pass