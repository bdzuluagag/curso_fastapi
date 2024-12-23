from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import CustomerCreate, CustomerUpdate, EnumState, Plan
from infrastructure.repositories.customer_repository import CustomerRepository
from domain.dto import Response


def create_customer_service(customer_data: CustomerCreate, repository: CustomerRepository) -> Response:
    existing_customer = repository.get_customer_by_email_repository(customer_data.email)
    if existing_customer:
        return Response(success=False, message="Email already registered", data=None)

    customer = repository.create_customer_repository(customer_data.model_dump())
    return Response(success=True, message="Customer created", data=customer)


def get_customer_service(customer_id: int, repository: CustomerRepository) -> Response:
    customer = repository.get_customer_repository(customer_id)
    if not customer:
        return Response(success=False, message="Customer doesn't exist", data=None)
    
    return Response(success=True, message="Customer retrieved", data=customer)


def delete_customer_service(customer_id: int, repository: CustomerRepository) -> Response:
    customer = repository.get_customer_repository(customer_id)
    if not customer:
        return Response(success=False, message="Customer doesn't exist", data=None)
    
    repository.delete_customer_service(customer)
    return Response(success=True, message="Customer deleted", data=None)


def update_customer_service(customer_id: int, customer_data: CustomerUpdate, repository: CustomerRepository) -> Response:
    customer = repository.get_customer_repository(customer_id)
    if not customer:
        return Response(success=False, message="Customer doesn't exist", data=None)
    
    customer_dict = customer_data.model_dump(exclude_unset=True)
    repository.update_customer_repository(customer, customer_dict)
    return Response(success=True, message="Customer updated", data=None)


def get_all_customers_service(repository: CustomerRepository) -> Response:
    customers = repository.get_all_customers_repository()
    if not customers:
        return Response(success=False, message="No customers found", data=None)
    
    return Response(success=True, message="Customers retrieved", data=customers)


def suscribe_to_plan_service(customer_id: int, plan_id: int, customer_repository: CustomerRepository, plan_repository: PlanRepository, state: EnumState) -> Response:
    customer = customer_repository.get_customer_repository(customer_id)
    plan = plan_repository.get_plans_repository(plan_id)
    if not customer or not plan:
        return Response(success=False, message="Customer or Plan doesn't exist", data=None)
    
    customer_plan = customer_repository.suscribe_to_plan_repository(customer.id, plan.id, state)
    return Response(success=True, message="Customer suscribed to plan", data=customer_plan)


def get_customer_plans_service(customer_id: int, repository: CustomerRepository) -> Response:
    customer = repository.get_customer_repository(customer_id)
    if not customer:
        return Response(success=False, message="Customer doesn't exist", data=None)
    
    return Response(success=True, message="Customer plans retrieved", data=customer.plans)


