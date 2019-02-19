from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import accuracy_score
df=pd.read_csv('iris.csv')
#print(df)
#df.Species.replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [1, 2, 3], inplace=True)
clf = GaussianNB()
array = df.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.33
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
clf.fit(X_train, Y_train)
pred_clf = clf.predict(X_validation)
print(pred_clf)
print(metrics.accuracy_score(Y_validation,pred_clf))
