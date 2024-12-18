from fastapi import FastAPI
from db import create_all_Tables
from .routers import customers, transactions, invoices

app = FastAPI(lifespan=create_all_Tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)


@app.get("/")
async def root():
    return {"message": "Hola mundo"}