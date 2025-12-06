# Parent Class 2: ShoppingCart
from logger import log_error, log_progress
import pandas as pd


subtotal = 0 

class ShoppingCart:
    def __init__(self):
        self._items = {}
    
    def add_item(self, product_id, quantity=1):
        def inner():
            nonlocal quantity
            quantity = quantity
        inner()
        try:
            if product_id in self._items:
                    self._items[product_id] += quantity
            else:
                self._items[product_id] = quantity
            log_progress(f"Added {quantity} of {product_id} to cart.")
        except Exception as e:
            log_error(f"Error adding item {product_id}: {e}")
    
    def remove_item(self, product_id, quantity=1):
        try:
            if product_id in self._items:
                if quantity >= self._items[product_id]:
                    del self._items[product_id]
                    log_progress(f"Removed all of {product_id} from cart.")
                else:
                    self._items[product_id] -= quantity
                    log_progress(f"Removed {quantity} of {product_id} from cart.")
            else:
                log_error(f"Product {product_id} not in cart.")
        except Exception as e:
            log_error(f"Error removing item {product_id}: {e}")
    
    def calculate_total(self, products_df):
        global subtotal
        total_tax = 0
        total_discount = 0
        line_total = lambda price, qty: price * qty

        try:
            for product_id, qty in self._items.items():
                product_row = products_df.loc[products_df['product_id'] == product_id]
                if product_row.empty:
                    log_error(f"Product {product_id} not found in products dataframe.")
                    continue
                price = float(product_row['price'].values[0])
                tax_rate = float(product_row['tax_rate'].values[0]) if 'tax_rate' in product_row.columns else 0
                discount = float(product_row['discount'].values[0]) if 'discount' in product_row.columns else 0
                base_amount = line_total(price, qty)

                tax_expr = f"{base_amount} * {tax_rate}"
                discount_expr = f"{base_amount} * {discount}"

                item_tax = eval(tax_expr)
                item_discount = eval(discount_expr)

                subtotal += base_amount
                total_tax += item_tax
                total_discount += item_discount
                final_total = subtotal + total_tax - total_discount
                log_progress(f"Calculated cart total: {final_total}")
            return {
                "subtotal": round(subtotal, 2),
                "tax": round(total_tax, 2),
                "discount": round(total_discount, 2),
                "final_total": round(final_total, 2)
            }
        except Exception as e:
            log_error(f"Error calculating totals: {e}")
            return {}
    
    def export_cart_csv(self, products_df, filepath):
        try:
            cart_data = []
            for product_id, qty in self._items.items():
                product_row = products_df.loc[products_df['product_id'] == product_id]
                if product_row.empty:
                    log_error(f"Product {product_id} not found for export.")
                    continue
                name = product_row['name'].values[0] if 'name' in product_row.columns else product_id
                price = float(product_row['price'].values[0])
                total_price = price * qty
                cart_data.append({
                    "product_id": product_id,
                    "name": name,
                    "quantity": qty,
                    "unit_price": round(price, 2),
                    "total_price": round(total_price, 2)
                })
            df = pd.DataFrame(cart_data)
            df.to_csv(filepath, index=False)
            log_progress(f"Exported cart to CSV: {filepath}")
        except Exception as e:
            log_error(f"Error exporting cart to CSV: {e}")
