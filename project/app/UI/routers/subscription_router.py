from fastapi import APIRouter, Depends, HTTPException, status
from domain.models import CustomerPlan
from application.controllers.subscription_controller import SubscriptionController
from infrastructure.db import SessionDep
from infrastructure.repositories.subscription_repository import SubscriptionRepository
from infrastructure.repositories.plan_repository import PlanRepository
from infrastructure.repositories.customer_repository import CustomerRepository
from services.subscription_service import SubscriptionService

router = APIRouter(tags=["subscriptions"])

def get_subscription_controller(session: SessionDep) -> SubscriptionController:
    repository = SubscriptionRepository(session)
    plan_repository = PlanRepository(session)
    customer_repository = CustomerRepository(session)
    service = SubscriptionService(repository, plan_repository, customer_repository)
    return SubscriptionController(service)


@router.post("/customers/{customer_id}/plans/{plan_id}/subscribe")
def subscribe_to_plan_endpoint(customer_id: int, plan_id: int, controller: SubscriptionController = Depends(get_subscription_controller)):                                                                    
    return controller.subscribe_to_plan_controller(customer_id, plan_id)


@router.post("/customers/{customer_id}/plans/{plan_id}/unsubscribe")
def unsubscribe_to_plan_endpoint(customer_id: int, plan_id: int, controller: SubscriptionController = Depends(get_subscription_controller)):
    return controller.unsubscribe_to_plan_controller(customer_id, plan_id)