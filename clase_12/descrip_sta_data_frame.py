# Se trata de calcular las principales funciones estadísticas
import statistics as sta
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS_PY/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/catalogo_pelis_1.csv')

# Eliminar espacios en blanco de los nombres de las columnas 
data.columns = data.columns.str.strip() 
# Verificar nombres de columnas 
print(data.columns)
print(data)
# Encuentra la moda de la columan 'año'
#moda_anios = sta.mode(data.año) 
#print('La moda de los años de las películas', moda_anios)


#print(data.info())

if 'Año' in data.columns:
    moda_anios = sta.mode(data['Año'])
    print('La moda es ', moda_anios)
else:
    print('En la columna no está Año.')

