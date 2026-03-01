"""
borough_summary.py

Goal:
Create borough-level summary after filtering food-only restaurants.
Example metrics:
- restaurant_count
- avg_score (if SCORE column exists)
"""

from _future_ import annotations
import pandas as pd


def borough_summary(food_only_restaurants: pd.DataFrame,
                    borough_col: str = "BORO",
                    score_col: str = "SCORE") -> pd.DataFrame:
    if borough_col not in food_only_restaurants.columns:
        raise ValueError(f"Column '{borough_col}' not found. Available: {list(food_only_restaurants.columns)}")

    df = food_only_restaurants.copy()

    agg_map = {"restaurant_count": (borough_col, "count")}

    if score_col in df.columns:
        # convert score to numeric safely
        df[score_col] = pd.to_numeric(df[score_col], errors="coerce")
        result = (
            df.groupby(borough_col, dropna=False)
              .agg(
                  restaurant_count=(borough_col, "count"),
                  avg_score=(score_col, "mean"),
              )
              .reset_index()
              .sort_values("restaurant_count", ascending=False)
        )
    else:
        result = (
            df.groupby(borough_col, dropna=False)
              .size()
              .reset_index(name="restaurant_count")
              .sort_values("restaurant_count", ascending=False)
        )

    return result