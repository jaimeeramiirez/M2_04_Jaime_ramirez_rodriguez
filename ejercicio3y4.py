
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

