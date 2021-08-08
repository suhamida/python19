#min-max
from statistics import mean, median ,stdev
list=[500, 300, 200, 700, 1000]
maximum=1
minimum=0;
for y in list:
    temp3 = ((y - min(list)) / (max(list) - min(list))) * (maximum-minimum )
    print("min max  of %.3f:"%y," is=%.3f"%temp3);

#Z-score
list1=[500, 300, 200, 700, 1000]
for x in list1:
    temp=x-mean(list1)
    temp2=temp/stdev(list1)
    print("Z-Score Normalization: % s " % (temp2))


#Z-score absulate std
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


#decimal
n=[500,300,200,700,1000]
n.sort()
print(n)

for x in n:
    temp2 = x/10000
    print("Decimal Scaling Normalization: % s " % (temp2))