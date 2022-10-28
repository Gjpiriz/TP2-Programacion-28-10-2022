#from listadecanciones import cancion1,cancion2,cancion3,cancion4,cancion5

#Pide un nombre de canción y la busca en el cancionero.
def listarCanciones(canciones):
    for cancion in canciones:
        print("cancion: ")
        print(cancion["nombre"])
        print(cancion["artista"])
        print(cancion["letra"])


