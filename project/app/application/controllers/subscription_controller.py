from fastapi import HTTPException, status
from domain.interfaces.services.Isubscription_service import ISubscriptionService


class SubscriptionController:

    def __init__(self, service: ISubscriptionService):
        self.service = service

    def subscribe_to_plan_controller(self, customer_id: int, plan_id: int):
        response = self.service.subscribe_to_plan_service(customer_id, plan_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.message

    def unsubscribe_to_plan_controller(self, customer_id: int, plan_id: int):
        response = self.service.unsubscribe_to_plan_service(customer_id, plan_id)
        return response.message