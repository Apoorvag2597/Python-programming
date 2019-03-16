import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
dataset = pd.read_csv("Breas Cancer.csv", header=None).values
#print(dataset.head())
dataset[:,1]=np.where(dataset[:,1]=='B',0,dataset[:,1])
dataset[:,1]=np.where(dataset[:,1]=='M',1,dataset[:,1])
#print(dataset.head())


X_train, X_test, Y_train, Y_test = train_test_split(dataset[1:,2:31], dataset[1:,1],
                                                    test_size=0.25, random_state=87)

np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(30, input_dim=29, activation='tanh')) # hidden layer
my_first_nn.add(Dense(30, input_dim=29, activation='tanh')) # hidden layer
my_first_nn.add(Dense(30, input_dim=29, activation='tanh')) # hidden layer


my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print("summary: ",my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))