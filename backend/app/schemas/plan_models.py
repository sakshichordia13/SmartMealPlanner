from __future__ import annotations

from pydantic import BaseModel, Field

from app.schemas.inventory_item import InventoryItem
from app.schemas.preferences_models import CookingModes, DietaryPreferences
from app.schemas.meal_models import MealOption
from app.schemas.shopping_models import ShoppingListByAisle
from app.schemas.use_first_models import UseFirstPlan


class PlanRequest(BaseModel):
    """
    Input payload for generating a meal plan.
    """
    inventory: list[InventoryItem]
    preferences: DietaryPreferences
    modes: CookingModes = Field(default_factory=CookingModes)


class PlanResponse(BaseModel):
    """
    Output returned to frontend: meals + shopping list + use-first plan.
    """
    meals: list[MealOption] = Field(..., min_length=1)
    shopping_list: ShoppingListByAisle
    use_first_plan: UseFirstPlan
