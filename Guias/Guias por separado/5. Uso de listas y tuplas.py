#Uso de listas
print("Uso de listas:")
#Las listas son un tipo de dato que se utiliza para almacenar varios valores en una sola variable
#Las listas son creadas utilizando corchetes []
#Las listas pueden contener cualquier tipo de dato, incluso otras listas
#Las listas pueden ser modificadas, agregando, eliminando o cambiando valores
list = ["Manzana", "Pera", "Uva", "Sandia", "Melon", "Kiwi", "Fresa", "Mango", "Papaya", "Cereza"]
print(list)

#Para acceder a un valor especifico de una lista se utiliza el indice del valor
#Los indices comienzan en 0, por lo que el primer valor de la lista es 0, el segundo es 1, el tercero es 2, etc, podemos llamar a un valor especifico de la lista utilizando list[indice]
print(list[0])
print(list[5])

#Si queremos acceder a un rango de valores de una lista se utiliza el indice inicial y el indice final, se escribe list[indice inicial:indice final]
#El rango de valores se mostrara desde el indice inicial hasta el indice final - 1
print(list[0:5])

#Si se deja en blanco el indice inicial, se mostrara desde el primer valor de la lista hasta el indice final - 1
print(list[:3])

#Si se deja en blanco el indice final, se mostrara desde el indice inicial hasta el ultimo valor de la lista
print(list[5:])

#Para modificar un valor de una lista se utiliza el indice del valor y se le asigna un nuevo valor
list[0] = "Durazno"
print(list)

#Tambien podemos darle al usuario la opcion de cambiar un valor de la lista
indice = int(input("Ingrese el numero del indice que desea cambiar: "))
indice -= 1
valor = str(input("Ingrese el nuevo valor: "))
list[indice] = valor
print(list)

#Para agregar un valor a una lista se utiliza la funcion append()
list.append("Naranja")
print(list)

#Tambien podemos darle al usuario la opcion de agregar un valor a la lista
valor = str(input("Ingrese el valor que desea agregar: "))
list.append(valor)
print(list)

#Para eliminar un valor de una lista se utiliza la funcion remove()
list.remove("Naranja")
print(list)

#Tambien podemos darle al usuario la opcion de eliminar un valor de la lista
valor = str(input("Ingrese el valor que desea eliminar en texto: "))
list.remove(valor)
print(list)

#Para eliminar un valor de una lista se utiliza la funcion pop() y se le asigna el indice del valor que se desea eliminar
list.pop(0)
print(list)

#Tambien podemos darle al usuario la opcion de eliminar un valor de la lista
indice = int(input("Ingrese el numero del indice que desea eliminar: "))
indice -= 1
list.pop(indice)
print(list)

#Para eliminar todos los valores de una lista se utiliza la funcion clear()
list.clear()
print(list)

#Tambien podemos darle al usuario la opcion de eliminar todos los valores de la lista
opcion = str(input("Desea eliminar todos los valores de la lista? (si/no): "))
if opcion == "si":
    list.clear()
    print(list)
else:
    print("La lista no ha sido modificada")

#Para copiar una lista se utiliza la funcion copy()
list = ["Manzana", "Pera", "Uva", "Sandia", "Melon", "Kiwi", "Fresa", "Mango", "Papaya", "Cereza"]
list2 = []
list2 = list.copy()
print(list2)

#Aunque no se puede copiar una lista utilizando list2 = list, ya que si se modifica list2 tambien se modificara list
list2 = list
list2[0] = "Durazno"
print(list2)
print(list)

#Para unir dos listas se utiliza la funcion extend()
list.extend(list2)
print(list)

#Uso de tuplas
print("Uso de tuplas:")

#Las tuplas son un tipo de dato que se utiliza para almacenar varios valores en una sola variable
#Las tuplas son creadas utilizando parentesis ()
#Las tuplas pueden contener cualquier tipo de dato, incluso otras tuplas
#Las tuplas no pueden ser modificadas, agregando, eliminando o cambiando valores
tuple = ("GTA V","Red Dead Redemption 2","CS2","The last of us (Juegazo)","Fortnite(Vendo pavos)","FIFA")
print(tuple)

#Podemos realizar todas las acciones que se realizan con las listas, excepto los que incluyan modificaciones a los valores de la tupla
#Podemos imprimir la lista o tupla saltando los espacios con un ciclo for
for i in tuple:
    print(i)

#En el ejemplo de duran sale asi, pero realmente es lo mismo:
for i in range(len(tuple)):
    print(tuple[i])