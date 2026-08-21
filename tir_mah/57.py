import pandas as pd

data = {
    'area': [50, 60, 80, 100, 120, 150, 200, 90, 70, 110],       # متراژ (متر مربع)
    'rooms': [1, 2, 2, 3, 3, 4, 5, 2, 2, 3],                       # تعداد اتاق
    'age': [10, 5, 8, 3, 15, 2, 1, 20, 12, 6],                     # سن بنا (سال)
    'price': [500, 650, 800, 1100, 1000, 1800, 2500, 700, 600, 1200]  # قیمت (میلیون تومان)
}

df = pd.DataFrame(data)
print(df)
X = df[['area', 'rooms', 'age']]   # ویژگی‌ها (چند ستون - دقت کن دو تا براکت!)
y = df['price']                     # جواب (قیمت)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
from sklearn.metrics import mean_absolute_error

predictions = model.predict(X_test)
print('Predictions:', predictions)
print('Actual:', y_test.values)

mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')
print(X_test)
print(y_test)