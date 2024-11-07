
import pandas as pd 
import matplotlib
import statistics as sta
#loading our csv

data= pd.read_csv('Escribir la ruta del archivo')
# print(data)
# print(data.info())
# print(data.head())
moda_data = sta.mode(data['Home Runs'])
print(f'La moda es {moda_data}')
mean_data = sta.mean(data['Home Runs'])
print(f'El promedio es {mean_data}')
median_data = sta.median(data['Home Runs'])
print(f'La mediana es {median_data}')
range_data = max(data['Home Runs']) - min(data['Home Runs'])
print(f'El rango es {range_data}')
sum_data = sum(data['Home Runs'])
print(f'La suma de la columna es {sum_data}')

