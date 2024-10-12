# 1. Solicitar al usuario que ingrese el nombre del catálogo de películas.
# 2. Si el catálogo ya existe, este se modificará.
# 3. Cuando el catálogo esté configurado, entonces el programa mostrará un menú de opciones.
import os
from pelicula import Pelicula
class CatalogoPeliculas:
    def __init__(self, ruta_directorio):
        self.nombre_catalogo = ''
        self.ruta_directorio = ruta_directorio
        self.peliculas = []


    def solicitar_nombre_catalogo(self):
        self.nombre_catalogo = input('Escribe el nombre del catálogo: ')    
        ruta_catalogo = os.path.join(self.ruta_directorio, self.nombre_catalogo)

        if os.path.exist(ruta_catalogo):
            print('El catálogo ya existe.\n')
        else:
            print('Creando nuevo catálogo.\n')


    def mostrar_menu_catalogo(self):
        print('1. Crear catálogo\n')
        print('2. Lista de catálogos\n')
        print('3. Eliminar catálogo\n')
        print('4. Salir del menú\n')

        elegir_opcion =input('Ingresa un número de las opciones: ')
        return elegir_opcion
    
# Ejecutar el menú de los catálogos
    def ejecutar_menu_catalogo(self):
     
 # Se elige una opción       
        while True:
            elegir_opcion = self.mostrar_menu_catalogo()

# Verificar que el usuario ingresó una opción válida. El método elegir_opcion.isdigit() verifica que la cadena que ingresa el usuario sean dígitos
            if not elegir_opcion.isdigit() or int(elegir_opcion) not in range (1,5):
                print('Opción inválida, intenta de nuevo.')
            else:
                elegir_opcion = int(elegir_opcion)

                if elegir_opcion == 1:
                    print('Escogiste crear un catálogo\n')
                    self.solicitar_nombre_catalogo()
                    self.crear_catalogo()
                   
                elif elegir_opcion == 2:
                    print('Escogiste abrir un catálogo\n')
# Abrir el catálogo que se encuentra en 
                    self.mostrar_archivos_txt()

                elif elegir_opcion == 3:
                    print('Escogiste eliminar un catálogo\n')
                    mensaje = self.eliminar_catalogo()
                    print(mensaje)

                elif elegir_opcion == 4:
                    print('Saliendo del menú...')
                    break
   
   
    def crear_catalogo(self):
        try:
            ruta_archivo = os.path.join(self.ruta_directorio, self.nombre_catalogo + '.txt')
            with opon(ruta_archivo, 'a') as nuevo:
                   while True:
                                titulo   = input('Título de la pélicula:\n ')
                                director = input('Director de la película:\n ')
                                anio     = input('Año de la película:\n ')
                                genero   = input('Género de la película\n')

                                peliculas = Pelicula(titulo, anio, genero, director)
                                self.peliculas.append(peliculas)
                                nuevo.write(str(peliculas + '\n'))

                                continuar = input('¿Deseas añadir otra película? (S/N):\n ')

                                if continuar.lower() != 's':
                                    break
                                print('Catálogo creado con éxito')
        except Exception as e:
            print(f'Error al crear {e}')

    def mostrar_archivos_txt(self):
# Mostrar todos los archivos .txt en el directorio especificado
        try:
            archivos_catalogos = os.listdir(self.ruta_directorio)
            archivos_catalogos_txt = [archivo for archivo in archivos_catalogos
                                       if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print(f'Los catálogos son:\n ')
                for archivo in archivos_catalogos_txt:
                    print(archivo)
            else:
                print('No se encontró ningún catálogo en el directorio.')
        except Exception as e:
            print(f'Error en la lista de catálogos en el directorio {e}')


    def eliminar_catalogo(self):
        try:
            archivo_catalogos = os.listdir(self.ruta_directorio)
            archivos_catalogos_txt = [archivo for archivo in archivo_catalogos
                                      if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print(f'Los archivos son:\n ')

                for i, archivo in enumerate(archivos_catalogos_txt, 1):
                    print(f'{i}. {archivo}')
                elegir_archivo = input('Ingresa el número del archivo que deseas eliminar: ')

                if elegir_archivo.isdigit() and 1 <= int(elegir_archivo) <= len(archivos_catalogos_txt):
                    archivo_a_eliminar = archivos_catalogos_txt[int(elegir_archivo) - 1]
                    ruta_archivo = os.path.join(self.ruta_directorio, archivo_a_eliminar)
                    os.remove(ruta_archivo)
                print(f'El archivo {archivo_a_eliminar} fue eliminado.')
            else:
                print('No hay catalogos en el directorio.')

        except Exception as e:
            print(f'Error al eliminar el catálogo en el directorio')

# Crear una instancia y ejecutar el menú
nombre_catalogo = 'catalogo_pelis_2'
ruta_directorio = '/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/'
        
catalogo = CatalogoPeliculas(nombre_catalogo, ruta_directorio)
catalogo.ejecutar_menu_catalogo()
