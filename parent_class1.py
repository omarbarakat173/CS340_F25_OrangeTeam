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
from Config import config
import pandas as pd
import matplotlib.pyplot as plt
from logger import log_error, log_progress

class ProductCatalog:
    def __init__(self, cfg=None):
        self.config = cfg if cfg else config()
        self.products = pd.DataFrame()
    
    def query_product(self, column, value):
        if column in self.products.columns:
            return self.products[self.products[column] == value]
        else:
            log_error(f"Column not found in products: {column}")
            return pd.DataFrame()
    
    def visualize_price_distribution(self):
        if "price" in self.products.columns:
            plt.hist(self.products["price"])
            plt.title(f"Product Price Distribution ({self.config.CURRENCY})")
            plt.xlabel(f"Price ({self.config.CURRENCY})")
            plt.ylabel("Count")
            plt.show()
            log_progress("Displayed product price distribution.")
        else:
            log_error("Error: 'price' column not found for visualization.")
