from pandas._libs.reduction import apply_frame_axis0
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from numpy import cov
data=pd.read_csv('forestfires.csv')
data.select_dtypes(include=[np.number]).interpolate().dropna() #replacing the null values with the average values
data['X'].fillna(data['X'].mean(),inplace =True)
data['Y'].fillna(data['Y'].mean(),inplace =True)
data['FFMC'].fillna(data['FFMC'].mean(),inplace =True)
data['DMC'].fillna(data['DMC'].mean(),inplace =True)
data['DC'].fillna(data['DC'].mean(),inplace =True)
data['ISI'].fillna(data['ISI'].mean(),inplace =True)
data['temp'].fillna(data['temp'].mean(),inplace =True)
print(data.corr())
data = data.dropna(how='any',axis=0)
data=data.drop(columns=['month','day']) #droping the attribute which are not required
train,test=train_test_split(data,test_size=0.2)
train_label=train['wind']
train_label=train_label.astype('int')
train=train.drop(columns=['wind'])
test_label=test['wind']
test_label=test_label.astype('int')
test=test.drop(columns=['wind'])
NBclf=GaussianNB()# fitting Naive bayes classifier
NBclf.fit(train,train_label)
SVCclf=SVC(gamma='auto') #fitting Support Vector Classifier
SVCclf.fit(train,train_label)
KNNclf=KNeighborsClassifier(n_neighbors=2) #fitting K nearest neighbour classifier
KNNclf.fit(train,train_label)
nbscore= NBclf.score(test,test_label)
svcscore=SVCclf.score(test,test_label)
knnscore=KNNclf.score(test,test_label)
print("Score for Naive Bayes is: ", nbscore)
print("Score for Support Vector Classifier is: ",svcscore)
print("Score for KNN Classifier is : ",knnscore)