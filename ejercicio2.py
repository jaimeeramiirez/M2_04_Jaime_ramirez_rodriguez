
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
