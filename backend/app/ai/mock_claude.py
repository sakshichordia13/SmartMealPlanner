from __future__ import annotations

from app.schemas.plan_models import PlanRequest, PlanResponse
from app.schemas.meal_models import MealOption
from app.schemas.shopping_models import ShoppingListByAisle
from app.schemas.use_first_models import UseFirstItem, UseFirstPlan

def mock_generate_plan(payload: PlanRequest) -> PlanResponse:
    """
    Mock AI (Claude-like) generator.
    """
    meal = MealOption(
        title="Quick Meal Idea (Mock AI)",
        time_minutes=5 if payload.modes.five_minute_only else 10,
        why_it_fits="Mock output to validate AI wiring.",
        ingredients_from_home=[item.name for item in payload.inventory[:2]],
        extra_ingredients=["salt", "pepper"],
        steps=["Step 1", "Step 2", "Step 3"],
        lazy_tips=["One-pan shortcut"] if payload.modes.lazy_mode else None,
    )

    shopping = ShoppingListByAisle(aisles={"Spices": ["salt", "pepper"]})

    use_first = UseFirstPlan(
        items=[
            UseFirstItem(
                name=payload.inventory[0].name if payload.inventory else "item",
                reason="Use soon to reduce waste (mock).",
                suggested_uses=["meal idea"],
            )
        ]
    )

    return PlanResponse(meals=[meal], shopping_list=shopping, use_first_plan=use_first)