# Child Class 1.1: PickleShoppingCart (inherits ShoppingCart)
class PickleShoppingCart(ShoppingCart):
    def save_cart(self, filepath=None):
        if filepath is None:
            filepath = "cart.pkl"
        with open(filepath, 'wb') as f:
            pickle.dump(self.items, f)
            print(f"Cart saved to {filepath}")
        pass
    
    def load_cart(self, filepath=None):
         if filepath is None:
            filepath = "cart.pkl"
        try:
            with open(filepath, 'rb') as f:
                self.items = pickle.load(f)
            print(f"Cart loaded from {filepath}")
        except FileNotFoundError:
            print(f"No file found at {filepath}". Starting with empty cart.")
                  self.items = {}
        pass
    
    def calculate_statistics(self, products_df):
        prices = []
       for product_id, quantity in self.items.items()
       product_row = products_df.loc[products_df['products_id']==product_id]
       if product_row.empty:
        continue
        price = float(product_row['price'].values[0])
            prices.extend([price]*quantity)
            if not prices:
            return{"mean":0,"median":0,"std":0}
        stats = {
            "mean": round(np.mean(prices),2)
            "median": round(np.median(prices),2)
            "std": round(np.std(prices),2)
        }
        return stats
        pass
