import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
#given 20 customuer,
# gender 2 type(m=13,f=6),
# 3 type car(family=1,sports=2,luxury=3),
# 4 type shirt size (small=1,medium=2,large=3, extra large=4)
# total 2 class(c0=10,c1=11)
dataset = np.array([[1,13,1,1,10],[2,13,2,2,10],[3,13,2,2,10],[4,13,2,3,10],[5,13,2,4,10],
              [6,13,2,4,10],[7,6,2,1,10],[8,6,2,1,10],[9,6,2,2,10],[10,6,3,3,10],
              [11,13,1,3,11],[12,13,1,4,11],[13,13,1,2,11],[14,13,3,4,11],[15,6,3,1,11],
              [16,6,3,1,11],[17,6,3,2,11],[18,6,3,2,11],[19,6,3,2,11],[20,6,3,3,11]])

X = dataset
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
model.fit(X)
labels = model.labels_
plt.scatter(X[labels==0, 0], X[labels==0, 1], s=50, marker='o', color='red')
plt.scatter(X[labels==1, 0], X[labels==1, 1], s=50, marker='o', color='blue')
plt.scatter(X[labels==2, 0], X[labels==2, 1], s=50, marker='o', color='green')
plt.scatter(X[labels==3, 0], X[labels==3, 1], s=50, marker='o', color='purple')
plt.scatter(X[labels==4, 0], X[labels==4, 1], s=50, marker='o', color='orange')
plt.show()