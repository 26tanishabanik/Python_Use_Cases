import pandas as pd
import numpy as np

def detect_datetime(path_to_filename):
    df = pd.read_csv(path_to_filename)
    date_columns = []
    datetime_columns = []
    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):
            print(column + ' is not a datefield')

        try:
            dt = pd.to_datetime(df[column])
            if (dt.dt.floor('d') == dt).all():
                print(column + ' is a pure date field')
                date_columns.append(column)
            elif df[column].str.contains(r"^\d{1,2}:\d{2}:\d{2}$").all():
                print(column + ' is a pure time field')
            else:
                print(column + ' is a Datetime field')
                datetime_columns.append(column)
        except BaseException:
            print(column + ' is not a datefield')
    print("Dates: ", date_columns)
    print("DateTime: ", datetime_columns)


detect_datetime('datetime.csv')

