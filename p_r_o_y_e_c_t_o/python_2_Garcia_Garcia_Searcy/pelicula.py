
# pelicula.py
#  Esta clase se encargará de representar una película con sus atributos, como el nombre.


class Pelicula:
    tipo = 'Cine'                                               # Atributo de clase
    
    def __init__(self, titulo, anio, genero, director):
        self.__titulo   = titulo                               # Atributo de instancia
        self.__anio     = anio
        self.genero     = genero
        self.director   = director

    def __str__(self):
        return f'("{self.titulo}", "{self.anio}", "{self.genero}", "{self.director}")'

    @property
    def titulo(self):
        return self.__titulo
# El decorador @property convierte el método titulo en un getter,
#  permitiendo acceder al atributo __titulo de manera controlada.

    # Setter con @nombre.setter
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            raise ValueError('El nombre debe ser una cadena de texto')
# El decorador @titulo.setter define un setter para el atributo __titulo,
#  permitiendo modificar su valor solo si nuevo_titulo es una cadena de texto.
#  Si no lo es, se lanza un ValueError.

    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self, corregir_anio):
        if isinstance(corregir_anio, int):
            self.__anio = corregir_anio
        else:
            raise ValueError('El año de la película debe ser un número')



# Uso de la propiedad
#pelicula_1 = Pelicula('Matriz', 1999, 'Ciencia Ficción', 'Lana Wachowski')
#print(pelicula_1.titulo)  # Llama al getter sin usar paréntesis
#pelicula_1.titulo = 'Matrix'  # Llama al setter como una asignación directa
#print(pelicula_1.titulo)  # Accede nuevamente al atributo usando getter}

#pelicula_2 = Pelicula('Una familia normal', 2003, 'Drama', 'Per Hanefjord') 
# La pelicula_2 tiene el año erroneo, debe ser 2023
#pelicula_2.mostrar_info() # Mostrar la información

# ¿Cómo se accede al año de película para cambiar el año?
