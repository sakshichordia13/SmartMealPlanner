from __future__ import annotations

from app.ai.mock_claude import mock_generate_plan
from app.schemas.plan_models import PlanRequest, PlanResponse


def generate_plan_with_ai(payload: PlanRequest) -> PlanResponse:
    """
    Single AI entrypoint used by API routes.
    """
    return mock_generate_plan(payload)
