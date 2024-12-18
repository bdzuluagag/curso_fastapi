from models import CustomerCreate, Customer, CustomerUpdate
from db import SessionDep
from fastapi import HTTPException, APIRouter, status
from sqlmodel import select


router = APIRouter(tags=['customers'])


@router.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
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