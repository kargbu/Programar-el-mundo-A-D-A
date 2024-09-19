# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: 

#Modulo random (paso 4)
import random 
print('¡Te doy la bienvenida a la Trivia sobre Python!')
# Paso 3
# Nombre usuario
nombre = input('Ingresa tu nombre, por favor: ')
# Edad usuario
edad = int(input('Ingresa tu edad, por favor: '))

if edad >= 18:
    print(f' \n¡Hola {nombre}, Es hora de comenzar con la Trivia sobre python!\n ')
    print("Antes de comenzar, las instrucciones del juego son las siguientes: ")
    print('debes de contestar correctamente las preguntas, por cada respuesta correcta \nvas a ganar 1 punto. Sin emabrgo, por cada respuesta incorrecta \nno sumaras puntos, pero si te equivocas más de tres veces pierdes el juego.')
    print('¡Ahora si, a jugar!')
else:
    print(f'Lo siento {nombre}, no tienes la edad mínima para jugar. ')
    exit()

# Paso 5 preguntas y respuestas
# Definir las preguntas y sus respuestas en un diccionario
preguntas = {
    'Pregunta 1': 'verdadero',               
    'Pregunta 2': 'verdadero',               
    "Pregunta 3": 'falso'
 } # FALTA AÑADIR LAS PREGUNTAS!

# Convertir en tuplas
Lista_preguntas = list(preguntas.items())

# Usar shuffle para mezclar las preguntas 
random.shuffle(Lista_preguntas)

# Preguntar y evaluar la respuesta
score = 0

for preguntaX, respuesta_correcta in Lista_preguntas:     #Ciclo for para que me muestre las preguntas de manera aleatoria
    respuesta_usuario = input(f'{preguntaX} (Responde verdadero o falso): ').lower()

    if (respuesta_usuario == 'verdadero' and respuesta_correcta) or (respuesta_usuario == 'falso' and not respuesta_correcta):
        print('Es correcto')
        score += 1
    else:
        print('Es incorrecto')
    print(f'Tu puntuación es de {score}')

print(f'Puntuación final: {score}/{len(Lista_preguntas)}')



