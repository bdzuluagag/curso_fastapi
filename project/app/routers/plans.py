from fastapi import APIRouter, Query
from sqlmodel import select
from db import SessionDep
from models import CustomerPlan, EnumState, Plan, PlanCreate

router = APIRouter(tags=["plans"])


@router.post("/plans", response_model=Plan)
async def create_plans(plan_data: PlanCreate, session: SessionDep):
    plan = Plan.model_validate(plan_data.model_dump())
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan


@router.get("/plans", response_model=list[Plan])
async def get_plans(session: SessionDep):
    return session.exec(select(Plan)).all()


@router.get("/plans/state", response_model=list[CustomerPlan])
async def get_state_plans(session: SessionDep, state: EnumState = Query()):
    plans = session.exec(select(CustomerPlan).where(CustomerPlan.state == state)).all()
    return plans
