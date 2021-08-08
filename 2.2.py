import statistics #for mean,median,mode
import numpy as np #for variance

import matplotlib.pyplot as plt #for boxplot
from numpy import percentile #for percentile
#mean
data1=[13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 23, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
x = statistics.mean(data1)
print("Mean is:", x)

#mode
print("Mode: % s" % (statistics.mode(data1)))

#median
print("Median  : % s " % (statistics.median(data1)))

#stdedi
print("Standard Deviation: % s " % (statistics.stdev(data1)))

#variance
variance = np.var(data1)
print("Variance: % s" %(variance))

#5-number summary
mn = min(data1)
mx = max(data1)
print("Min: % s" %(mn))
quartiles = percentile(data1,[25,50,75])
print('Q1: %3f'%quartiles[0])
#another way to define median
print('Median: %.3f'%quartiles[1])
print('Q3: %.3f'%quartiles[2])
print("Max: % s" %(mx))

#boxplot

box_plot_data = [data1]
plt.boxplot(box_plot_data)
plt.show()

