# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:08:46 2024

@author: Jonathan
"""
"""
Write a Python program to train CIFAR10 dataset (http://www.cs.toronto.edu/~kriz/cifar.html) using Backpropagation. 
Use TensorFlow.

You will design an MLP network and train the network using backpropagation. 
Make the necessary adjustments to the net architecture to achieve a high accuracy. 
Build an image classifier using the sequential API. Compile, train, and evaluate the model. 
Use the model to make predictions.

    a)	Try different network architectures. What network architecture produces the best result?
        •	Fine-Tune Neural Network Hyperparameters 
            (number of hidden layers, number of neurons per hidden layer, activation functions),
    b)	Try different learning algorithms. Which one worked better?
    c)	Try different parameters of the learning algorithms. 
        Which ones produced the best results? 
        •	Fine-Tune learning rate, batch size, etc.

Your output should display the results of image classification in a friendly format. (6 marks)
"""

import pickle
import numpy as np
import pandas as pd

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
path = "./cifar-10-batches-py/"

# Sigmoid activation function z = f(x)
def sigmoid(z):
    """Applies the sigmoid activation function."""
    return 1 / (1 + np.exp(-z))

# Derivative of the sigmoid function; considering y = f(x)
def sigmoid_derivative(y):
    """Calculates the derivative of the sigmoid function."""
    return y * (1 - y)

data = unpickle(path + "batches.meta")
data_batch1 = unpickle(path + "data_batch_1")
data_batch2 = unpickle(path + "data_batch_2")
data_batch3 = unpickle(path + "data_batch_3")
data_batch4 = unpickle(path + "data_batch_4")
data_batch5 = unpickle(path + "data_batch_5")
data_test_batch = unpickle(path + "test_batch")
x_test_data = list(data_test_batch[b'data'])
y_test_data = data_test_batch[b'labels']
#x_test_list = pd.data_test_batch()
#print(data_test_batch)

# Forward Propagation function
def forward_propagation(inputs, weights_input_hidden, weights_hidden_output):
    """
    Performs forward propagation through the network.

    Args:
    - inputs: The input data (batch of samples).
    - weights_input_hidden: Weights from input to hidden layer.
    - weights_hidden_output: Weights from hidden to output layer.

    Returns:
    - hidden_layer_output: The activated output of the hidden layer.
    - final_output: The final activated output of the network.
    """
    # Step 1: Calculate input to hidden layer
    hidden_layer_input = np.dot(inputs, weights_input_hidden)  # Linear transformation (dot product)
    hidden_layer_output = sigmoid(hidden_layer_input)          # Apply activation function (sigmoid)

    # Step 2: Calculate input to final output layer
    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output)  # Linear transformation
    final_output = sigmoid(final_layer_input)                               # Apply activation function (sigmoid); y-hat

    return hidden_layer_output, final_output

# Backpropagation function
def backpropagation(inputs, hidden_layer_output, final_output, expected_output,
                    weights_input_hidden, weights_hidden_output, learning_rate):
    """
    Performs backpropagation and updates the weights.

    Args:
    - inputs: The input data (batch of samples).
    - hidden_layer_output: The output of the hidden layer.
    - final_output: The final output of the network.
    - expected_output: The true target values.
    - weights_input_hidden: Weights from input to hidden layer.
    - weights_hidden_output: Weights from hidden to output layer.
    - learning_rate: The learning rate for weight updates.

    Returns:
    - weights_input_hidden: Updated weights from input to hidden layer.
    - weights_hidden_output: Updated weights from hidden to output layer.
    """
    # Step 1: Calculate the error at the output layer (difference between predicted and actual output)
    output_error = expected_output - final_output

    # Step 2: Calculate the gradient (derivative) of the error at the output layer
    d_output = output_error * sigmoid_derivative(final_output)

    # Step 3: Backpropagate the error to the hidden layer (calculate hidden layer error)
    hidden_error = d_output.dot(weights_hidden_output.T)  # Error propagated back to hidden layer
    d_hidden_layer = hidden_error * sigmoid_derivative(hidden_layer_output)  # Gradient of hidden layer

    # Step 4: Update the weights using the gradients
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate

    return weights_input_hidden, weights_hidden_output

"""
# Training inputs (4 samples with 2 features) X-OR
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

# Expected outputs (XOR gate)
expected_output = np.array([[0], [1], [1], [0]])
"""

#inputs = np.array([])
#expected_output = ([])
inputs = np.array([x_test_data])
expected_output = ([y_test_data])

# Seed random numbers to make the example deterministic
np.random.seed(42)

# Initialize weights randomly for input to hidden layer and hidden layer to output
input_layer_neurons = 5
hidden_layer_neurons = 2
output_neurons = 1

# Initialize random weights (2x2 for input to hidden and 2x1 for hidden to output)
weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))

# Learning rate
learning_rate = 0.5

# Number of training iterations (epochs)
epochs = 10000

# Training process using forward propagation and backpropagation
for epoch in range(epochs):
    # Step 1: Perform forward propagation
    hidden_layer_output, final_output = forward_propagation(inputs, weights_input_hidden, weights_hidden_output)

    # Step 2: Perform backpropagation and update weights
    weights_input_hidden, weights_hidden_output = backpropagation(
        inputs, hidden_layer_output, final_output, expected_output,
        weights_input_hidden, weights_hidden_output, learning_rate
    )

# After training, print the final predicted output
print("Final output after training:")
print(final_output)

































