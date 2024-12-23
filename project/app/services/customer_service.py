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
    customer_updated = repository.update_customer_repository(customer, customer_dict)
    return Response(success=True, message="Customer updated", data=customer_updated)


def get_all_customers_service(repository: CustomerRepository) -> Response: 
    customers = repository.get_all_customers_repository()
    if not customers:
        return Response(success=False, message="No customers found", data=None)
    
    return Response(success=True, message="Customers retrieved", data=customers)


def suscribe_to_plan_service(customer_id: int, plan_id: int, customer_repository: CustomerRepository, plan_repository: PlanRepository) -> Response:
    customer = customer_repository.get_customer_repository(customer_id)
    plan = plan_repository.get_plan_repository(plan_id)
    if not customer or not plan:
        return Response(success=False, message="Customer or Plan doesn't exist", data=None)
    
    # Check if already subscribed
    if customer_repository.is_already_subscribed(customer_id, plan_id):
        return Response(success=False, message="Customer already subscribed to this plan", data=None)
    
    customer_plan = customer_repository.suscribe_to_plan_repository(customer.id, plan.id)
    return Response(success=True, message="Customer subscribed to plan", data=customer_plan)


def desuscribe_to_plan_service(customer_id: int, plan_id: int, customer_repository: CustomerRepository, plan_repository: PlanRepository) -> Response:
    customer = customer_repository.get_customer_repository(customer_id)
    plan = plan_repository.get_plan_repository(plan_id)
    if not customer or not plan:
        return Response(success=False, message="Customer or Plan doesn't exist", data=None)
    
    if not customer_repository.is_already_subscribed(customer_id, plan_id):
        return Response(success=False, message="Customer wasn't suscribed", data=None)
    
    customer_plan = customer_repository.desuscribe_to_plan_repository(customer.id, plan.id)
    return Response(success=True, message="Customer desuscribed to plan", data=customer_plan)


def get_customer_plans_service(customer_id: int, repository: CustomerRepository) -> Response:
    customer = repository.get_customer_repository(customer_id)
    if not customer:
        return Response(success=False, message="Customer doesn't exist", data=None)
    
    return Response(success=True, message="Customer plans retrieved", data=customer.plans)


