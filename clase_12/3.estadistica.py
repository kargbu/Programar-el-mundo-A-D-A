
import pandas as pd 
import matplotlib
import statistics as sta

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

# Escribir el fichero, cargarlo y escribir el nombre y el salario más alto


# Eliminar el símbolo de dólar y convertir a números
data['salary'] = data['salary'].replace('[\$,]', '', regex=True).astype(float)

# Encontrar el empleado con el salario más alto
empleado_max_salario = data.loc[data['salary'].idxmax()]

# Imprimir el nombre y el salario del empleado con el salario más alto
print(f"Nombre: {empleado_max_salario['employee_name']}, Salario: {empleado_max_salario['salary']}")
print("El empleado con salario más alto es:")
print(f"employee_id: {empleado_max_salario['employee_id']}")
print(f"employee_name: {empleado_max_salario['employee_name']}") 
print(f"job_title: {empleado_max_salario['job_title']}") 
print(f"department: {empleado_max_salario['department']}") 
print(f"salary: {empleado_max_salario['salary']}")