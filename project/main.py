from fastapi import FastAPI, HTTPException
from models import *
from db import SessionDep, create_all_Tables
from sqlmodel import select

app = FastAPI(lifespan=create_all_Tables)


@app.get("/")
async def root():
    return {"message": "Hola mundo"}


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer doesn't exists")
    return customer


@app.get("/customers", response_model=list[Customer])
async def getall_customer(session: SessionDep):
    return session.exec(select(Customer)).all() 


@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return transaction.id


@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return invoice.id