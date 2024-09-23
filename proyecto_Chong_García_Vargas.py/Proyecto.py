# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes:  Catalina Vargas
#               Karina García Buendía
#

# Paso 4 Modulo random
import random

# Paso 8 Creación de funciones
def juego_trivia():

    def bienvenida ():
        print('\n¡Te doy la bienvenida al juego de L A   T R I V I A  D E   P Y T H O N!')
        
# Paso 3 Estructura básica del juego
    # 3.1 Nombre del usuario

    def datos ():
        nombre = input('\nIngresa tu nombre, por favor: ')

    # 3.2 Edad del usuario

        edad = int(input('\nIngresa tu edad, por favor: '))
       
        if edad >= 18:
         print(f'\n¡Hola, {nombre}!\nEres mayor de edad. Es hora de comenzar con la trivia.\n')
        else:
            print(f'\nLo siento {nombre}, no tienes la edad mínima para jugar. \n')
            exit()
        return nombre, edad

    def instrucciones():
        print('\nAntes de comenzar, las instrucciones del juego son las siguientes: debes contestar correctamente las preguntas. '
              'Por cada respuesta correcta ganarás 1 punto. Sin embargo, por cada respuesta incorrecta no sumarás puntos, '
              'pero si te equivocas más de tres veces, pierdes el juego.\n¡Ahora sí, a jugar!')

# Paso 5 preguntas y respuestas

    # 5.1 Definir las preguntas y sus respuestas en un diccionario
    def preguntas_y_respuestas():
        preguntas = {
        'Pregunta 1': 'verdadero',               
        'Pregunta 2': 'verdadero',               
        "Pregunta 3": 'falso'
 } # FALTA AÑADIR LAS PREGUNTAS!

    # 5.2 Convertir en tuplas

        lista_preguntas = list(preguntas.items())

    # 5.3 Usar shuffle para mezclar las preguntas 

        random.shuffle(lista_preguntas)
        return lista_preguntas

# Paso 6 y 7 Mostrar la preguntar y evaluar la respuesta
    # Contador de puntuación
    def jugar(lista_preguntas):
        score = 0

    # Contador de intentos fallidos
        errores = 0

    # 1.6 Ciclo para mostar preguntas
        for preguntaX, respuesta_correcta in lista_preguntas:     #Ciclo for para que me muestre las preguntas de manera aleatoria
            respuesta_usuario = input(f'{preguntaX} (Responde verdadero o falso): ').lower()

# Validar respuestas
        if (respuesta_usuario == 'verdadero' and respuesta_correcta) or (respuesta_usuario == 'falso' and not respuesta_correcta):
            print('Es correcto')
            score += 1
        else:
            print('Es incorrecto')
            errores += 1
            print(f'Tu puntuación es de {score}')

    # 6.2 Contar y controlar los intentos fallidos
        if errores != 3:
            print(f'Puntuación final: {score}/{len(lista_preguntas)}')

# Paso 7 Controlar errores consecutivos
        while errores <= 3:
            print(f'Fallaste tres veces. Final del juego.')
            break
     # Mostrar mensaje final
    print('\n¡Gracias por jugar esta trivia sobre Python, bonito día!') 
    bienvenida()
    datos()
    instrucciones()
    lista_preguntas = preguntas_y_respuestas()
    jugar(lista_preguntas)

juego_trivia()
