#SELECT user_id,
#    (UPPER(SUBSTRING(name FOR 1)) || LOWER(SUBSTRING(name FROM 2))) as name
#    FROM Users
#    ORDER BY user_id

import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users[["user_id", "name"]].sort_values("user_id")