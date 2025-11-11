# Child Class 2.1: PickleShoppingCart (inherits ShoppingCart)
# Paste this into child_class2_1.py (same folder/package as parent_class2.py)
import os
import pickle
import numpy as np
import pandas as pd

from parent_class2 import ShoppingCart
from logger import log_error, log_progress


class PickleShoppingCart(ShoppingCart):
    """
    Extends ShoppingCart with:
      - save_cart / load_cart using pickle
      - calculate_statistics: mean/median/std of unit prices in the cart (quantity-weighted)

    Assumes:
      self.items is a dict {product_id: quantity}
      products_df contains columns: product_id, price (case-insensitive accepted)
    """

    def save_cart(self, filepath: str | None = None) -> str:
        """
        Save ONLY the cart items dict (self.items) to a pickle file.
        Returns the path used.
        """
        try:
            if filepath is None:
                filepath = os.path.join("data", "cart.pkl")
            os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)

            with open(filepath, "wb") as f:
                pickle.dump(self.items, f, protocol=pickle.HIGHEST_PROTOCOL)

            log_progress(f"Cart saved to {filepath}")
            return filepath
        except Exception as e:
            log_error(f"Error saving cart to {filepath}: {e}")
            raise

    def load_cart(self, filepath: str | None = None) -> "PickleShoppingCart":
        """
        Load cart items from a pickle file into self.items. Returns self.
        If file is missing, starts with an empty cart and logs a progress message.
        """
        try:
            if filepath is None:
                filepath = os.path.join("data", "cart.pkl")

            if not os.path.exists(filepath):
                log_progress(f"No file found at {filepath}. Starting with empty cart.")
                self.items = {}
                return self

            with open(filepath, "rb") as f:
                loaded = pickle.load(f)

            if not isinstance(loaded, dict):
                raise TypeError("Loaded pickle is not a dict of {product_id: quantity}.")

            self.items = loaded
            log_progress(f"Cart loaded from {filepath}")
            return self
        except Exception as e:
            log_error(f"Error loading cart from {filepath}: {e}")
            # Keep cart usable; default to empty on failure
            self.items = {}
            return self

    def calculate_statistics(self, products_df: pd.DataFrame) -> dict:
        """
        Calculate mean, median, std of unit prices of items in the cart.
        Quantity-weighted: each unit contributes one price observation.

        Returns
        -------
        dict: {"mean": float, "median": float, "std": float}
        """
        try:
            # Empty cart or no products table
            if not self.items or products_df is None or products_df.empty:
                return {"mean": 0.0, "median": 0.0, "std": 0.0}

            # Make column-name handling case-insensitive
            df = products_df.copy()
            df.columns = [c.strip().lower() for c in df.columns]

            if "product_id" not in df.columns or "price" not in df.columns:
                raise ValueError("products_df must include 'product_id' and 'price' columns.")

            prices: list[float] = []

            # Iterate items in the cart
            for product_id, qty in self.items.items():
                # sanitize qty
                try:
                    qty = int(qty)
                except Exception:
                    qty = 0
                if qty <= 0:
                    continue

                match = df.loc[df["product_id"] == product_id]
                if match.empty:
                    log_error(f"Product {product_id} not found in products_df for statistics.")
                    continue

                unit_price = float(match["price"].iloc[0])
                prices.extend([unit_price] * qty)

            if not prices:
                return {"mean": 0.0, "median": 0.0, "std": 0.0}

            arr = np.asarray(prices, dtype=float)
            mean = float(np.mean(arr))
            median = float(np.median(arr))
            # Population std (ddof=0). Use ddof=1 for sample std if required by rubric.
            std = float(np.std(arr, ddof=0))

            stats = {
                "mean": round(mean, 2),
                "median": round(median, 2),
                "std": round(std, 2),
            }
            log_progress(f"Calculated cart price stats: {stats}")
            return stats

        except Exception as e:
            log_error(f"Error calculating statistics: {e}")
            return {"mean": 0.0, "median": 0.0, "std": 0.0}
```
