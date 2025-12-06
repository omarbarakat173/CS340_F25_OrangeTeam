import pandas as pd
import seaborn as sns
from Config import config
from logger import log_progress, log_error
from parent_class1 import ProductCatalog
import matplotlib.pyplot as plt

class CSVProductCatalog(ProductCatalog):
    def __init__(self, cfg=None):
        super().__init__(cfg if cfg else config())
        self.config = cfg if cfg else config()
        
    def load_products(self, *filepath):
        try:
            final_path = filepath[0] if filepath else self.config.PRODUCT_CSV_PATH
            self.products = pd.read_csv(final_path)
            log_progress(f"Loaded products from {final_path}")
        except FileNotFoundError:
            log_error(f"CSV file not found: {final_path}")
        except Exception as e:
            log_error(f"Error loading CSV file: {e}")

    def visualize_advanced(self):
        try:
            if self.products.empty:
                log_error("No products loaded for advanced visualization.")
                return

            numeric_cols = self.products.select_dtypes(include='number').columns

            if len(numeric_cols) == 0:
                log_error("No numeric columns available for visualization.")
                return

            plt.figure(figsize=(12, 8))
            sns.violinplot(data=self.products[numeric_cols])
            plt.title("Violin Plot of Product Data")
            plt.tight_layout()
            plt.savefig(f"{self.config.OUTPUT_FOLDER}/violin_plot.png")
            plt.close()
            log_progress("Saved violin plot to Output folder.")

            plt.figure(figsize=(12, 8))
            sns.boxplot(data=self.products[numeric_cols])
            plt.title("Box Plot of Product Data")
            plt.tight_layout()
            plt.savefig(f"{self.config.OUTPUT_FOLDER}/box_plot.png")
            plt.close()
            log_progress("Saved box plot to Output folder.")

            if len(numeric_cols) >= 2:
                plt.figure(figsize=(8, 6))
                sns.scatterplot(
                    data=self.products,
                    x=numeric_cols[0],
                    y=numeric_cols[1]
                )
                plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
                plt.tight_layout()
                plt.savefig(f"{self.config.OUTPUT_FOLDER}/scatter_plot.png")
                plt.close()
                log_progress("Saved scatter plot to Output folder.")
            else:
                log_error("Not enough numeric columns for scatter plot.")

        except Exception as e:
            log_error(f"Error during advanced visualization: {e}")

    def query_products_multi(self, **kwargs):
        try:
            if self.products.empty:
                log_error("No products loaded for querying.")
                return pd.DataFrame()

            condition = pd.Series(True, index=self.products.index)

            for column, value in kwargs.items():
                if column not in self.products.columns:
                    log_error(f"Invalid column for query: {column}")
                    return pd.DataFrame()
                if isinstance(value, (list, tuple, set)):
                    condition &= self.products[column].isin(value)
                else:
                    condition &= self.products[column] == value

            results = self.products[condition]
            log_progress(f"Multi-condition query executed with {len(results)} results.")
            return results

        except Exception as e:
            log_error(f"Error in query_products_multi: {e}")
            return pd.DataFrame()

