import pandas as pd 
data ={
    'name': ['ramin' , 'amirreza' , 'mahta' , 'maryam'] ,
    'grade': [12,8,20,10]
}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())
passed = df[df['grade']>10]
print(passed)

