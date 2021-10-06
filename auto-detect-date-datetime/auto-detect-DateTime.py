from pandas.api.types import is_datetime64_any_dtype as is_datetime
def detect_datetime(path_to_filename):
    df = pd.read_csv(path_to_filename)
    columns = []
    for column in df.columns:
        if is_datetime(df[column])):
            columns.append(column)
    return columns
