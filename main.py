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


print("\n\n\n\n")



#EJERCICIO 3 y 4.- Pedir un número al usuario es algo que ya llevamos haciendo un par de códigos por lo que no tiene mucha complejidad, lo único que debemos tener en cuenta es que se trata de un "float". Para la lista de números simplemente hacemos referencia a los variables y las metemos dentro de la lista. La función "sum" nos ayuda a hacer el sumatorio de la lista sin tener que hacer refencia a cada una de las variables. Para la media aritmética, como no siempre vamos a tener 3 elementos nos interesa saber cuantos elementos va a tener la lista, para eso; lo que hacemos es usar la función "len" y siempre dividiremos el sumatorio por el número de elementos de la lista.

num1= float(input("Introduce el primer número: "))
print("\n")
num2= float(input("Introduce el segundo número: "))
print("\n")
num3= float(input("Introduce el tercer número: "))
print("\n")

Listanum=[num1, num2, num3]
print(Listanum)
sumatorio=sum(Listanum)
print("La suma de los elementos de la lista es: ",sumatorio)
print("\n")
Media=(sumatorio/(len(Listanum)))
print("La media aritmética de los elementos de la lista es= ", Media)












