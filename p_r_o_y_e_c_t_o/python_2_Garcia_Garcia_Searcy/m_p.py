# Abrir el archivo 'Catalogo.txt' en modo lectura
with open("Catalogo.txt", 'r') as archivo:
    sentencia = archivo.readline()  # Leer la primera línea del archivo

    while sentencia:  # Continua leyendo y procesando líneas hasta el final del archivo
        print(sentencia.strip())  # Imprime la línea sin espacios en blanco al principio o al final
        sentencia = archivo.readline()  # Lee la siguiente línea del archivo

print("¿Deseas agregar otra película?")  # Preguntar al usuario si desea agregar otra película
otra = input()

if otra.lower() in ["si", "sí"]:  # Verifica la respuesta del usuario
    from a_p import *  # Importa el módulo y su contenido
else:
    print("¡Ok! ¡Gracias, adiosito!")  # Imprime mensaje de despedida
