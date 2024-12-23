from infrastructure.repositories.plan_repository import PlanRepository
from domain.models import EnumState, Plan, PlanCreate
from domain.dto import Response


def create_plan_service(plan_data: PlanCreate, session: PlanRepository) -> Response:
    repository = PlanRepository(session)
    plan = repository.create_plans_repository(plan_data.model_dump())
    return Response(success=True, message="Plan created", data=plan)
    

def get_plans_service(session: PlanRepository) -> Response:
    repository = PlanRepository(session)
    plans = repository.get_plans_repository()
    if not plans:
        return Response(success=False, message="No plans found", data=None)
    
    return Response(success=True, message="Plans retrieved", data=plans)


def get_plan_service(plan_id: int, session: PlanRepository) -> Response:
    repository = PlanRepository(session)
    plan = repository.get_plan_repository(plan_id)
    if not plan:
        return Response(success=False, message="Plan not found", data=None)
    
    return Response(success=True, message="Plan retrieved", data=plan)


def get_state_plans_service(session: PlanRepository, state: EnumState) -> Response:
    repository = PlanRepository(session)
    plans = repository.get_state_plans_repository(state)
    if not plans: 
        return Response(success=False, message="No plans found", data=None)
    
    return Response(success=True, message="Plans retrieved", data=plans)
    