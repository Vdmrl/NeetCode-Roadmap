# SELECT Customers.name as Customers FROM Customers WHERE (Customers.id NOT IN (SELECT Orders.customerId FROM Orders));
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders["customerId"])][["name"]].rename(columns={"name": "Customers"})