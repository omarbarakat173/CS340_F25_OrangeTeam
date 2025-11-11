#Version: v0.1
#Date Last Updated: 11-10-2025

#%% MODULE BEGINS
module_name_gl = 'ui'

'''
Version: v0.1
Description:
    Console-based menu and display functions for the product catalog and cart.
Authors:
    Omar
Date Created     : 11-10-2025
Date Last Updated: 11-10-2025
Notes:
    No GUI, text-based interface only.
'''

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display_menu():
    print("\n--- STORE MENU ---")
    print("1. View all products")
    print("2. Search for a product")
    print("3. Show price graph")
    print("4. View cart")
    print("5. Add product to cart")
    print("6. Checkout / calculate totals")
    print("7. Exit")

def get_user_choice():
    return input("Enter your choice (1-7): ")

def show_products(products):
    """Prints the product DataFrame"""
    if products.empty:
        print("No products found.")
    else:
        print(products.to_string(index=False))

def show_cart(items):
    """Prints items in the shopping cart"""
    if not items:
        print("Your cart is empty.")
    else:
        print("Cart contents:")
        for item in items:
            print(item['name'], "-", item['price'])
          
def get_input(prompt):
    """Asks the user for input"""
    return input(prompt)

#%% FUNCTION DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    """Test the UI menu"""
    display_menu()
    choice = get_user_choice()
    show_message(f"You chose option {choice}")

#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    print(f"\"{module_name_gl}\" module begins.")
    main()
