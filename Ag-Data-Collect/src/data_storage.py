def save_to_csv(dataframe, filepath): #Convert the data extracted to a .csv file
    dataframe.to_csv(filepath, index=False)

