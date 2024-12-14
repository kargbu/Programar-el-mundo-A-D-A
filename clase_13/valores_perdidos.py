import matplotlib
import statistics as sta
import pandas as pd
import numpy as np

# WRITE YOUR CODE HERE
stocks =[[2015,1,'???'],[2015,2,0.59],[2015,'???',0.35], [2015,4,None]  ,[2016,2,0.92],[2016,3,0.17],[2016,4,2.66]]
df2 = pd.DataFrame(stocks,columns=['year','qtr','return'])

print (df2)
df2.replace('???' , "None",inplace=True)
print (df2)
print (type(df2["return"][0]))
print (type(df2["return"][3]))