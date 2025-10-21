# Parent Class 2: ShoppingCart
class ShoppingCart:
    def __init__(self, config):
        # Initialize config and cart storage (product IDs and quantities)
        pass
    
    def add_item(self, product_id, quantity=1):
        # Add item(s) to cart
        pass
    
    def remove_item(self, product_id, quantity=1):
        # Remove item(s) from cart
        pass
    
    def calculate_total(self, products_df):
        # Calculate subtotal, tax, discount, final total
        pass
    
    def export_cart_csv(self, products_df, filepath):
        # Export cart contents to CSV file
        pass
