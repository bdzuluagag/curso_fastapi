
from fastapi import APIRouter, Query
from infrastructure.db import SessionDep
from domain.models import CustomerPlan, EnumState, Plan, PlanCreate
from services.plan_service import create_plan_service, get_plans_service, get_state_plans_service

router = APIRouter(tags=["plans"])


@router.post("/plans", response_model=Plan)
async def create_plans_endpoint(plan_data: PlanCreate, session: SessionDep):
    return create_plan_service(plan_data, session)


@router.get("/plans", response_model=list[Plan])
async def get_plans_endpoint(session: SessionDep):
    return get_plans_service(session)


@router.get("/plans/state", response_model=list[CustomerPlan])
async def get_state_plans_endpoint(session: SessionDep, state: EnumState = Query()):
    return get_state_plans_service