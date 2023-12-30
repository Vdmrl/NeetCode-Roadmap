#SELECT employee_id,
#    CASE
#        WHEN (employee_id % 2 = 1 AND name NOT LIKE 'M%') THEN salary
#        ELSE 0
#    END AS bonus
#    FROM Employees
#    ORDER BY employee_id;

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[(employees["employee_id"] % 2 == 0) | (employees["name"].str.startswith("M")), "salary"] = 0
    return employees[["employee_id", "salary"]].rename(columns={"salary": "bonus"}).sort_values(by="employee_id")