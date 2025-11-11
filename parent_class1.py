#Version: v0.1
#Date Last Updated: 11-10-2025

module_name_gl = 'parent_class1'

'''
Version: v0.1
Description:
    Parent class for managing a product catalog.
    Handles loading, querying, and visualizing product data.
Authors:
    Omar, Ayomide
Date Created     : 11-10-2025
Date Last Updated: 11-10-2025
Doc:
    Implements ProductCatalog class.
Notes:
    Uses pandas and matplotlib for data processing and visualization.
'''


# custom imports
import pandas as pd
import matplotlib.pyplot as plt
from Config import config

class ProductCatalog:
    def __init__(self):
        # Initialize config and product storage
        self.config = config()
        self.products = pd.DataFrame()
    
    def query_product(self, column, value):
        # Return products matching simple condition
        if column in self.products.columns:
            return self.products[self.products[column] == value]
        else:
            print("Column not found.")
            return pd.DataFrame()
    
    def visualize_price_distribution(self):
        # Simple histogram for product prices
        if "price" in self.products.columns:
            plt.hist(self.products["price"])
            plt.title("Product Price Distribution")
            plt.xlabel(f"Price ({self.config.CURRENCY})")
            plt.ylabel("Count")
            plt.show()
        else:
            print("Error: 'price' column not found.")
