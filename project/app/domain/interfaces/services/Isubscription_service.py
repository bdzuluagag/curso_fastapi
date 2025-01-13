from abc import ABC, abstractmethod
from domain.dto import Response

class ISubscriptionService(ABC):

    @abstractmethod
    def subscribe_to_plan_service(self, customer_id: int, plan_id: int) -> Response:
        pass

    @abstractmethod
    def unsubscribe_to_plan_service(self, customer_id: int, plan_id: int) -> Response:
        pass