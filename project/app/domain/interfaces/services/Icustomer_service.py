from abc import ABC
from domain.dto import Response
from domain.models import CustomerCreate, CustomerUpdate


class ICustomerService(ABC):

    def create_customer_service(self, customer_data: CustomerCreate) -> Response:
        pass

    def get_customer_service(self, customer_id: int) -> Response:
        pass

    def delete_customer_service(self, customer_id: int) -> Response:
        pass

    def update_customer_service(self, customer_id: int, customer_data: CustomerUpdate) -> Response:
        pass

    def get_all_customers_service(self) -> Response:
        pass

    def get_customer_plans_service(self, customer_id: int) -> Response:
        pass