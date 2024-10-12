# 1. Solicitar al usuario que ingrese el nombre del catálogo de películas.
# 2. Si el catálogo ya existe, este se modificará.
# 3. Cuando el catálogo esté configurado, entonces el programa mostrará un menú de opciones.
import os
from pelicula import Pelicula
class CatalogoPeliculas:
    def __init__(self, nombre_catalogo, ruta_catalogo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_catalogo = ruta_catalogo
        self.peliculas = []

    def mostrar_menu_catalogo(self, nombre_catalogo, ruta_catalogo):
        print('1. Crear catálogo\n')
        print('2. Abrir catálogo\n')
        print('3. Eliminar catálogo\n')
        print('4. Salir del menú\n')

        elegir_opcion =input('Ingresa un número de las opciones: ')

        return elegir_opcion
    
# Ejecutar el menú de los catálogos
    
    def ejecutar_menu_catalogo(self):
     
 # Se elige una opción       
        while True:
            elegir_opcion = self.mostrar_menu_catalogo(nombre_catalogo, ruta_catalogo)

# Verificar que el usuario ingresó una opción válida. El método elegir_opcion.isdigit() verifica que la cadena que ingresa el usuario sean dígitos

            if not elegir_opcion.isdigit() or int(elegir_opcion) not in range (1,5):
                print('Opción inválida, intenta de nuevo.')
            else:
                elegir_opcion = int(elegir_opcion)

                if elegir_opcion == 1:
                    print('Escogiste crear un catálogo')

                    try:
                        with open(self.ruta_catalogo, 'w') as nuevo:

                            while True:
                                titulo   = input('Título de la pélicula:\n ')
                                director = input('Director de la película:\n ')
                                anio     = input('Año de la película:\n ')
                                genero   = input('Género de la película')

                                peliculas = Pelicula(titulo, anio, genero, director)
                                self.peliculas.append(pelicula)
                                nuevo.write(str(peliculas + '\n'))

                                continuar = input('¿Deseas añadir otra película? (S/N):\n ')

                                if continuar.lower() != 's':
                                    break
                                print('Catálogo creado con éxito')
                    except Exception as e:
                        print(f'Error al crear {e}')

                elif elegir_opcion == 2:
                    print('Escogiste abrir un catálogo')
# Abrir el catálogo que se encuentra en 
                    self.mostrar_archivos_txt(self.nombre_catalogo, self.ruta_catalogo)

                elif elegir_opcion == 3:
                    print('Escogiste eliminar un catálogo')
                    mensaje = self.eliminar_catalogo()
                    print(mensaje)

                elif elegir_opcion == 4:
                    print('Saliendo del menú...')
                    break
    
    def mostrar_archivos_txt(self,nombre_catalogo, ruta_catalogo):
# Mostrar que el/los archivos existen
        if os.path.exists(self.ruta_catalogo):
            try:
                with open(self.ruta_catalogo, 'r') as archivo:
                     contenido = archivo.read()
                     print(f'El contenido {self.ruta_catalogo}:\n{contenido}')
                
            except FileNotFoundError:
                print(f'No se encontró {self.ruta_catalogo}')
        else:
             print(f'El archivo {self.ruta_catalogo} no existe.')

# Mostrar todos los archivos .txt en el directorio especificado
        try:
            archivos_catalogos = os.listdir(self.ruta_catalogo)
            archivos_catalogos_txt = [archivo for archivo in archivos_catalogos
                                       if archivos_catalogos.endswith('.txt')]
            if archivos_catalogos_txt:
                print(f'Los catálogos son:\n {self.ruta_catalogo}')
                for archivo in archivos_catalogos_txt:
                    print(archivo)
            else:
                print('No se encontró ningún catálogo en el directorio.')
        except Exception as e:
            print(f'Error en la lista de catálogos: {e}')
    
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_catalogo):
            os.remove(self.ruta_catalogo)
            return 'El catálogo fue eliminado con éxito.'
        else:
            return 'No se encontró el archivo del catálogo.'

# Crear una instancia y ejecutar el menú
nombre_catalogo = 'catalogo_pelis_1'
ruta_catalogo = '/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/'
        
catalogo = CatalogoPeliculas(nombre_catalogo, ruta_catalogo)
catalogo.ejecutar_menu_catalogo()
