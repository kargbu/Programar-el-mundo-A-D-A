# Este archivo no se va utilizar. Revisar

print("Escribe el nombre de la pelicula a registrar")
Nombre_Peli = input()
with open ("Catalogo.txt", 'w') as archivo:
   archivo.write(Nombre_Peli)
   archivo.write("\n")
   print(Nombre_Peli)
   print("¿Deseas agregar otra pelicula? SI/NO")
   otra = input()

   if otra.lower()in ["si"]:
      import a_p
      from a_p import *
   else: 
      otra.lower() in ["no"]
      print("Ok, gracias, adiosito!")
      



  

