import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

data = {
    'area' : [50,60,80,100,120,150,200,90,70,110],
    'rooms' : [1,2,2,3,3,4,5,2,2,3],
    'age' : [10,5,8,3,5,2,1,20,12,6],
    'price' : [500,650,800,1100,1000,1800,2500,700,600,1200]
}
df = pd.DataFrame(data)

x = df[['area','rooms','age']]
y = df['price']
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state=42)

#--------بدون نرمال سازی----------
model_raw = KNeighborsRegressor ( n_neighbors=3)
model_raw.fit (x_train , y_train)
pred_raw = model_raw.predict(x_test)
mae_raw = mean_absolute_error(y_test , pred_raw)
print(f'MAE without scaling:  {mae_raw}')

#------------با نرمال سازی------------
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model_scaled = KNeighborsRegressor(n_neighbors=3)
model_scaled.fit(x_train_scaled, y_train)
pred_scaled = model_scaled.predict(x_test_scaled)
mae_scaled = mean_absolute_error(y_test, pred_scaled)
print(f'MAE with scaling: {mae_scaled}')