# generate_test_data.py

import pandas as pd
import pickle
import random
import os

# Create product data
def generate_product_data(n=20):
    categories = ['Electronics', 'Clothing', 'Books', 'Toys', 'Home']
    product_names = ['Gadget', 'Shirt', 'Novel', 'Puzzle', 'Lamp']

    data = []
    for i in range(n):
        product = {
            'product_id': 101 + i,
            'name': f"{random.choice(product_names)} {i}",
            'category': random.choice(categories),
            'price': round(random.uniform(10, 100), 2),
            'stock': random.randint(5, 100)
        }
        data.append(product)

    return pd.DataFrame(data)

# Create fake shopping cart data
def generate_cart_pickle(filepath='Input/cart.pkl'):
    cart = {
        101: 2,  # Buy 2 of product 101
        105: 1,  # Buy 1 of product 105
        108: 3   # Buy 3 of product 108
    }
    with open(filepath, 'wb') as f:
        pickle.dump(cart, f)

# Ensure folders exist
os.makedirs("Input", exist_ok=True)
os.makedirs("Output", exist_ok=True)

# Generate product CSV
df = generate_product_data()
df.to_csv("Input/products.csv", index=False)

# Generate cart pickle
generate_cart_pickle()

print(" Test product data saved to 'Input/products.csv'")
print(" Test cart data saved to 'Input/cart.pkl'")
