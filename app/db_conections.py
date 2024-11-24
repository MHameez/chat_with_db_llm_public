import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

DATAWAREHOUSE_SERVER = os.getenv("DATAWAREHOUSE_SERVER")


class DataWarehouse:
    def __init__(self):
        pass  # No real database connection

    def get_table_schema(self, table_name):
        # Mock schema
        return {
            "Customer_Name": "VARCHAR",
            "Sales": "FLOAT",
            "Production_Country": "VARCHAR"
        }

    def execute_query(self, query):
        # Mock query execution results
        return {
            "columns": ["Customer_Name", "Total_Sales", "Production_Country"],
            "rows": [
                ["John Doe", 1200000, "USA"],
                ["Jane Smith", 950000, "UK"]
            ]
        }
