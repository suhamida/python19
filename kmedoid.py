from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
import k_medoids
# 3 points in dataset
data = np.array([[1,1],[2,2],[10,10]])

# distance matrix
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = k_medoids.kmedoids(D, 2)   ### ki hoise bujhi na :( ###

print('medoids:')
for point_idx in M:
    print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))


        ### https://github.com/letiantian/kmedoids  ###