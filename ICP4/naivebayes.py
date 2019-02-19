import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
dataset = pd.read_csv('iris.csv')
X = dataset.drop(['class'], axis=1) # Here first : means fetch all rows :-1 means except last column
y = dataset.drop(['sepal length','sepal width','petal length'], axis=1)# : is fetch all rows 3 means 3rd column
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state = 2) # 0.2 test_size means 20%
print(X_train, y_train)
model = GaussianNB()
model.fit(X_train,y_train)
print(model)
expected = X_test
predicted = model.predict(y_test)
print(expected, ":", predicted)
# Matlab Plot
plt.plot(expected, predicted)
plt.show()
# Cross Validation
print(metrics.classification_report(expected, predicted))
# confusion_matrix - To evaluate Accuracy of classification
print(metrics.confusion_matrix(expected, predicted))
model.fit(X_train, y_train)
Y_predicted = model.predict(X_test)
print("Gaussian Model Accuracy is ", metrics.accuracy_score(y_test, Y_predicted) * 100)
