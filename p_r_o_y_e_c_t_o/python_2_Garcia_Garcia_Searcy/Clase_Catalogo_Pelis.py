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
        if os.path.exists(ruta_catalogo):  
            print('El catálogo ya existe.\n')
        else:
            print('Se creo el catálogo {self.nombre_catalogo}.\n')

    def mostrar_menu_catalogo(self):
        print('1. Crear catálogo\n')
        print('2. Lista de catálogos\n')
        print('3. Eliminar catálogo\n')
        print('4. Salir del menú\n')
        elegir_opcion = input('Ingresa un número de las opciones: ')
        return elegir_opcion

    def ejecutar_menu_catalogo(self):
        while True:
            elegir_opcion = self.mostrar_menu_catalogo()
            if not elegir_opcion.isdigit() or int(elegir_opcion) not in range(1, 5):
                print('Opción inválida, intenta de nuevo.')
            else:
                elegir_opcion = int(elegir_opcion)
                if elegir_opcion == 1:
                    print('Escogiste crear un catálogo\n')
                    self.solicitar_nombre_catalogo()
                    self.crear_catalogo()
                    self.mostrar_archivos_txt()
                elif elegir_opcion == 2:
                    print('Escogiste abrir un catálogo\n')
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
            with open(ruta_archivo, 'a') as nuevo:  # Corregido: 'opon' a 'open'
                while True:
                    titulo = input('Título de la pélicula:\n ')
                    director = input('Director de la película:\n ')
                    anio = input('Año de la película:\n ')
                    genero = input('Género de la película:\n')
                    pelicula = Pelicula(titulo, anio, genero, director)
                    self.peliculas.append(pelicula)
                    nuevo.write(str(pelicula) + '\n')
                    continuar = input('¿Deseas añadir otra película? (S/N):\n ')
                    if continuar.lower() != 's':
                        break
                print('Catálogo creado con éxito')
        except Exception as e:
            print(f'Error al crear el catálogo: {e}')

    def mostrar_archivos_txt(self):
        try:
            archivos_catalogos = os.listdir(self.ruta_directorio)
            archivos_catalogos_txt = [archivo for archivo in archivos_catalogos if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print('Los catálogos son:\n ')
                for archivo in archivos_catalogos_txt:
                    print(archivo)
            else:
                print('No se encontró ningún catálogo en el directorio.')
        except Exception as e:
            print(f'Error al listar los catálogos: {e}')

    def eliminar_catalogo(self):
        try:
            archivos_catalogos = os.listdir(self.ruta_directorio)
            archivos_catalogos_txt = [archivo for archivo in archivos_catalogos if archivo.endswith('.txt')]
            if archivos_catalogos_txt:
                print('Los archivos son:\n ')
                for i, archivo in enumerate(archivos_catalogos_txt, 1):
                    print(f'{i}. {archivo}')
                elegir_archivo = input('Ingresa el número del archivo que deseas eliminar: ')
                if elegir_archivo.isdigit() and 1 <= int(elegir_archivo) <= len(archivos_catalogos_txt):
                    archivo_a_eliminar = archivos_catalogos_txt[int(elegir_archivo) - 1]
                    ruta_archivo = os.path.join(self.ruta_directorio, archivo_a_eliminar)
                    os.remove(ruta_archivo)
                    print(f'El archivo {archivo_a_eliminar} fue eliminado.')
            else:
                print('No hay catálogos en el directorio.')
        except Exception as e:
            print(f'Error al eliminar el catálogo en el directorio: {e}')

# Crear una instancia y ejecutar el menú
ruta_directorio = '/Users/kgb/Desktop/ADA_TRABAJOS/ADA_TRABAJOS/p_r_o_y_e_c_t_o/python_2_Garcia_Garcia_Searcy/'
catalogo = CatalogoPeliculas(ruta_directorio)
catalogo.ejecutar_menu_catalogo()
