from domain.interfaces.repositories.Iplan_repository import IPlanRepository
from domain.models import EnumState, Plan, PlanCreate
from domain.dto import Response
from domain.interfaces.services.Iplan_service import IPlanService


class PlanService(IPlanService):

    def __init__(self, repository: IPlanRepository):
        self.repository = repository

    def create_plan_service(self, plan_data: PlanCreate) -> Response:
        plan = self.repository.create_plans_repository(plan_data.model_dump())
        return Response(success=True, message="Plan created", data=plan)
    

    def get_plans_service(self) -> Response:
        plans = self.repository.get_plans_repository()
        if not plans:
            return Response(success=False, message="No plans found", data=None)
        
        return Response(success=True, message="Plans retrieved", data=plans)


    def get_plan_service(self, plan_id: int) -> Response:
        plan = self.repository.get_plan_repository(plan_id)
        if not plan:
            return Response(success=False, message="Plan not found", data=None)
        
        return Response(success=True, message="Plan retrieved", data=plan)


    def get_state_plans_service(self, state: EnumState) -> Response:
        plans = self.repository.get_state_plans_repository(state)
        if not plans: 
            return Response(success=False, message="No plans found", data=None)
        
        return Response(success=True, message="Plans retrieved", data=plans)
    

    def delete_plan_service(self, plan_id: int) -> Response:
        plan = self.repository.get_plan_repository(plan_id)
        if not plan:
            return Response(success=False, message="Plan not found", data=None)
        
        self.repository.delete_plan_repository(plan)
        return Response(success=True, message="Plan deleted", data=None)