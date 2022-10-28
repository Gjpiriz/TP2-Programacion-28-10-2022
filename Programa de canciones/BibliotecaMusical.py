from listadecanciones import crearCanciones
from buscarcanciones  import identificarcancion
from AlmacenarNuevasCanciones import almacenarnuevascanciones
from modificarcancion import modificarCanciones
from listarCanciones import listarCanciones

print("Biblioteca de canciones")
canciones = crearCanciones()
print("opcion1: identificar canciones opcion2:almacenar nuevas canciones opcion3: modificar canciones opcion 4:salir ")

def biblioteca (opcion):
   while opcion != 4:
       opcion = int(input("ingresar opcion : ")) 
       if opcion == 1 :
         identificarcancion(canciones)
       elif opcion == 2 :
         almacenarnuevascanciones(canciones)
       elif opcion == 3 :
         modificarCanciones(canciones)
       elif opcion == 5 :
         listarCanciones(canciones)

     


biblioteca(0)
