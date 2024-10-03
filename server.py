import pandas as pd
from generator import Data

data = Data(rate=90, num_days=31).get_data()
data = data.groupby('Дата').mean(numeric_only=True)
data.to_csv('Data.csv')







