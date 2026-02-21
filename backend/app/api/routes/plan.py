from fastapi import APIRouter

from app.ai.service import generate_plan_with_ai
from app.schemas.plan_models import PlanRequest, PlanResponse

router = APIRouter(prefix="/plan", tags=["plan"])


@router.post("", response_model=PlanResponse)
def generate_plan(payload: PlanRequest) -> PlanResponse:
    return generate_plan_with_ai(payload)
