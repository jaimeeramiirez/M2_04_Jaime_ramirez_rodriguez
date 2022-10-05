
#EJERCICIO1.- Crearemos una lista con el nombre "Lista", y una tupla con el nombre "Tupla", para hacer referencia al segundo valor de la lista tendremos que indicarlo. Ya que las listas y las tuplas relacionan el primer elemento con el número 0, el segundo elemento estara vincluado con el número 1 y de la misma manera el tercer elemento de la tupla con el 2. Las tuplas no pueden modificarse por lo que al principio del código deberemos nombrar los elemento de la mimsa. Para modificar una lista podremos añadir o eliminar elementos; en nuestro caso, con la función ".remove" hemos eliminado el segundo elemento de la lista, lo cual no afecta al principio del código ya que el cambio es posterior. Para saber cual es el tamaño de la lista, utilizaremos la función "len" y para añadir elementos, la función ".append"

print("\n")

Lista = ["Futbol", "Baloncesto", "Tenis", "Golf", "Balonmano"]
print(Lista)
print("El segundo elemento de la lista es :", Lista[1])
print("El tamaño de la lista es de:", len(Lista))
#A continuación, haremos una búsqueda del último elemento de la lista.
print("El útlimo elemento de la lista es:", Lista[4])
Lista.append("Natación")
Lista.remove("Baloncesto") #Eliminamos "baloncesto" de nuestra lista
print(Lista)

print("\n\n")

Tupla = ("Manzana", "pera", "plátano", "naranja")
print(Tupla)
print("El penúltimo elemento de la tupla es:", Tupla[2])
print(len(Tupla))
#Tupla.append("Uva").- Esta función da error ya que cuando estamos en tuplas, no podemos añadir más elementos; es una de las características de las duplas.
#Tupla.remove("naranja").- Pasa lo mismo que con añadir elementos.


