from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
train= pd.read_csv('weatherHistory.csv')

train=train.drop(columns=['Summary','Precip Type','Daily Summary' ],axis=1)
train.select_dtypes(include=[np.number]).interpolate().dropna()
X_train,X_test = train_test_split(train,test_size=0.2)
y_train=X_train['Temperature']
#print(train1)
X_train=X_train.drop(columns=['Temperature'])
y_test=X_test['Temperature']
#print(train1)
X_test=X_test.drop(columns=['Temperature'])
#train=train.apply(LabelEncoder().fit_transform)
reg=LinearRegression().fit(X_train,y_train)
answer=reg.predict(X_test)
mean_squared_error = mean_squared_error(y_test, answer)
r2_score = r2_score(y_test,answer)
print("mean squared error is :",mean_squared_error)
print(r2_score)