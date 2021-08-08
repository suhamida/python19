import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('G:\dataset\BreadBasket.csv')
store_data.head()
store_data = pd.read_csv('G:\dataset\BreadBasket.csv', header=None)
store_data.head()
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 3)])
    association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
    association_results = list(association_rules)
    print(len(association_results))
    print(association_results)
    #print(' '.join(map(str, association_rules[0])))
