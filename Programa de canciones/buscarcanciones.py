#from listadecanciones import cancion1,cancion2,cancion3,cancion4,cancion5

#Pide un nombre de canción y la busca en el cancionero.
def identificarcancion(canciones):
    nombreCancion = input("ingrese nombre cancion:")
    for cancion in canciones:
        if nombreCancion == cancion["nombre"]:
            print("cancion encontrada")
            print(cancion["nombre"])
            print(cancion["artista"])
            print(cancion["letra"])
            return
    print("cancion no almacenada")