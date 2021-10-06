import pandas as pd
def detect_datetime(path_to_filename):
    df = pd.read_csv(path_to_filename)
    for column in df.columns:
        if df[column].dtype == 'object':
            try:
                df[column] = pd.to_datetime(df[column])
            except ValueError:
                print("Not a datetime compatible data-type")
    return df