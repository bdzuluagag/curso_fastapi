from domain.models import CustomerPlan
from sqlmodel import select
from infrastructure.db import SessionDep
from domain.interfaces.repositories.Isubscription_repository import ISubscriptionRepository


class SubscriptionRepository(ISubscriptionRepository):

    def __init__(self, session: SessionDep):
        self.session = session


    def subscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        customer_plan = self.session.exec(select(CustomerPlan).where(CustomerPlan.customer_id == customer_id, CustomerPlan.plan_id == plan_id)).first()
        print("CUSTOMER PLAN FOUND?", customer_plan)
        if not customer_plan:
            customer_plan = CustomerPlan(customer_id=customer_id, plan_id=plan_id, state="active")
            self.session.add(customer_plan)
            self.session.commit()
            self.session.refresh(customer_plan)
            return customer_plan
        else:
            customer_plan.state = "active"
            self.session.add(customer_plan)
            self.session.commit()
            self.session.refresh(customer_plan)
            return customer_plan
        

    def unsubscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        customer_plan = self.session.exec(select(CustomerPlan).where(CustomerPlan.customer_id == customer_id, CustomerPlan.plan_id == plan_id)).first()
        if customer_plan:
            customer_plan.state = "inactive"
            self.session.add(customer_plan)
            self.session.commit()
            self.session.refresh(customer_plan)
            return customer_plan
        return None
    

    def is_already_subscribed(self, customer_id: int, plan_id: int) -> bool:
        customer_plan = self.session.exec(select(CustomerPlan).where(CustomerPlan.customer_id == customer_id, CustomerPlan.plan_id == plan_id, CustomerPlan.state == "active")).first()
        print("already subscribed: ", customer_plan)
        if customer_plan:
            return True
        return False