# This is the script I used to split the big .csv into multiple single-region .csv

import pandas as pd

df = pd.read_csv('data.csv')
data_output = []

for i in range(len(df)):
    if (df.iloc[i, 1] == "us-central"): data_output.append(df.iloc[i, 2])

df_output = pd.DataFrame(data_output, columns=['Data'])

df_output.to_csv('us_central_data.csv')
