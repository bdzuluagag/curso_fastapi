from sqlmodel import Session
from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import CustomerCreate, CustomerUpdate
from domain.dto import Response
from domain.interfaces.repositories.IcustomerRepository import ICustomerRepository


class CustomerService:

    def __init__(self, repository: ICustomerRepository): 
        self.repository = repository

    def create_customer_service(self, customer_data: CustomerCreate) -> Response:
        existing_customer = self.repository.get_customer_by_email_repository(customer_data.email)
        if existing_customer:
            return Response(success=False, message="Email already registered", data=None)

        customer = self.repository.create_customer_repository(customer_data.model_dump())
        return Response(success=True, message="Customer created", data=customer)


    def get_customer_service(self, customer_id: int) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        return Response(success=True, message="Customer retrieved", data=customer)


    def delete_customer_service(self, customer_id: int) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        self.repository.delete_customer_repository(customer)
        return Response(success=True, message="Customer deleted", data=None)


    def update_customer_service(self, customer_id: int, customer_data: CustomerUpdate) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        customer_dict = customer_data.model_dump(exclude_unset=True)
        customer_updated = self.repository.update_customer_repository(customer, customer_dict)
        return Response(success=True, message="Customer updated", data=customer_updated)


    def get_all_customers_service(self) -> Response: 
        customers = self.repository.get_all_customers_repository()
        if not customers:
            return Response(success=False, message="No customers found", data=None)
        
        return Response(success=True, message="Customers retrieved", data=customers)


    def get_customer_plans_service(self, customer_id: int) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        return Response(success=True, message="Customer plans retrieved", data=customer.plans)


