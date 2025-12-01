from Config import config
from logger import log_progress, log_error
from parent_class1 import ProductCatalog
from child_class1_1 import CSVProductCatalog
from parent_class2 import ShoppingCart
from child_class2_1 import PickleShoppingCart
import os
import ui

def main():
    log_progress("Program started.")

    try:
        cfg = config()
        catalog = CSVProductCatalog(cfg)
        cart = PickleShoppingCart()
        cart.load_cart(cfg.CART_PICKLE_PATH)

        if os.path.exists(cfg.PRODUCT_CSV_PATH):
            catalog.load_products(cfg.PRODUCT_CSV_PATH)
            log_progress(f"Loaded products from {cfg.PRODUCT_CSV_PATH}")
        else:
            log_error(f"Product CSV not found: {cfg.PRODUCT_CSV_PATH}")

        while True:
            ui.display_menu()
            choice = ui.get_user_choice()

            if choice == "1":
                ui.show_products(catalog.products)
                log_progress("Viewed all products.")

            elif choice == "2":
                term = ui.get_input("Enter product name to search: ")
                results = catalog.query_product("name", term)
                ui.show_products(results)
                log_progress(f"Searched for product: {term}")

            elif choice == "3":
                catalog.visualize_price_distribution()
                log_progress("Displayed price distribution.")

            elif choice == "4":
                items = []
                for product_id, qty in cart.items.items():
                    product_row = catalog.products.loc[catalog.products['product_id'] == product_id]
                    if not product_row.empty:
                        items.append({
                            "name": product_row['name'].values[0],
                            "price": float(product_row['price'].values[0]),
                            "quantity": qty
                        })
                ui.show_cart(items)
                log_progress("Viewed cart contents.")

            elif choice == "5":
                pid = ui.get_input("Enter product ID: ")
                qty = int(ui.get_input("Enter quantity: "))
                cart.add_item(pid, qty)
                cart.save_cart(cfg.CART_PICKLE_PATH)
                log_progress(f"Added product {pid} x{qty} to cart.")

            elif choice == "6":
                totals = cart.calculate_total(catalog.products)
                print("Checkout Totals:", totals)
                log_progress(f"Checkout performed. Totals: {totals}")

            elif choice == "7":
                cart.save_cart(cfg.CART_PICKLE_PATH)
                log_progress("Exited program.")
                break

            else:
                log_error(f"Invalid menu choice: {choice}")
                print("Invalid choice. Please try again.")

    except Exception as e:
        log_error(f"Unhandled exception: {e}")
        print(f"Error: {e}")

    finally:
        log_progress("Program ended.")

if __name__ == "__main__":
    main()
