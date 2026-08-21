import pandas as pd
data ={
    'name' : ['ramin' , 'amirreza' , 'mahta' , 'maryam' , 'ali' , 'mahdi', 'alireza' ],
    'grade' : [10,16,20,8,12,15,11],
    'city' : ['tabriz', 'tehran' , 'isfahan' , 'isfahan' , 'isfahan' , 'isfahan' , 'tabriz']
}
df = pd.DataFrame(data)
grouped = df.groupby('city')['grade'].agg(['mean','count','max'])
print(grouped)

