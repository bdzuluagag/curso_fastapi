from fastapi import HTTPException, status
from domain.models import CustomerCreate, CustomerUpdate
from domain.interfaces.services.Icustomer_service import ICustomerService


class CustomerController:

    def __init__(self, service: ICustomerService):
        self.service = service


    def create_customer_controller(self, customer_data: CustomerCreate):
        response = self.service.create_customer_service(customer_data)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
        
        return response.data


    def get_customer_controller(self, customer_id: int):
        response = self.service.get_customer_service(customer_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data


    def getall_customer_controller(self):
        response = self.service.get_all_customers_service()
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data
    

    def delete_customer_controller(self, customer_id: int):
        response = self.service.delete_customer_service(customer_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.message


    def update_customer_controller(self, customer_id: int, customer_data: CustomerUpdate):
        response = self.service.update_customer_service(customer_id, customer_data)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data


    def get_customer_plans_controller(self, customer_id: int):
        response = self.service.get_customer_plans_service(customer_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data
    