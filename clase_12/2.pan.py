import pandas as pd
import numpy as np

#matriz_data = np.genfromtxt('/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS_PY/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/catalogo_pelis_1.csv', delimiter=',')
#print(matriz_data) Pasar a una matriz, pero hay datos que no son números

data = pd.read_csv('/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS_PY/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/catalogo_pelis_1.csv')
print(data)
print(data.info()) # Nos muestra la información de columnas y filas. La información del DataFrame

# Seleccionar columnas Título
print(data.Título)
# Nos dice qué tipo de dato es
print(data['Título'])

# Seleccionar e imprimir la primera y segunda columna
print(data.loc[1])

# Selecciona e imprime la columna donde hay 'Inception'
print(data[data.Título == 'Inception'])