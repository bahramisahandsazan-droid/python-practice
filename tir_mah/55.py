from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()
x = iris.data
y = iris.target
print('feature names : ' , iris.feature_names)
print('target names : ' , iris.target_names)
print('x shape : ' , x.shape)
print('first 5 rows of x : ' , x[:150])
print('first 5 value of y : ' , y[:150])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy * 100}%')
