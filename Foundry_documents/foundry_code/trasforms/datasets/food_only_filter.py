"""
food_only_filter.py

Goal:
Keep only "food-only" restaurants.
Exclude anything that looks like bar / liquor / grocery / supermarket.
"""

from _future_ import annotations
from typing import List
import pandas as pd


EXCLUDED_KEYWORDS: List[str] = [
    "bar",
    "liquor",
    "wine",
    "beer",
    "brewery",
    "cocktail",
    "supermarket",
    "grocery",
    "convenience",
    "mart",
]


def filter_food_only(restaurants: pd.DataFrame, col: str = "CUISINE_DESCRIPTION") -> pd.DataFrame:
    """
    Returns only restaurants that do NOT contain excluded keywords in the cuisine/description column.
    """
    if col not in restaurants.columns:
        raise ValueError(f"Column '{col}' not found. Available columns: {list(restaurants.columns)}")

    s = restaurants[col].fillna("").astype(str).str.lower()

    # Build a single boolean mask: keep rows where none of the excluded keywords match
    mask_keep = ~s.str.contains("|".join(map(pd.regex.escape, EXCLUDED_KEYWORDS)), regex=True)

    filtered = restaurants.loc[mask_keep].copy()
    return filtered