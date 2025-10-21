# Child Class 2.1: PickleShoppingCart (inherits ShoppingCart)
class PickleShoppingCart(ShoppingCart):
    def save_cart(self, filepath=None):
        # Save cart data to a pickle file
        pass
    
    def load_cart(self, filepath=None):
        # Load cart data from a pickle file
        pass
    
    def calculate_statistics(self, products_df):
        # Calculate mean, median, std of prices in cart
        pass
