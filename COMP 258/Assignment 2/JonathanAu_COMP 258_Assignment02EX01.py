# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:01:42 2024

@author: Jonathan
"""
"""
Write a Python program to classify the different species of the iris flower. 
The iris dataset is provided on eCentennial. 
You will implement the backpropagation algorithm in a similar way to the code from BackPropEx1 example. 
Use the following net architecture:
    
Your output should display the results of classification for the test examples in a friendly format.
"""
#Imports
import json
import numpy as np
import pandas as pd

#retrieve Iris.csv data
data = pd.read_csv('./CSVs/iris.csv', header=None)
D = data[4]
D = D.replace('Iris-setosa', .33)
D = D.replace('Iris-versicolor', .66)
D = D.replace('Iris-virginica', 1)
D = D.astype('float')

with open('./Json Files/test.json') as f:
    d_test = json.load(f)
    #print(d_test)

with open('./Json Files/training.json') as f:
    d_train = json.load(f)
    #print(d_train)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(data.iloc[:, 0:4])
data.iloc[:, 0:4] = imputer.transform(data.iloc[:, 0:4])
X = data.iloc[:, 0:4].values

#data = data.drop([4], axis=1)
#X = np.array([data[0] , data[1] , data[2] , data[3]])
#X = np.array(data[[0,1,2,3]])

#4-5-3 NN
sigmoid = lambda x: 1/(1 + np.exp(-x))

def backprop(W1, W2, X, D):
    alpha = 0.9
    N = X.shape[0]
    for k in range(0,N):
        x = X[k, :].T
        #x = X[:, k].T
        #print("x=", X)
        d = D.iloc[k]

        #Front Prop step
        #Calculate weighted sum of hidden node
        v1 = np.dot(W1, x)
        #pass weighted sum through activation function to give output from hidden layer
        y1 = sigmoid(v1)
        #calculate weighted sum of output layer
        v = np.dot(W2, y1)
        #pass through activation function to give third layer output
        y = sigmoid(v)
        #calculate the error - diff between correct and computed output
        e = d - y
        #Calculate delta, derivative of activation function times error
        delta = y*(1-y)*e

        #Back Prop Step
        #propagate output node delta, sigma, backward, and calculate deltas of hidden layer
        e1 = np.dot(W2.T, delta)
        #Element Mulltiplication
        delta1 = y1*(1-y1)*e1

        ##Adjusting the weight according to learning rule
        #Input Layer Row Vector
        x.shape = (1,4)
        #Hidden Layer Column Vector
        delta1.shape = (5,1)
        dW1 = alpha*np.dot(delta1, x)
        W1 = W1 + dW1

        #Output Layer Row Vector
        y1.shape = (1, 5)
        dW2 = alpha*np.dot(delta, y1)
        W2 = W2 + dW2;
    return W1, W2

# Init weights between Hidden and Input layer
W1 = 2*np.random.rand(5, 4) - 1;
# Init weights between Output and Hidden layer
W2 = 2*np.random.rand(1, 5) - 1;

#Run backprop to compute
for epoch in range(1,10000):
    W1, W2 = backprop(W1, W2, X, D)

N=X.shape[0]
for k in range(0,N):
    x = X[k, :].T

    d = D.iloc[k]

    v1 = np.dot(W1, x)

    y1 = sigmoid(v1)

    v = np.dot(W2, y1)

    y = sigmoid(v)

    if y < 0.5:
        y = "Iris-setosa"
    elif y > 0.5 and y < .8:
        y = "Iris-versicolor"
    else:
        y = "Iris-virginica"

    print(k, " y = ", y)













