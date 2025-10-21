#parent class 1.1 - product catalog
class Config:
    TAX_RATE = 0.08
    DISCOUNT_RATE = 0.10
    CURRENCY = "USD"
    PRODUCT_CSV_PATH = "Input/products.csv"
    CART_PICKLE_PATH = "Input/cart.pkl"
    OUTPUT_FOLDER = "Output/"


class ProductCatalog:
    def __init__(self, config):
        # Initialize config and product storage
        pass
    
    def query_product(self, column, value):
        # Return products matching simple condition
        pass
    
    def visualize_price_distribution(self):
        # Simple histogram or line plot for product prices
        pass
