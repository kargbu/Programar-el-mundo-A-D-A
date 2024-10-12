# 1. Solicitar al usuario que ingrese el nombre del catálogo de películas.
# 2. Si el catálogo ya existe, este se modificará.
# 3. Cuando el catálogo esté configurado, entonces el programa mostrará un menú de opciones.
import os

class CatalogoPeliculas:
    def __init__(self, nombre_catalogo, ruta_catalogo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_catalogo = ruta_catalogo

    def mostrar_menu_catalogo(self, nombre_catalogo, ruta_catlogo):
        print('1. Crear catálogo\n')
        print('2. Abrir catálogo\n')
        print('3. Eliminar catálogo\n')
        print('4. Salir de menú')
        elegir_opcion =input('Ingresa un número de las opciones:\n ')

        return elegir_opcion
    
# Ejecutar el menú de los catálogos
    
    def ejecutar_menu_catalogo(self):
        while True:
            elegir_opcion = self.mostrar_menu_catalogo()

# Verificar que el usuario ingresó una opción válida. El método elegir_opcion.isdigit() verifica que la cadena que ingresa el usuario sean dígitos

            if not elegir_opcion.isdigit() or int(elegir_opcion) not in range (1,5):
                print('Opción inválida, intenta de nuevo.')
            else:
                elegir_opcion = int(elegir_opcion)

                if elegir_opcion == 1:
                    print('Escogiste crear un catálogo')

                    try:
                        with open(self.ruta_catalogo, 'w') as nuevo:
                            contenido = input('Escribe el contenido del nuevo catálogo')
                                               # Tengo que mandar llamar a la clase Película ¿cómo le hago?
                            nuevo.write(contenido)
                            print('Catálogo creado con éxito')
                    except excepcion as e:
                        print(f'Error al crear {e}')

                elif elegir_opcion == 2:
                    print('Escogiste abrir un catálogo')

                elif elegir_opcion == 3:
                    print('Escogiste eliminar un catálogo')
                    mensaje = self.eliminar_catalogo()
                    print(mensaje)

                elif elegir_opcion == 4:
                    print('Saliendo del menú...')
                    break

    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_catalogo):
            os.remove(self.ruta_catalogo)
            return 'El catálogo fue eliminado con éxito.'
        else:
            return 'No se encontró el archivo del catálogo.'

# Crear una instancia y ejecutar el menú
catalogo = CatalogoPeliculas('Mi Catalogo', 'ruta_del_catalogo.txt')
catalogo.ejecutar_menu_catalogo()
