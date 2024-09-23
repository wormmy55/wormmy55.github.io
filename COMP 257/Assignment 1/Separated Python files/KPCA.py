# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 04:43:15 2024

@author: Jonathan
"""

import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA
from sklearn.datasets import fetch_openml, make_swiss_roll
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

#X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
#X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

mnist = fetch_openml('mnist_784', version=1, parser='auto')
X_train, X_test, y_train, y_test = mnist.data[:60000], mnist.data[60000:], mnist.target[:60000], mnist.target[60000:]

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)
#X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
X_test_kernel_pca = kernel_pca.fit(X_train.shape[0])
fig, (kernel_pca_proj_ax) = plt.subplots()
kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")
plt.show()

"""
#Generate swiss roll data
swiss_x, swiss_t = make_swiss_roll(X_train, noise=0.05)
print(swiss_x.shape)
print(swiss_t.shape)
swiss_x[:, 1] *= 0.5


#Computing Cluster
print("Computing unstructured heirarchical cluster...")
start_time = time.time()
clusters = AgglomerativeClustering(n_clusters=10, linkage="ward").fit(swiss_x)
elapsed_time = time.time() - start_time
label = clusters.labels_
print(f"Elapsed time: {elapsed_time:.2f}s")
print(f"Number of points: {label.size}")

#Plotting Swiss roll data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection="3d", elev=7, azim=-80)
ax1.set_position([0, 0, 0.95, 1])
for i in np.unique(label):
    ax1.scatter(
        swiss_x[label == i, 0],
        swiss_x[label == i, 1],
        swiss_x[label == i, 2],
        color = plt.cm.jet(float(i) / np.max(label + 1)),
        s=20,
        edgecolor="k",
    )
fig1.suptitle(f"Without connectivity constraints (time {elapsed_time:.2f}s")
plt.show()

#Use and Plot KernelPCA
pca_loop = ['linear', 'rbf', 'sigmoid']
for i in pca_loop:
    rbf_pca = KernelPCA(n_components=2, kernel=i, gamma=0.04)
    X_reduced = rbf_pca.fit_transform(X_train)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_train, s=10, alpha=0.8)
    ax.set_xlabel("1st Principal Component")
    ax.set_ylabel("2nd Principal Component")
    plt.show()
"""
from sklearn.decomposition import KernelPCA
from sklearn.datasets import fetch_openml, make_swiss_roll

mnist = fetch_openml('mnist_784', version=1, parser='auto')
X_train, X_test, y_train, y_test = mnist.data[:60000], mnist.data[60000:], mnist.target[:60000], mnist.target[60000:]

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)
X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = plt.subplots(
    ncols=3, figsize=(14, 4)
)
kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")