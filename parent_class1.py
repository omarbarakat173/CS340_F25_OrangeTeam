#parent class 1.1 - product catalog

import pandas as pd
import matplotlib.pyplot as plt

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
        self.config = config
        self.products = pd.DataFrame()
    
    def query_product(self, column, value):
        # Return products matching simple condition
        if column in self.products.columns:
            return self.products[self.products[column] == value]
        else:
            print("Column not found.")
            return pd.DataFrame()
    
    def visualize_price_distribution(self):
        # Simple histogram or line plot for product prices
        if "price" in self.products.columns:
            plt.hist(self.products["price"])   # Make a histogram
            plt.title("Product Price Distribution")  # Title of the graph
            plt.xlabel("Price")                     # Label x axis
            plt.ylabel("Count")                     # Label y axis
            plt.show()                              # Display the graph
        else:
            print("Error")
