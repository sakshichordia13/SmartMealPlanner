from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.enums import DietType

class CookingModes(BaseModel):
    """
    Toggles that change how recipes are generated.
    """
    five_minute_only: bool = Field(default=False, description="Only ultra-fast meals (<= 5 mins)")
    lazy_mode: bool = Field(default=False, description="Minimal steps + minimal tools")

class DietaryPreferences(BaseModel):
    """
    Dietary constraints and taste preferences.
    """
    diet_type: DietType = Field(default=DietType.none)
    allergies: list[str] = Field(default_factory=list, description="e.g., peanuts, shellfish")
    dislikes: list[str] = Field(default_factory=list, description="e.g., mushrooms, olives")
    preferred_cuisines: list[str] = Field(default_factory=list, description="e.g., indian, italian")

    max_cook_time_minutes: int = Field(default=20, ge=5, le=120)
    servings: Optional[int] = Field(default=1, ge=1, le=10)