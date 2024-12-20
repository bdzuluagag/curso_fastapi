from fastapi import Query
from sqlmodel import select
from domain.models import EnumState, Plan, PlanCreate, CustomerPlan
from infrastructure.db import SessionDep


def create_plan_service(plan_data: PlanCreate, session: SessionDep) -> Plan:
    plan = Plan.model_validate(plan_data.model_dump())
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan


def get_plans_service(session: SessionDep) -> list[Plan]:
    return session.exec(select(Plan)).all()


def get_state_plans_service(session: SessionDep, state: EnumState = Query()) -> list[CustomerPlan]:
    return session.exec(select(CustomerPlan).where(CustomerPlan.state == state)).all()