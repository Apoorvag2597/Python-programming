from sklearn import svm
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
df=pd.read_csv('iris.csv')
array = df.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.33
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
model=svm.SVC(kernel='rbf')
model.fit(X_train,Y_train.ravel())
print(model)
y_pred=model.predict(X_validation)
print(y_pred)
print(metrics.accuracy_score(Y_validation,y_pred))
