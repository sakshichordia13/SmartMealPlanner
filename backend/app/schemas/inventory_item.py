from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.enums import FoodCategory, StorageLocation


class InventoryItem(BaseModel):
    """
    One ingredient/item the user currently has at home.
    """
    name: str = Field(..., min_length=1, examples=["spinach"])
    quantity: float = Field(..., gt=0, examples=[1])
    unit: str = Field(..., min_length=1, examples=["bag", "count", "g", "ml"])
    location: StorageLocation
    category: FoodCategory
    expires_at: Optional[date] = Field(default=None, description="Expiry date if known")
