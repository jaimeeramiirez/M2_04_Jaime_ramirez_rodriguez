#EJERCICIO1.- Crearemos una lista con el nombre "Lista", y una tupla con el nombre "Tupla", para hacer referencia al segundo valor de la lista tendremos que indicarlo. Ya que las listas y las tuplas relacionan el primer elemento con el número 0, el segundo elemento estara vincluado con el número 1 y de la misma manera el tercer elemento de la tupla con el 2. Las tuplas no pueden modificarse por lo que al principio del código deberemos nombrar los elemento de la mimsa. Para modificar una lista podremos añadir o eliminar elementos; en nuestro caso, con la función ".remove" hemos eliminado el segundo elemento de la lista, lo cual no afecta al principio del código ya que el cambio es posterior. Para saber cual es el tamaño de la lista, utilizaremos la función "len" y para añadir elementos, la función ".append"

print("\n")

Lista = ["Futbol", "Baloncesto", "Tenis", "Golf", "Balonmano"]
print(Lista)
print("El segundo elemento de la lista es :", Lista[1])
Lista.remove("Baloncesto")
print(Lista)
print("El tamaño de la lista es de:", len(Lista))
#A continuación, haremos una búsqueda del último elemento de la lista.
print("El útlimo elemento de la lista es:", Lista[3])
Lista.append("Natación")
print(Lista)

print("\n\n")

Tupla = ("Manzana", "pera", "plátano", "naranja")
print(Tupla)
print("El penúltimo elemento de la tupla es:", Tupla[2])
print(len(Tupla))
#Tupla.append("Uva").- Esta función da error ya que cuando estamos en tuplas, no podemos añadir más elementos; es una de las características de las duplas.
#Tupla.remove("naranja").- Pasa lo mismo que con añadir elementos.

print("\n\n\n\n")




#EJERCICIO2.- El ejericio 2 tiene una estructura similar al 1, nos pide que creemos un set y un diccionario. Los set son un tipo de listas que no pueden modificarse a lo largo del código una vez creadas por lo que podremos averiguar su tamaño o imprimirlas pero nunca añadir, eliminar o cambiar sus elmentos. En el caso de los diccionarios, podremos introducir claves nuevas o eliminar claves ya establecidas en el diccionario.

s = {"Mercedes", "Opel", "Volvo","Porsche", "Peugeot"}
print(s)
#print(s[1]).- Parecido a lo que pasa con las tuplas, los sets tampoco pueden modificarse a lo largo del código.
#s.append("Citroen").- Nos da error ya que las sets no pueden modificarse a lo largo del código
print(len(s))

print("\n\n")

dicc= {
  "Nombre" : "Jaime",
  "Edad" : "17",
  "Ocupación" : "Estudiante"
}
print(dicc)
print(dicc["Nombre"][0:5]) #Imprimos el primer elemento de nuestro diccionario, en este caso, tenemos que hacer referencia al número de caracteres y su posición, si lo metieramos en una lista, haríamos referencia solo a su posición
print("\n")
dicc["Estado civil"]="Soltero" #Introducimos una nueva clave
print(dicc)
print(len(dicc)) #Indicamos la longitud del diccionario
print("\n")
dicc["DNI"]="06666666Z" #Introducimos una nueva clave
print(dicc)
print("\n")
del(dicc["Nombre"]) #Eliminamos la clave nombre y su valor asociado
print(dicc)
