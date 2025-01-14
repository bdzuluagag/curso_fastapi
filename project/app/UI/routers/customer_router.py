from fastapi import APIRouter, Depends, status
from application.controllers.customer_controller import CustomerController
from infrastructure.repositories.customer_repository import CustomerRepository
from services.customer_service import CustomerService
from infrastructure.db import SessionDep
from domain.models import Customer, CustomerCreate, CustomerUpdate, Plan

router = APIRouter(tags=["customers"])


def get_customer_controller(session: SessionDep) -> CustomerController:
    repository = CustomerRepository(session)
    service = CustomerService(repository)
    return CustomerController(service)


@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer_endpoint(customer_data: CustomerCreate, controller: CustomerController = Depends(get_customer_controller)):
    return controller.create_customer_controller(customer_data)


@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_endpoint(customer_id: int, controller: CustomerController = Depends(get_customer_controller)):
    return controller.get_customer_controller(customer_id)


@router.get("/customers", response_model=list[Customer])
async def getall_customer_controller(controller: CustomerController = Depends(get_customer_controller)):
    return controller.getall_customer_controller()


@router.delete("/customers/{customer_id}")
async def delete_customer_endpoint(customer_id: int, controller: CustomerController = Depends(get_customer_controller)):
    return controller.delete_customer_controller(customer_id)


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer_endpoint(customer_id: int, customer_data: CustomerUpdate, controller: CustomerController = Depends(get_customer_controller)):
    return controller.update_customer_controller(customer_id, customer_data)