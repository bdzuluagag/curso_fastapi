from db import SessionDep
from fastapi import HTTPException, APIRouter, Query, status
from sqlmodel import select

from models import Customer, CustomerCreate, CustomerUpdate, CustomerPlan, EnumState, Plan


router = APIRouter(tags=['customers'])


@router.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    existing_customer = session.exec(select(Customer).where(Customer.email == customer_data.email)).first()
    if existing_customer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer doesn't exist")
    return customer


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    session.delete(customer)
    session.commit()
    return {"detail": "ok"}


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer doesn't exists")
    
    customer_dict = customer_data.model_dump(exclude_unset=True)
    customer.sqlmodel_update(customer_dict)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.get("/customers", response_model=list[Customer])
async def getall_customer(session: SessionDep):
    return session.exec(select(Customer)).all() 


@router.post("/customers/{customer_id}/plans/{plan_id}", response_model=CustomerPlan)
async def suscribe_to_plan(customer_id: int, plan_id: int, session: SessionDep, state: EnumState = Query()):
    customer = session.get(Customer, customer_id)
    plan = session.get(Plan, plan_id)

    if not customer or not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer or Plan doesn't exist")
    
    customer_plan = CustomerPlan(customer_id=customer_id, plan_id=plan_id, state=state)
    session.add(customer_plan)
    session.commit()
    session.refresh(customer_plan)
    return customer_plan


@router.get("/customers/{customer_id}/plans", response_model=list[Plan])
async def get_customer_plans(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customers doesn't exist")

    return customer.plans