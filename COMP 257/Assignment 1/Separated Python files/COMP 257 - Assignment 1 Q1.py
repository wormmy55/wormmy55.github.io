# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:08:49 2024

@author: Jonathan Au
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_openml
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning)
"""
Question 1
1. Retrieve and load the mnist_784 dataset of 70,000 instances. [5 points]

2. Display each digit. [5 points]

3. Use PCA to retrieve the 1st and 2nd principal component 
    and output their explained variance ratio. [5 points]
    
4. Plot the projections of the 1st and 2nd principal component 
    onto a 1D hyperplane. [5 points]

5. Use Incremental PCA to reduce the dimensionality of the MNIST dataset 
    down to 154 dimensions. [10 points]

6. Display the original and compressed digits from (5). [5 points]

7. Create a video discussing the code and result for each question. 
    Discuss challenges you confronted and solutions to overcoming them, 
    if applicable [15 points]
    
"""
#retrieve and load the mnist 784 dataset of 70,000 instances.
mnist = fetch_openml('mnist_784', version=1, parser='auto')
mnist.keys()
# split the data to attributes and output
X, y = mnist["data"], mnist["target"]
#Check the data shape 
X.shape
y.shape
X_train, X_test, y_train, y_test = mnist.data[:60000], mnist.data[60000:], mnist.target[:60000], mnist.target[60000:]
# Each hand writing image is a 28 by 28 pixel
#28*28
#Plot an image use the method imshow
#Display each digit
for i in range(10):
    some_digit = X.loc[i].array
    some_digit_image = some_digit.reshape(28, 28)
    plt.imshow(some_digit_image, cmap=mpl.cm.binary)
    plt.axis("off")
    plt.show()

# Create PCA instance
pca = PCA()
# Fit train data
pca.fit(X_train)

# number of Principal components
n_components = 2
pca = PCA(n_components=n_components)
pca_x = pca.fit_transform(X_train)

# Print the explained variance ratio and number of n_components
print("n_components = ", pca.n_components_)
print("Explained Variance Ratio: ", pca.explained_variance_ratio_.sum())

# Plot the projections
for i in range(10):
  plt.scatter(pca_x[y_train == str(i), 0], pca_x[y_train == str(i), 1], label = str(i))
plt.xlabel("1st Principal Component")
plt.ylabel("2nd Principal Component")
plt.legend()
plt.title("PCA Projection")
plt.show()

# Reducing demensionality
clf = make_pipeline(PCA(random_state=152), RandomForestClassifier(random_state=42))
param_distribution = {
    "pca__n_components": np.arange(154),
    "randomforestclassifier__n_estimators": np.arange(100, 500)
}
rnd_search = RandomizedSearchCV(clf, param_distribution, n_iter=10, cv = 3, random_state=2)
rnd_search.fit(X_train[:1000], y_train[:1000])
print(rnd_search.best_params_)

"""
Question 2
1. Generate Swiss roll dataset. [5 points]

2. Plot the resulting generated Swiss roll dataset. [2 points]

3. Use Kernel PCA (kPCA) with: 
    linear kernel (2 points), 
    a RBF kernel (2 points), 
    and a sigmoid kernel (2 points). [6 points]
    
4. Plot the kPCA results of applying: 
    the linear kernel (2 points), 
    a RBF kernel (2 points), 
    and a sigmoid kernel (2 points) from (3). 
    Explain and compare the results [6 points]
    
5. Using kPCA and a kernel of your choice, 
    apply Logistic Regression for classification. 
    Use GridSearchCV to find the best kernel 
    and gamma value for kPCA in order to get the best classification accuracy 
    at the end of the pipeline. 
    Print out best parameters found by GridSearchCV. [14 points]
    
6. Plot the results from using GridSearchCV in (5). [2 points]

7. Create a video discussing the code and result for each question. 
    Discuss challenges you confronted and solutions to overcoming them, 
    if applicable [15 points]
"""
"""
import time as time
import mpl_toolkits.mplot3d
from sklearn import datasets, manifold
from sklearn.decomposition import KernelPCA
from sklearn.datasets import make_swiss_roll
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import IncrementalPCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.model_selection import train_test_split

#Generate Swiss roll dataset with mnist
swiss_x, swiss_t = datasets.make_swiss_roll(X_train.shape[0], random_state=0)
#print shapes
print(swiss_x.shape)
print(swiss_t.shape)
swiss_x[:, 1] *= 0.5

#Plotting Swiss roll data with mnist
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection="3d", elev=12, azim=-66)

fig1.add_axes(ax1)
ax1.scatter(
    swiss_x[:, 0], swiss_x[:, 1], swiss_x[:, 2], c=swiss_t, s=50, alpha=0.8
)
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
plt.show()



swiss_x, swiss_y = datasets.make_swiss_roll(n_samples=1500, random_state=0)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(
    swiss_x[:, 0], swiss_x[:, 1], swiss_x[:, 2], c=swiss_y, s=50, alpha=0.8
)
ax.set_title("Swiss Roll in Ambient Space")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)

#Use and Plot KernelPCA
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

pca_loop = ['linear', 'rbf', 'sigmoid']
for i in pca_loop:
    kernel_pca = KernelPCA(
    n_components=None, kernel=i, gamma=10, fit_inverse_transform=True, alpha=0.1)
    X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
    fig, (kernel_pca_proj_ax) = plt.subplots()
    
    kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
    kernel_pca_proj_ax.set_ylabel("Principal component #1")
    kernel_pca_proj_ax.set_xlabel("Principal component #0")
    _ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA ", i)
"""

