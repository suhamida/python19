from math import* #for manhattan,minkowski,euclidean,cosine,supremum

#manhattan distance
def manhattan_distance(x,y):
 return sum(abs(a-b) for a,b in zip(x,y))
print("Manhattan:% s" % (manhattan_distance([10, 20, 10], [10, 20, 20])))

#Euclidian distance
def euclidean_distance(x,y):
 return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
print("Euclidean:%s"%(euclidean_distance([0, 3, 4, 5], [7, 6, 3, -1])))

#Minkowski distance
from decimal import Decimal
def nth_root(value, n_root):
 root_value = 1/float(n_root)
 return round (Decimal(value) **
Decimal(root_value),3)
def minkowski_distance(x,y,p_value):
 return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)
print("Minkowski:% s"%(minkowski_distance([0, 3, 4, 5], [7, 6, 3, -1], 3)))

#supremum distance
def supremum_distance(x,y):
 return max(abs(a-b) for a,b in zip(x,y))
print("Supremum:%s"%(supremum_distance([0,5,7],[8,7,5])))

#Cosine similarity
def square_rooted(x):
 return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x: object, y: object) -> object:
 numerator = sum(a*b for a,b in zip(x,y))
 denominator =square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),3)
print("Cosine:%s"%(cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15])))