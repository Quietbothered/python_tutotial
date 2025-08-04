import pandas as pd
# pd.options.display.max_rows = 200
df = pd.read_csv('data.csv')

# print(df)
print(df.info())
print(pd.options.display.max_rows)
