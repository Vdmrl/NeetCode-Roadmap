#CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
#BEGIN
#    IF N > 0 THEN
#        RETURN QUERY (SELECT DISTINCT Employee.salary FROM Employee ORDER BY Employee.salary DESC OFFSET N-1 LIMIT 1);
#    ELSE
#        RETURN QUERY (SELECT NULL::INT);
#    END IF;
#END;
#$$ LANGUAGE plpgsql;

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary")
    if N > 0 and N <= len(employee):
        return employee.sort_values(by="salary", ascending=False).iloc[[N - 1]][["salary"]].rename(columns={"salary": f'getNthHighestSalary({N})'})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
