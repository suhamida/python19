from pomegranate import*

import numpy as np

mydb = np.array([[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 8], [2, 3, 8], [1, 2, 4]])

bnet = BayesianNetwork.from_samples(mydb)
### weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
### temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

### play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
print(bnet.node_count())
print(bnet.probability([[1, 2, 3]]))
print(bnet.probability([[1, 2, 8]]))