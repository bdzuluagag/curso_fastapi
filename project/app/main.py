
from fastapi import FastAPI, Request
from infrastructure.db import create_all_Tables
from application.routers import customers, transactions, invoices, plans

app = FastAPI(lifespan=create_all_Tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)


@app.middleware("http")
async def log_request_headers(request: Request, call_next):
    print("Request Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hola mundo"}