  def mostrar_menu(self):
        print("Hola, ¡bienvenido a Pelimovie!")
        print("Escoge qué deseas hacer (escribe el número)")
        print("1.- Agregar película")
        print("2.- Listar películas")
        print("3.- Eliminar catálogo de películas")
        print("4.- Salir")
        choose = input("Dame un número entre 1 y 4: ")
        return choose
    
     def ejecutar(self):
        while True:
            choose = self.mostrar_menu()
            if not choose.isdigit() or int(choose) not in range(1, 5):
                print("Opción inválida, intenta de nuevo.")
            else:
                choose = int(choose)
                if choose == 1:
                    print("Escogiste la opción 1")
                    try:
                        with open(self.ruta_catalogo) as f:
                            print("El archivo existe")
                            titulo = input("Ingrese el título de la película: ")
                            director = input("Ingrese el director de la película (opcional): ")
                            genero = input("Ingrese el género de la película (opcional): ")
                            año = input("Ingrese el año de la película (opcional): ")
                            print(self.agregar_pelicula(titulo, director, genero, año))
                    except FileNotFoundError:
                        print("El archivo aún no existe")
                        print(self.no_existe_catalogo("Nueva Película"))
                
                elif choose == 2:
                    try:
                        with open(self.ruta_catalogo) as f:
                            print("Mostrar películas existentes en el catálogo")
                            print(self.listar_peliculas())
                    except FileNotFoundError:
                        print("El archivo no existe. Por favor, primero registra una película.")
                        
                elif choose == 3:
                    print("Elimina el catálogo.")
                    print(self.eliminar_catalogo())
                    
                elif choose == 4:
                    print("¡Muchas gracias por visitarnos! ¡Adiós!")
                    break

# Ejecutar la función principal
if __name__ == "__main__":



    def agregar_pelicula(self, titulo, director=None, genero=None, año=None):
        return a_p.agregar_pelicula(self.ruta_catalogo, titulo, director, genero, año)
    
    def listar_peliculas(self):
        return m_p.listar_peliculas(self.ruta_catalogo)

    def buscar_pelicula(self, titulo):
        return m_p.buscar_pelicula(self.ruta_catalogo, titulo)

    def eliminar_pelicula(self, titulo):
        return m_p.eliminar_pelicula(self.ruta_catalogo, titulo)
    
    def no_existe_catalogo(self, Nombre_Peli):
        return c_no_e.no_existe_catalogo(self.ruta_catalogo, Nombre_Peli)
    