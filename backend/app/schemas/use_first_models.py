from __future__ import annotations

from pydantic import BaseModel, Field


class UseFirstItem(BaseModel):
    """
    Item the user should prioritize using soon (to reduce waste).
    """
    name: str
    reason: str
    suggested_uses: list[str] = Field(default_factory=list)


class UseFirstPlan(BaseModel):
    """
    Ordered list of items to use first.
    """
    items: list[UseFirstItem] = Field(default_factory=list)
