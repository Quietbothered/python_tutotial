import pandas as pd  

df = pd.read_csv("data.csv")
# if you want to change in original dataframe use df.dropna(inframe = True)
new_df= df.dropna()
print(new_df.to_string())