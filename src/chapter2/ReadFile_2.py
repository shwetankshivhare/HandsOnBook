import pandas as pd

filePath = "C:\workspace\HandsOnBook\dataset\housing\housing.csv"


def readfile(file_path = filePath):
    return pd.read_csv(file_path)


housing = readfile(filePath)
housing.head()
