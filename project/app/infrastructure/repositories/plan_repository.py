from sqlmodel import Session, select

from domain.models import CustomerPlan, EnumState, Plan


class PlanRepository:

    def __init__(self, session: Session):
        self.session = session

    
    def create_plans_repository(self, plan_data: dict) -> Plan:
        plan = Plan.model_validate(plan_data)
        self.session.add(plan)
        self.session.commit()
        self.session.refresh(plan)
        return plan
    

    def get_plans_repository(self) -> list[Plan]:
        return self.session.exec(select(Plan)).all()
    

    def get_plan_repository(self, plan_id: int) -> Plan:
        return self.session.get(Plan, plan_id)
    

    def get_state_plans_repository(self, state: EnumState) -> list[CustomerPlan]:
        return self.session.exec(select(CustomerPlan).where(CustomerPlan.state == state)).all()
        