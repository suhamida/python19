import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
#collection of data sets represented by a numpy array
X = np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91],])
#Merge the two clusters that are closest to each other
linked = linkage(X, 'single')
labelList = range(1, 11)
# show the figure
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top', #Plots the root at the top, and plot descendent links going downwards.
            labels=labelList,
            distance_sort='descending',  #The child with the maximum distance between its direct descendents is plotted first.
            show_leaf_counts=True)  #When True, leaf nodes representing k>1 original observation are labeled with the number of observations they contain in parentheses.
plt.show()

