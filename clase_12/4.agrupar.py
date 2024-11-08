# Calcule el salario medio de cada departamento
import pandas as pd 
import matplotlib
import statistics as sta

data= pd.read_csv('MOCK_COMPANY_DATA.csv')
print(data)
import pandas as pd

# Eliminar el símbolo de dólar y convertir a números
data['salary'] = data['salary'].replace('[\$,]', '', regex=True).astype(float)

# Calcular el salario promedio por departamento
salario_promedio_departamento = data.groupby('department')['salary'].mean()

# Imprimir el salario promedio por departamento
print(salario_promedio_departamento)
 ##########################################################################
 

# Remove the dollar sign and convert the 'salary' column to float
data['salary'] = data['salary'].str.replace('$', '').astype(float)

# Find the employee with the highest salary
highest_salary_employee = data.loc[data['salary'].idxmax()]
print("Employee with the highest salary:")
print(highest_salary_employee)


# Calculate the average salary for each department
average_salary_per_department = data.groupby('department')['salary'].mean()

# Print the average salary for each department
print("Average salary per department:")
print(average_salary_per_department)
