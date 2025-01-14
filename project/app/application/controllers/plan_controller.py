from fastapi import HTTPException, Query, status
from domain.models import EnumState, PlanCreate
from domain.interfaces.services.Iplan_service import IPlanService

class PlanController:

    def __init__(self, service: IPlanService):
        self.service = service


    def create_plans_endpoint(self, plan_data: PlanCreate):
        response = self.service.create_plan_service(plan_data)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
        
        return response.data


    def get_plans_endpoint(self):
        response = self.service.get_plans_service()
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data


    def get_plan_endpoint(self, plan_id: int):
        response = self.service.get_plan_service(plan_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data


    def get_state_plans_endpoint(self, state: EnumState = Query()):
        response = self.service.get_state_plans_service(state)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.data


    def delete_plan_endpoint(self, plan_id: int):
        response = self.service.delete_plan_service(plan_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        
        return response.message