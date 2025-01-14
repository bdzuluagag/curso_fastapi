
from fastapi import APIRouter, HTTPException, Query, status, Depends
from infrastructure.db import SessionDep
from domain.models import CustomerPlan, EnumState, Plan, PlanCreate
from application.controllers.plan_controller import PlanController
from infrastructure.repositories.plan_repository import PlanRepository
from services.plan_service import PlanService

router = APIRouter(tags=["plans"])


def get_plan_controller(session: SessionDep) -> PlanController:
    repository = PlanRepository(session)
    service = PlanService(repository)
    return PlanController(service)


@router.post("/plans", response_model=Plan)
async def create_plans_endpoint(plan_data: PlanCreate, controller: PlanController = Depends(get_plan_controller)):
    return controller.create_plans_endpoint(plan_data)


@router.get("/plans", response_model=list[Plan])
async def get_plans_endpoint(controller: PlanController = Depends(get_plan_controller)):
    return controller.get_plans_endpoint()


@router.get("/plan", response_model=Plan)
async def get_plan_endpoint(plan_id: int, controller: PlanController = Depends(get_plan_controller)):
    return controller.get_plan_endpoint(plan_id)


@router.get("/plans/state", response_model=list[CustomerPlan])
async def get_state_plans_endpoint(state: EnumState = Query(), controller: PlanController = Depends(get_plan_controller)):
    return controller.get_state_plans_endpoint(state)


@router.delete("/plans/{plan_id}")
async def delete_plan_endpoint(plan_id: int, controller: PlanController = Depends(get_plan_controller)):
    return controller.delete_plan_endpoint(plan_id)