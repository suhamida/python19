from statistics import mean, median, stdev
n=[500,300,200,700,1000]
n.sort()
print(n)

for x in n:
    temp2 = x/10000
    print("Decimal Scaling Normalization: % s " % (temp2))