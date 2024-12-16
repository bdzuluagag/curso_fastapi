from fastapi import FastAPI
from models import CustumerModel, Transaction, Invoice

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola mundo"}


@app.post("/costumers")
async def create_costumer(costumer: CustumerModel):
    return costumer.id

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return transaction.id

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return invoice.id