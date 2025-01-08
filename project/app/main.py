from dotenv import load_dotenv
from fastapi import FastAPI, Request
from infrastructure.db import create_all_Tables
from application.controllers import transactions, invoices, plans, users
from UI.routers import customer_router, subscription_router

load_dotenv()

app = FastAPI(lifespan=create_all_Tables)
app.include_router(customer_router.router)
app.include_router(subscription_router.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)
app.include_router(users.router)


"""@app.middleware("http")
async def log_request_headers(request: Request, call_next):
    print("Request Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    response = await call_next(request)
    return response"""


@app.get("/")
async def root():
    return {"message": "Holaa"}


@app.get("/hello/{name}")
async def hello(name: str):
    return f"Hello {name}"