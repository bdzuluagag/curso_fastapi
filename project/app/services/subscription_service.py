from domain.interfaces.repositories.Iplan_repository import IPlanRepository
from domain.interfaces.repositories.Isubscription_repository import ISubscriptionRepository
from domain.interfaces.repositories.Icustomer_repository import ICustomerRepository
from domain.dto import Response
from domain.interfaces.services.Isubscription_service import ISubscriptionService


class SubscriptionService(ISubscriptionService):

    def __init__(self, repository: ISubscriptionRepository, plan_repository: IPlanRepository, customer_repository: ICustomerRepository):
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
    

    def get_customer_active_plans_service(self, customer_id: int) -> Response:
        customer = self.customer_repository.get_customer_repository(customer_id)
        if not customer:
            return Response(success=False, message="Customer doesn't exist", data=None)
        
        active_plans = self.repository.get_customer_active_plans_repository(customer_id)
        if not active_plans:
            return Response(success=False, message="Customer has no active plans", data=None)
        
        return Response(success=True, message="Active customer plans retrieved", data=active_plans)
