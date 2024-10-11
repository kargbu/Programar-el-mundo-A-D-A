# Agregar en el catalogó con los atributos título, dirección, género, año

while True:
    
  # Solicitar el título a agregar al usuario
    print("Escribe el título de la película que vas a registrar: \n")
    agregar_pelicula = input()

  # Solicitar el director de la película al usuario
    print("Escribe el director de la película que vas a registrar: \n")
    agregar_director = input()

  # Solicitar el género de la película al usuario
    print("Escribe el género de la película que vas a registrar: \n")
    agregar_genero = input()

  # Solicitar el año de la película al usuario
    print("Escribe el año de la película que vas a registrar: \n")
    agregar_anio = input()


  # Abrir el archivo 'Catalogo.txt' en modo de adición y escribir los datos de la película
    with open("Catalogo.txt", 'a') as archivo:
        archivo.write(f"{agregar_pelicula}, {agregar_director}, {agregar_genero}, {agregar_anio}\n")
        print(f'Película {agregar_pelicula} fue registrada.')

  # Preguntar al usuario si quiere agregar otra película    
        print("¿Deseas agregar otra película? SI/NO")
        otra = input().strip().lower()                          # .strip elimina espacios en blanco
    
    if otra in ['si', 'sí']:                                    # consideré que el usuario puede no escribir el acento}
           continue
        
    elif otra in ["no"]:
       print(f'¿Quieres ver la lista de películas? SI/NO\n')
       ver = input().strip().lower()                 # Elimina espacios y pone la entrada en minúsculas

       if ver in['si', 'sí']: 
          with open("Catalogo.txt", 'r') as archivo:
                peliculas = archivo.read()
                print(f'Las películas existentes en el catálogo son:\n{peliculas}')        
       break

    else:
       print("Opción inválida. Por favor escribe SI/NO")
       break