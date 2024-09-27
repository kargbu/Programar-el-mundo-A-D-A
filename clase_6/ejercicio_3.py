# Ejercicio 3. Rango, enumeración y break y continua

lista_cadena = ['yo', 'te', 'quiero', 'para', 'beso', 'casa', 'mandarina', 'compras', '', 'Uruguay', 'viaje', 'trabajo']

# Crear el objeto en enumerate
mostrara_in_val = enumerate(lista_cadena, 0)

# Imprimir los elementos enumerados
for indice, valor in mostrara_in_val:
   
    if valor == '':
        print(f'{indice} encontró al vacío')

        continue

    print(f'{indice}: {valor}')