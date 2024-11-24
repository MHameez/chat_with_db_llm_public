import re
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Chain:
    def __init__(self):
        pass  # No real LLM initialization

    def generate_sql(self, user_query, schema, table_name):
        # Mock SQL query generation
        return f"SELECT TOP 1 [Customer_Name], SUM([Sales]) AS [Total_Sales], [Production_Country] " \
               f"FROM [MockTable] GROUP BY [Production_Country], [Customer_Name] ORDER BY [Total_Sales] DESC;"

    def natural_response(self, sql_query, result):
        # Mock natural language explanation
        return "This query retrieves the top customer with the highest sales for each production country."