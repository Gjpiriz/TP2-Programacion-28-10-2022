#from listadecanciones import canciones
def almacenarnuevascanciones(canciones):
 cancion = []
 nombre = input("ingrese nueva cancion: ")
 artista = input("ingrese nuevo artista: ")
 letra  =  input("ingrese letra: ")
 cancion = {"nombre":nombre,"artista":artista,"letra":letra}
 canciones.append(cancion)
 print("almacenado con exito")


 
 