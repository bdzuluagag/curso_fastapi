from fastapi import APIRouter, HTTPException, Query, status
from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import Customer, CustomerCreate, CustomerUpdate, CustomerPlan, EnumState, Plan
from infrastructure.db import SessionDep
from infrastructure.repositories.customer_repository import CustomerRepository
from services.customer_service import create_customer_service, get_all_customers_service, get_customer_service, get_customer_plans_service, update_customer_service, delete_customer_service, suscribe_to_plan_service, desuscribe_to_plan_service

router = APIRouter(tags=['customers'])


@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer_endpoint(customer_data: CustomerCreate):
    repository = CustomerRepository(SessionDep)
    response = create_customer_service(customer_data, repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
    
    return response.data


@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    response = get_customer_service(customer_id, repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.delete("/customers/{customer_id}")
async def delete_customer_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    response = delete_customer_service(customer_id, repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.message


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer_endpoint(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    repository = CustomerRepository(session)
    response = update_customer_service(customer_id, customer_data, repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.get("/customers", response_model=list[Customer])
async def getall_customer_endpoint(session: SessionDep):
    repository = CustomerRepository(session)
    response = get_all_customers_service(repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.post("/customers/{customer_id}/plans/{plan_id}/suscribe", response_model=CustomerPlan)
async def suscribe_to_plan_endpoint(customer_id: int, plan_id: int, session: SessionDep):
    customer_repository = CustomerRepository(session)
    plan_repository = PlanRepository(session)
    response = suscribe_to_plan_service(customer_id, plan_id, customer_repository, plan_repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.post("/customers/{customer_id}/plans/{plan_id}/desuscribe", response_model=CustomerPlan)
async def desuscribe_to_plan_endpoint(customer_id: int, plan_id: int, session: SessionDep):
    customer_repository = CustomerRepository(session)
    plan_repository = PlanRepository(session)
    response = desuscribe_to_plan_service(customer_id, plan_id, customer_repository, plan_repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data
    

@router.get("/customers/{customer_id}/plans", response_model=list[Plan])
async def get_customer_plans_endpoint(customer_id: int, session: SessionDep):
    repository = CustomerRepository(session)
    response = get_customer_plans_service(customer_id, repository)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data