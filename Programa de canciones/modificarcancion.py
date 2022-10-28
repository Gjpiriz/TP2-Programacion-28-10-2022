#from listadecanciones import cancion1
def modificarCanciones (listaCanciones):
     modificar = input("ingrese cancion a modificar : ")
     pos = 0
     for cancion1 in listaCanciones:
          if modificar == cancion1["nombre"]:
               nombre = input("Ingrese el nuevo nombre : ")
               artista = input ("ingrese artista a modificar : ")
               letra = input ("ingrese letra a modificar : ")
               print("nombre de la cancion",modificar,"artista:",artista,"letra:",letra)
               print("modificacion con exito")
               listaCanciones[pos]["nombre"] = nombre
               listaCanciones[pos]["artista"] = artista
               listaCanciones[pos]["letra"] = letra
               return
          pos = pos + 1   
     print("modificacion sin exito")
     