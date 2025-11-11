#Version: v0.1
#Date Last Updated: 11-10-2025

#%% MODULE BEGINS
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

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    # os.chdir("./../..")

# custom imports
import pandas as pd
import matplotlib.pyplot as plt

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (not used yet)

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (not used yet)

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Config:
    TAX_RATE = 0.08
    DISCOUNT_RATE = 0.10
    CURRENCY = "USD"
    PRODUCT_CSV_PATH = "Input/products.csv"
    CART_PICKLE_PATH = "Input/cart.pkl"
    OUTPUT_FOLDER = "Output/"

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (not used yet)

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        # Simple histogram for product prices
        if "price" in self.products.columns:
            plt.hist(self.products["price"])
            plt.title("Product Price Distribution")
            plt.xlabel(f"Price ({self.config.CURRENCY})")
            plt.ylabel("Count")
            plt.show()
        else:
            print("Error: 'price' column not found.")

#%% FUNCTION DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    pass

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name_gl}\" module begins.")
    main()
