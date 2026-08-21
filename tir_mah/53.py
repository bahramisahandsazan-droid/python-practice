from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
x = np.array([[1] , [2] , [3] , [4] ,[5] , [6] , [7] , [8] , [9] , [10]])
y = np.array([0,0,0,0,0,1,1,1,1,1])
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42 )
print('x_train: ' ,x_train)
print('x_test : ' , x_test)
print('y_train : ' , y_train)
print('y_test : ' , y_test)
model = LogisticRegression()
model.fit(x_train,y_train)
prediction = model.predict(x_test)
print('prediction : ', prediction)
print('actual : ', y_test)
accuracy = accuracy_score(y_test, prediction)
print(f'Accuracy: {accuracy * 100}%')
