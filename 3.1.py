from statistics import mean, median, stdev
n = [500, 300, 200, 700, 1000]
n.sort()
print(n)
temp = mean(n)
print(temp)
temp1 = (abs(200-temp)+abs(300-temp)+abs(500-temp)+abs(700-temp)+abs(1000-temp))
temp2 = temp1/5
print(temp2)
for x in n:
 t = x/temp2
 print("Z-Score Normalization: % s " % (t))
