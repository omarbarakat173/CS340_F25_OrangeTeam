# Parent Class 2: ShoppingCart
class ShoppingCart:
    def __init__(self):
        # Initialize cart storage (product IDs and quantities)
        self.items = {}
    
    def add_item(self, product_id, quantity=1):
        # Add item(s) to cart
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
    
    def remove_item(self, product_id, quantity=1):
        # Remove item(s) from cart
        if product_id in self.items:
            if quantity >= self.items[product_id]:
                del self.items[product_id]
            else:
                self.items[product_id] -= quantity
        else:
            print(f"Product {product_id} not in cart.")
    
    def calculate_total(self, products_df):
        # Calculate subtotal, tax, discount, final total
        subtotal = 0
        total_tax = 0
        total_discount = 0
        
        for product_id, qty in self.items.items():
            product_row = products_df.loc[products_df['product_id'] == product_id]
            if product_row.empty:
                continue
            
            price = float(product_row['price'].values[0])
            tax_rate = float(product_row['tax_rate'].values[0]) if 'tax_rate' in product_row.columns else 0
            discount = float(product_row['discount'].values[0]) if 'discount' in product_row.columns else 0
            
            subtotal += price * qty
            total_tax += (price * qty) * tax_rate
            total_discount += (price * qty) * discount
        
        final_total = subtotal + total_tax - total_discount
        
        return {
            "subtotal": round(subtotal, 2),
            "tax": round(total_tax, 2),
            "discount": round(total_discount, 2),
            "final_total": round(final_total, 2)
        }
    
    def export_cart_csv(self, products_df, filepath):
        # Export cart contents to CSV file
        cart_data = []
        
        for product_id, qty in self.items.items():
            product_row = products_df.loc[products_df['product_id'] == product_id]
            if product_row.empty:
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
