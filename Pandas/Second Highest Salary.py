# SELECT MAX(salary) AS SecondHighestSalary FROM Employee
# 	    WHERE salary <> (SELECT MAX(salary) FROM Employee);

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary").sort_values(by="salary", ascending=False)
    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return employee.iloc[[1]][["salary"]].rename(columns={"salary": "SecondHighestSalary"})