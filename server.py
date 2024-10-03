import pandas as pd
from pandas.io.excel import ExcelWriter, ExcelFile
import os
import stat

data = pd.read_csv('Data.csv')

os.chmod('exdata.xlsx', mode=stat.S_IXUSR|stat.S_IRUSR|stat.S_IWUSR)
# with ExcelFile('exdata.xlsx') as writer:
#     data.to_excel(writer, index=False)
# print(data)

with open('exdata.xlsx', 'r+') as fh:
    fh.seek(0)                            # seek the to beginning
    fh.write(data)                        # write out new contents
    fh.truncate()



