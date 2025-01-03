from fastapi import APIRouter, HTTPException, status
from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import Customer, CustomerCreate, CustomerUpdate, CustomerPlan, Plan
from infrastructure.db import SessionDep
from infrastructure.repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService
router = APIRouter(tags=['customers'])


@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer_endpoint(customer_data: CustomerCreate, session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.create_customer_service(customer_data)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
    
    return response.data


@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.get_customer_service(customer_id)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.delete("/customers/{customer_id}")
async def delete_customer_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.delete_customer_service(customer_id)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.message


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer_endpoint(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.update_customer_service(customer_id, customer_data)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.get("/customers", response_model=list[Customer])
async def getall_customer_endpoint(session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.get_all_customers_service()
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.post("/customers/{customer_id}/plans/{plan_id}/suscribe", response_model=CustomerPlan)
async def suscribe_to_plan_endpoint(customer_id: int, plan_id: int, session: SessionDep):
    customer_repository = CustomerRepository(session)
    plan_repository = PlanRepository(session)
    service = CustomerService(customer_repository)
    response = service.suscribe_to_plan_service(customer_id, plan_id, plan_repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.post("/customers/{customer_id}/plans/{plan_id}/unsuscribe", response_model=CustomerPlan)
async def unsuscribe_to_plan_endpoint(customer_id: int, plan_id: int, session: SessionDep):
    customer_repository = CustomerRepository(session)
    plan_repository = PlanRepository(session)
    service = CustomerService(customer_repository)
    response = service.unsuscribe_to_plan_service(customer_id, plan_id, plan_repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data
    

@router.get("/customers/{customer_id}/plans", response_model=list[Plan])
async def get_customer_plans_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    response = service.get_customer_plans_service(customer_id)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data