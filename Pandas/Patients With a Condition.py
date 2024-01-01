# SELECT *
#    FROM Patients
#    WHERE conditions ~'(^|\s)DIAB1.*';

import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains("(^|\s)DIAB1.*", regex = True)]