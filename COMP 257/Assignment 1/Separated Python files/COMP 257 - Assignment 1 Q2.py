# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:23:09 2024

@author: Jonathan
"""

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.decomposition import KernelPCA
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

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

# Generate Swiss roll dataset
swiss_x, swiss_y = datasets.make_swiss_roll(n_samples=1500, random_state=0)

#Plot swiss roll dataset
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(swiss_x[:, 0], swiss_x[:, 1], swiss_x[:, 2], c=swiss_y, s=50, alpha=0.8)
ax.set_title("Swiss Roll in Ambient Space")
ax.view_init(azim=-66, elev=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)

# Use and plot kernel PCA
pca_loop = ['linear', 'rbf', 'sigmoid']
for i in pca_loop:
  if i == 'sigmoid':
    kernel_pca = KernelPCA(n_components=2, kernel=i, gamma=0.0020, coef0=0.01)
  elif i == 'rbf':
    kernel_pca = KernelPCA(n_components=2, kernel=i, gamma=0.04)
  else:
    kernel_pca = KernelPCA(n_components=2, kernel=i, gamma=1)
    
  X_test_kernel_pca = kernel_pca.fit_transform(swiss_x)
  fig, (kernel_pca_proj_ax) = plt.subplots()
    
  kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=swiss_y)
  kernel_pca_proj_ax.set_ylabel("Z 1")
  kernel_pca_proj_ax.set_xlabel("Z 2")
  _ = kernel_pca_proj_ax.set_title(f"Projection of testing data\n using KernelPCA {i}")

#Applying Logistic Regression
clf = Pipeline([
    ("kpca", KernelPCA(n_components=2)),
    ("log_reg", LogisticRegression())
])

#Setting parameters for gridSearchCV
param_grid = [{
    "kpca__gamma": np.linspace(0.03, 0.05, 10),
    "kpca__kernel": [ "rbf", "sigmoid"]
}]

#Required since using swiss_y in gridsearch.fit() caused an error
swiss_y_discrete = np.where(swiss_y < 10, 0, 1)

#Loading GridSearchCV
grid_search = GridSearchCV(clf, param_grid, cv=3)
grid_search.fit(swiss_x, swiss_y_discrete)
#Printing Grid Search
print(grid_search.best_params_)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  