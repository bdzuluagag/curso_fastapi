from fastapi import FastAPI
from models import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola mundo"}

db_customer: list[Customer] = []

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    db_customer.append(customer)
    customer.id = len(db_customer)
    return customer

@app.get("/customers/{id}", response_model=Customer)
async def get_customer(id: int):
    customer = db_customer[id - 1]
    return customer

@app.get("/customers", response_model=list[Customer])
async def getall_customer():
    return db_customer

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return transaction.id

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return invoice.id