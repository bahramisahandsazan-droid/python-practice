from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# مدل ۱: Logistic Regression
model1 = LogisticRegression(max_iter=200)
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)
acc1 = accuracy_score(y_test, pred1)

# مدل ۲: Decision Tree
model2 = DecisionTreeClassifier()
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
acc2 = accuracy_score(y_test, pred2)

# مدل ۳: KNN (نزدیک‌ترین همسایه‌ها)
model3 = KNeighborsClassifier(n_neighbors=3)
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)
acc3 = accuracy_score(y_test, pred3)

print(f'Logistic Regression Accuracy: {acc1 * 100}%')
print(f'Decision Tree Accuracy: {acc2 * 100}%')
print(f'KNN Accuracy: {acc3 * 100}% ')