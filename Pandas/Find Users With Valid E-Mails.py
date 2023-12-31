# SELECT user_id, name, mail
#    FROM Users
#    Where mail ~'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].str.contains("^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$", regex=True)]
