from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

class MealOption(BaseModel):
    """
    One meal/recipe suggestion returned to the user.
    """
    title: str = Field(..., min_length=1)
    time_minutes: int = Field(..., ge=1, le=180)
    why_it_fits: str = Field(..., min_length=1)

    ingredients_from_home: list[str] = Field(default_factory=list)
    extra_ingredients: list[str] = Field(default_factory=list)

    steps: list[str] = Field(default_factory=list, description="Short step-by-step instructions")
    lazy_tips: Optional[list[str]] = Field(default=None, description="Only when lazy_mode=true")