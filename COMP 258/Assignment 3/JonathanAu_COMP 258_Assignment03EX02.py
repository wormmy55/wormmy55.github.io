# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:42:37 2024

@author: Jonathan
"""
"""
Exercise 2: Facial Recognition for Differentiating Specific Features – Using CNNs

Using TensorFlow, design and develop a CNN model for differentiating people with mask and those without mask. 
Use the dataset of images uploaded on the Assignment 3 folder. 
Follow the steps given in the referenced article also uploaded on the Assignment 3 folder. 

Analyze the accuracy of the model and point out some of the pitfalls.

Your output should display the results of image classification in a friendly format.

(7 marks)
"""
#EX2 Imports
import os
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from google.colab import files
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Input, Normalization
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

"""
Algorithm 1: Face Mask detection

Input: Dataset including faces with and without masks
Output: Categorized image depicting the presence of face mask
FOR each image in the dataset DO
    Visualize the image in 2 categories and label them
    Convert the RGB image to Gray-scale image
    Resize the gray-scale image into 100 x 100
    Normalize the image and convert it into 4 dimensional array
END
FOR building the CNN model DO
    Add a Convolution layer of 200 filters
    Add the second Convolution layer of 100 filters
    Insert a Flatten layer to the network classifier
    Add a Dense layer of 64 neurons
    Add the final Dense layer with 2 outputs for 2 categories
END
Split the data and train the model
"""
# Loading the database
path = './Dataset'
categories = os.listdir(path)
cat0 = ("./Dataset/without_mask")
cat1 = ("./Dataset/with_mask")

# Get a list of all image file paths
image_paths = []
for cat in categories:
  category_path = os.path.join(path, cat)
  for filename in os.listdir(category_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')): # Adjust file extensions if needed
      img_path = np.array(Image.open(os.path.join(category_path, filename)))
      image_paths.append(img_path)

  # Convert the RGB image to Gray-scale image
  for i in image_paths:
    # Load the image using cv2.imread
    img = cv2.imread("image", i) 

    # Check if the image was loaded successfully
    if img is not None:
      # Convert the image to grayscale
      img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      # Resize the image to 100 x 100
      img = cv2.resize(img, (100, 100))
      # Normalize the image and convert it to 4 dimensional array
      #i = np.reshape(img(image_paths[i],100, 100, 1))
      print(f"Successfully loaded image: {i}")

    else:
      print(f"Failed to load image: {i}")




































