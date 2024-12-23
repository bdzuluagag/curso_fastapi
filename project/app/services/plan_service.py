from fastapi import Response
from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import EnumState, Plan, PlanCreate


def create_plan_service(plan_data: PlanCreate, session: PlanRepository) -> Response:
    repository = PlanRepository(session)
    plan = repository.create_plans_repository(plan_data.model_dump(), repository)
    return Response(success=True, message="Plan created", data=plan)
    

def get_plans_service(session: PlanRepository) -> Response:
    repository = PlanRepository(session)
    plans = repository.get_plans_repository()
    if not plans:
        return Response(success=False, message="No plans found", data=None)
    
    return Response(success=True, message="Plans retrieved", data=plans)


def get_state_plans_service(session: PlanRepository, state: EnumState) -> Response:
    repository = PlanRepository(session)
    plans = repository.get_state_plans_repository(state)
    if not plans: 
        return Response(success=False, message="No plans found", data=None)
    
    return Response(success=True, message="Plans retrieved", data=plans)
    