import os
import pickle
import numpy as np
import pandas as pd
import math
from typing import Optional, List

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

    def save_cart(self, filepath: Optional[str] = None) -> str:
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

    def load_cart(self, filepath: Optional[str] = None) -> "PickleShoppingCart":
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

            prices: List[float] = []

            # Iterate items in the cart
            for product_id, qty in self.items.items():
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


    def position_vector(self, p1, p2):
        """    
        Treat two product attribute lists (like price, rating, weight)
        as points and show how much they differ. Compares features of product A vs product B.
        """
        return [p2[i] - p1[i] for i in range(len(p1))]

    def unit_vector(self, v):
        """Return unit vector of v."""
        length = sum(x*x for x in v) ** 0.5
        if length == 0:
            return v
        return [x / length for x in v]

    def dot_product(self, v1, v2):
        """        
        Compare similarity between two product feature vectors.
        Higher dot product = more similar products.
        
        """
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    def projection(self, a, b):
        """Show how much of product A's features align with product B's features."""
        dot_ab = self.dot_product(a, b)
        dot_bb = self.dot_product(b, b)
        if dot_bb == 0:
            return [0]*len(b)
        scale = dot_ab / dot_bb
        return [scale * x for x in b]

    def angle_between(self, v1, v2):
        """
        Return how different two products are based on their features.
        Angle near 0° = very similar.
        Angle near 90° = totally different.
        """
        dot = self.dot_product(v1, v2)
        len1 = sum(x*x for x in v1) ** 0.5
        len2 = sum(x*x for x in v2) ** 0.5
        if len1 == 0 or len2 == 0:
            return 0
        cos_theta = dot / (len1 * len2)
        cos_theta = max(-1, min(1, cos_theta))
        return math.degrees(math.acos(cos_theta))

    def is_orthogonal(self, v1, v2):
    
        """Check if two products share similarity in their features."""
        return self.dot_product(v1, v2) == 0
    
    def display_vector(self, v):
        """Print the vector."""
        print("Vector:", v)

    def export_vector(self, v, filepath="data/vector.txt"):
        """Export the vector"""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w") as f:
                f.write(str(v))
            print("Exported vector to", filepath)
            return filepath
        except Exception as e:
            print("Export error:", e)
            return ""

    def obtain_unique(self, values):
        """
        Return the unique categorical values.
        """
        try:
            uniques = list(dict.fromkeys(values))
            print("Unique values:", uniques)
            return uniques
        except Exception as e:
            print("Error obtaining unique values:", e)
            return []

    def generate_permutations(self, values, r=None):
        """
        Generate permutations of categorical values.
        """
        try:
            uniques = self.obtain_unique(values)
            r = r or len(uniques)
            perms = list(itertools.permutations(uniques, r))
            print(f"Permutations (r={r}):", perms)
            return perms
        except Exception as e:
            print("Error generating permutations:", e)
            return []

    def generate_combinations(self, values, r):
        """
        Generate combinations (no order) of categorical values.
        """
        try:
            uniques = self.obtain_unique(values)
            combs = list(itertools.combinations(uniques, r))
            print(f"Combinations (r={r}):", combs)
            return combs
        except Exception as e:
            print("Error generating combinations:", e)
            return []
