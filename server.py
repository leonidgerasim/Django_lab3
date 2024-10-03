import pandas as pd
from pandas.io.excel import ExcelWriter, ExcelFile
import os
import stat

data = pd.read_csv('Data.csv')

with ExcelWriter('exdata.xlsx') as writer:
    data.to_excel(writer, index=False)

print(data)

