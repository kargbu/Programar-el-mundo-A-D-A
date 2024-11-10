# Ya no calculamos a mano la desviación estandar

#import matplotlib
#import pandas as pd 
#from scipy.stats import ttest_ind
import statistics as sta

sample_1 = [1,2,3,4,5]
sample_2 = [1,2,3,4,18]
sample_3 = [1,2,3,4,999]

print(sta.stdev(sample_1),sta.mean(sample_1))
print(sta.stdev(sample_2),sta.mean(sample_2))
print(sta.stdev(sample_3),sta.mean(sample_3))
