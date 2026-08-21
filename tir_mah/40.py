import pandas as pd
data = {
    'name': ['ramin','amir','mahta'],
    'age' : [51,21,11],
    'grade' : [12,18,20]
}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.shape)
print(df.describe())