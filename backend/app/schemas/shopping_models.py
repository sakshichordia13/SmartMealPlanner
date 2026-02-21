from __future__ import annotations

from pydantic import BaseModel, Field


class ShoppingListByAisle(BaseModel):
    """
    Shopping list grouped by aisle/category for easy grocery runs.
    Example:
      {"Produce": ["berries", "lettuce"], "Dairy": ["milk"]}
    """
    aisles: dict[str, list[str]] = Field(default_factory=dict)
