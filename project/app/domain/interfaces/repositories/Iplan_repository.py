from abc import ABC, abstractmethod
from domain.models import CustomerPlan, EnumState, Plan

class IPlanRepository(ABC):
    
    @abstractmethod
    def create_plans_repository(self, plan_data: dict) -> Plan:
        pass

    @abstractmethod
    def get_plans_repository(self) -> list[Plan]:
        pass

    @abstractmethod
    def get_plan_repository(self, plan_id: int) -> Plan:
        pass

    @abstractmethod
    def get_state_plans_repository(self, state: EnumState) -> list[CustomerPlan]:
        pass

    @abstractmethod
    def delete_plan_repository(self, plan: Plan):
        pass