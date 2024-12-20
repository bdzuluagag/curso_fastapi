from sqlmodel import select
from fastapi import HTTPException, status, Query
from domain.models import Customer, CustomerCreate, CustomerPlan, CustomerUpdate, EnumState, Plan
from infrastructure.db import SessionDep


def create_customer_service(customer_data: CustomerCreate, session: SessionDep) -> Customer:
    existing_customer = session.exec(select(Customer).where(Customer.email == customer_data.email)).first()
    if existing_customer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


def get_customer_service(customer_id: int, session: SessionDep) -> Customer:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    return customer


def delete_customer_service(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    session.delete(customer)
    session.commit()
    return {"detail": "ok"}


def update_customer_service(customer_id: int, customer_data: CustomerUpdate, session: SessionDep) -> Customer:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    customer_dict = customer_data.model_dump(exclude_unset=True)
    customer.sqlmodel_update(customer_dict)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


def get_all_customers_service(session: SessionDep) -> list[Customer]:
    return session.exec(select(Customer)).all()


def suscribe_to_plan_service(customer_id: int, plan_id: int, session: SessionDep, state: EnumState = Query()) -> CustomerPlan:
    customer = session.get(Customer, customer_id)
    plan = session.get(Plan, plan_id)
    if not customer or not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer or Plan doesn't exist")
    
    customer_plan = CustomerPlan(customer_id=customer.id, plan_id=plan.id, state=state)
    session.add(customer_plan)
    session.commit()
    session.refresh(customer_plan)
    return customer_plan


def get_customer_plans_service(customer_id: int, session: SessionDep) -> list[Plan]:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    return customer.plans


