import pandas as pd
database = pd.read_csv('G:\dataset\BreadBasket.csv',header = None)
transactions = []
for i in range(0,7501):
    transactions.append([str(database.values[i,j]) for j in range(0,3)])

from apyori import apriori
rules = apriori(transactions,min_supprot = 0.003,min_confidence = 0.2, min_lift = 3,min_length = 2)
print(rules)

results = list(rules)
print(results)