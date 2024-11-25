# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:41:10 2024

@author: Jonathan
"""
"""
Exercise 1: Using Data API - Loading and Preprocessing Data with TensorFlow

Using TensorFlow Data API, load data and perform the necessary preprocessing steps for the HYPE-Retention dataset:
  -	Loading data
  -	Converting categorical features to numerical
  -	Transformations
  -	Standardization

Note that all these tasks should be done after data cleaning.<br>
(3 marks)
"""
#!pip install ucimlrepo
#All Imports
from ucimlrepo import fetch_ucirepo

import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Normalization
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#from ucimlrepo import fetch_ucirepo
# fetch dataset
adult = fetch_ucirepo(id=2)

# data (as pandas dataframes)
#X = adult.data.features
#y = adult.data.targets

X = pd.DataFrame(adult.data.features)
Y = pd.DataFrame(adult.data.targets)

# Print the description and shapes of the dataset
print(X.shape)
print(Y.shape)

# metadata
print(adult.metadata)

# variable information
print(adult.variables)

#split into train and test data
X_train, X_val_test, y_train, y_val_test = train_test_split(X, Y, test_size=.665)

#split train data into train and validation data
X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5)

#print the shapes of the data
print(X_train.shape)
print(X_test.shape)
print(X_val.shape)

# Convert categorical features to numerical using OneHotEncoder
categorical_features = X.select_dtypes(include=['object']).columns
numerical_features = X.select_dtypes(exclude=['object']).columns

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore') # sparse=False for dense output
encoded_data = encoder.fit_transform(X[categorical_features])

# Create a new DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_features))

# Concatenate numerical and encoded features
X_encoded = pd.concat([X[numerical_features], encoded_df], axis=1)

# Convert target variable to numerical using LabelEncoder if it's categorical
if Y['income'].dtype == 'object':
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(Y['income']) # Also, transform the column
else:
    y_encoded = Y

# variable information
print(y_encoded.dtype)

#dataset = tf.data.Dataset.from_tensor_slices((X,y))
dataset = tf.data.Dataset.from_tensor_slices((X_encoded.values, y_encoded))

def showTensor(dataset):
  # Iterate and print values
  for value in dataset:
    print(value)

#showTensor(dataset)

# Aply Transformation
dataset = dataset.repeat(3)
#showTensor(dataset)

# create normalization layer
norm = Normalization(axis=None)
norm.adapt(dataset.map(lambda x, y: x))
norm(X_encoded.values)










































