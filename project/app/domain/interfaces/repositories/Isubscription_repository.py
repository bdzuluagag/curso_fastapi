from abc import ABC, abstractmethod
from domain.models import CustomerPlan

class ISubscriptionRepository(ABC):

    @abstractmethod
    def subscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        pass

    @abstractmethod
    def unsubscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        pass

    @abstractmethod
    def is_already_subscribed(self, customer_id: int, plan_id: int) -> bool:
        pass