from domain.models import EnumState, Plan, PlanCreate
from domain.dto import Response
from abc import ABC, abstractmethod

class IPlanService(ABC):
    
    @abstractmethod
    def create_plan_service(self, plan_data: PlanCreate) -> Response:
        pass

    @abstractmethod
    def get_plans_service(self) -> Response:
        pass

    @abstractmethod
    def get_plan_service(self, plan_id: int) -> Response:
        pass

    @abstractmethod
    def get_state_plans_service(self, state: EnumState) -> Response:
        pass

    @abstractmethod
    def delete_plan_service(self, plan_id: int) -> Response:
        pass