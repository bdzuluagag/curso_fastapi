
from fastapi import APIRouter, HTTPException, Query, status
from infrastructure.db import SessionDep
from domain.models import CustomerPlan, EnumState, Plan, PlanCreate
from services.plan_service import delete_plan_service, create_plan_service, get_plans_service, get_state_plans_service, get_plan_service

router = APIRouter(tags=["plans"])


@router.post("/plans", response_model=Plan)
async def create_plans_endpoint(plan_data: PlanCreate, session: SessionDep):
    response = create_plan_service(plan_data, session)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
    return response.data


@router.get("/plans", response_model=list[Plan])
async def get_plans_endpoint(session: SessionDep):
    response = get_plans_service(session)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.get("/plan", response_model=Plan)
async def get_plan_endpoint(plan_id: int, session: SessionDep):
    response = get_plan_service(plan_id, session)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.get("/plans/state", response_model=list[CustomerPlan])
async def get_state_plans_endpoint(session: SessionDep, state: EnumState = Query()):
    response = get_state_plans_service(session, state=state)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.data


@router.delete("/plans/{plan_id}")
async def delete_plan_endpoint(plan_id: int, session: SessionDep):
    response = delete_plan_service(plan_id, session)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
    
    return response.message