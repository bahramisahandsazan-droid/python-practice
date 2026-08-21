import pandas as pd 
data ={
    'name': ['ramin' , 'amirreza' , 'mahta' , 'maryam'] ,
    'grade': [12,8,20,10]
}
df = pd.DataFrame(data)
df['status'] = df['grade'].apply(lambda x : 'passed' if x>=10 else 'fail')
print(df)
