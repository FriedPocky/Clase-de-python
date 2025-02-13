#Uso de diccionarios
#Los diccionarios son un tipo de dato que se utiliza para almacenar varios valores en una sola variable
#Los diccionarios son creados utilizando llaves {}
#Los diccionarios contienen valores en pares, la primera parte es la clave y la segunda parte es el valor, la clave y el valor se separan con dos puntos :
#Los diccionarios pueden contener cualquier tipo de dato, incluso otros diccionarios
#Los diccionarios pueden ser modificados, agregando, eliminando o cambiando valores
diccionario = {"Nombre":"Juan","Edad":25,"Sexo":"Masculino"}
print(diccionario)

#Para acceder a un valor especifico de un diccionario se utiliza la clave del valor
#Se escribe diccionario[clave]
print(diccionario["Nombre"])
print(diccionario["Edad"])

#Para modificar un valor de un diccionario se utiliza la clave del valor y se le asigna un nuevo valor
diccionario["Nombre"] = "Pedro"
print(diccionario)

#Tambien podemos darle al usuario la opcion de cambiar un valor del diccionario
clave = str(input("Ingrese la clave (Nombre) que desea cambiar: "))
valor = str(input("Ingrese el nuevo valor: "))
diccionario[clave] = valor
print(diccionario)

#Para agregar un valor a un diccionario se utiliza la funcion update()
diccionario.update({"Pais":"Mexico"})
print(diccionario)

#Tambien podemos darle al usuario la opcion de agregar un valor al diccionario
clave = str(input("Ingrese la clave que desea agregar: "))
valor = str(input("Ingrese el valor que desea agregar: "))
diccionario.update({clave:valor})
print(diccionario)

#Para eliminar un valor de un diccionario se utiliza la funcion pop() y se le asigna la clave del valor que se desea eliminar
diccionario.pop("Pais")
print(diccionario)

#Tambien podemos darle al usuario la opcion de eliminar un valor del diccionario
clave = str(input("Ingrese la clave que desea eliminar: "))
diccionario.pop(clave)
print(diccionario)