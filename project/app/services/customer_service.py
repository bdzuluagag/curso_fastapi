from sqlmodel import Session
from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import CustomerCreate, CustomerUpdate
from infrastructure.repositories.customer_repository import CustomerRepository
from domain.dto import Response


class CustomerService:

    def __init__(self, repository: CustomerRepository):
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


    def suscribe_to_plan_service(self, customer_id: int, plan_id: int, plan_repository: PlanRepository) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        plan = plan_repository.get_plan_repository(plan_id)
        if not customer or not plan:
            return Response(success=False, message="Customer or Plan doesn't exist", data=None)
        
        # Check if already subscribed
        if self.repository.is_already_subscribed(customer_id, plan_id):
            return Response(success=False, message="Customer already subscribed to this plan", data=None)
        
        customer_plan = self.repository.suscribe_to_plan_repository(customer.id, plan.id)
        return Response(success=True, message="Customer subscribed to plan", data=customer_plan)


    def unsuscribe_to_plan_service(self, customer_id: int, plan_id: int, plan_repository: PlanRepository) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        plan = plan_repository.get_plan_repository(plan_id)
        if not customer or not plan:
            return Response(success=False, message="Customer or Plan doesn't exist", data=None)
        
        if not self.repository.is_already_subscribed(customer_id, plan_id):
            return Response(success=False, message="Customer wasn't suscribed", data=None)
        
        customer_plan = self.repository.unsuscribe_to_plan_repository(customer.id, plan.id)
        return Response(success=True, message="Customer unsuscribed to plan", data=customer_plan)


    def get_customer_plans_service(self, customer_id: int) -> Response:
        customer = self.repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        return Response(success=True, message="Customer plans retrieved", data=customer.plans)


