import pandas as pd

def save_to_csv(dataframe, filepath):
    dataframe.to_csv(filepath, index=False)

