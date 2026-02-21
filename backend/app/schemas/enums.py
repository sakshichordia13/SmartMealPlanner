from __future__ import annotations
from enum import Enum

class StorageLocation(str, Enum):
    fridge = "fridge"
    pantry = "pantry"
    freezer = "freezer"

class FoodCategory(str, Enum):
    produce = "produce"
    dairy = "dairy"
    meat_seafood = "meat_seafood"
    grains = "grains"
    canned = "canned"
    spices = "spices"
    frozen = "frozen"
    bakery = "bakery"
    beverages = "beverages"
    other = "other"
    
class DietType(str, Enum):
    none = "none"
    vegetarian = "vegetarian"
    vegan = "vegan"
    keto = "keto"
    halal = "halal"
    gluten_free = "gluten_free"