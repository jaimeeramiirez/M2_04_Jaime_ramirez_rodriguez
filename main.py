#Crearemos una lista con el nombre "Lista", y una tupla con el nombre "Tupla", para hacer referencia al segundo valor de la lista tendremos que indicarlo. Ya que las listas y las tuplas relacionan el primer elemento con el número 0, el segundo elemento estara vincluado con el número 1 y de la misma manera el tercer elemento de la tupla con el 2. Las tuplas no pueden modificarse por lo que al principio del código deberemos nombrar los elemento de la mimsa.



print("\n")

Lista = ["Futbol", "Baloncesto", "Tenis", "Golf"]
print(Lista)
print ("El segundo elemento de la lista es :", Lista [1])
Lista.remove("Baloncesto")
print(Lista)

print("\n\n")

Tupla = ("Manzana", "pera", "plátano", "naranja")
print (Tupla)
print("El penúltimo elemento de la tupla es:", Tupla[2])