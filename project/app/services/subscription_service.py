from sqlmodel import Session
from infrastructure.repositories.plan_repository import PlanRepository
from infrastructure.repositories.subscription_repository import SubscriptionRepository
from infrastructure.repositories.customer_repository import CustomerRepository
from domain.dto import Response


class SubscriptionService:

    def __init__(self, repository: SubscriptionRepository, plan_repository: PlanRepository, customer_repository: CustomerRepository):
        self.repository = repository
        self.plan_repository = plan_repository
        self.customer_repository = customer_repository


    def subscribe_to_plan_service(self, customer_id: int, plan_id: int) -> Response:
        customer = self.customer_repository.get_customer_repository(customer_id)
        plan = self.plan_repository.get_plan_repository(plan_id)
        if not customer or not plan:
            return Response(success=False, message="Customer or Plan doesn't exist", data=None)
        
        # Check if already subscribed
        if self.repository.is_already_subscribed(customer_id, plan_id):
            return Response(success=False, message="Customer already subscribed to this plan", data=None)
        
        customer_plan = self.repository.subscribe_to_plan_repository(customer.id, plan.id)
        return Response(success=True, message="Customer subscribed to plan", data=customer_plan)


    def unsubscribe_to_plan_service(self, customer_id: int, plan_id: int) -> Response:
        customer = self.customer_repository.get_customer_repository(customer_id)
        plan = self.plan_repository.get_plan_repository(plan_id)
        if not customer or not plan:
            return Response(success=False, message="Customer or Plan doesn't exist", data=None)
        
        if not self.repository.is_already_subscribed(customer_id, plan_id):
            return Response(success=False, message="Customer wasn't subscribed", data=None)
        
        customer_plan = self.repository.unsubscribe_to_plan_repository(customer.id, plan.id)
        return Response(success=True, message="Customer unsubscribed to plan", data=customer_plan)