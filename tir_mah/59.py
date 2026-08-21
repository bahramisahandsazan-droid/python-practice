from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

model = DecisionTreeClassifier()

scores = cross_val_score(model, X, y, cv=5)   # cv=5 یعنی 5-Fold

print('Scores for each fold:', scores)
print('Average accuracy:', scores.mean())