from fastapi import APIRouter, Query, status
from domain.models import Customer, CustomerCreate, CustomerUpdate, CustomerPlan, EnumState, Plan
from infrastructure.db import SessionDep
from services.customer_service import create_customer_service, get_all_customers_service, get_customer_service, get_customer_plans_service, update_customer_service, delete_customer_service, suscribe_to_plan_service


router = APIRouter(tags=['customers'])


@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer_endpoint(customer_data: CustomerCreate, session: SessionDep):
    return create_customer_service(customer_data, session)


@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_endpoint(customer_id: int, session: SessionDep):
    return get_customer_service(customer_id, session)


@router.delete("/customers/{customer_id}")
async def delete_customer_endpoint(customer_id: int, session: SessionDep):
    return delete_customer_service(customer_id, session)


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer_endpoint(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    return update_customer_service(customer_id, customer_data, session)


@router.get("/customers", response_model=list[Customer])
async def getall_customer_endpoint(session: SessionDep):
    return get_all_customers_service(session) 


@router.post("/customers/{customer_id}/plans/{plan_id}", response_model=CustomerPlan)
async def suscribe_to_plan_endpoint(customer_id: int, plan_id: int, session: SessionDep, state: EnumState = Query()):
    return suscribe_to_plan_service(customer_id, plan_id, session, state)


@router.get("/customers/{customer_id}/plans", response_model=list[Plan])
async def get_customer_plans_endpoint(customer_id: int, session: SessionDep):
    return get_customer_plans_service(customer_id, session)