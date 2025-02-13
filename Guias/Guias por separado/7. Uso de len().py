list = ["Manzana", "Pera", "Uva", "Sandia", "Melon", "Kiwi", "Fresa", "Mango", "Papaya", "Cereza"]
tuple = ("GTA V","Red Dead Redemption 2","CS2","The last of us (Juegazo)","Fortnite(Vendo pavos)","FIFA")
#Uso de len()
#La funcion len() se utiliza para contar la cantidad de valores que tiene una lista o tupla
print("Numero de elementos en la lista de frutas:",len(list))
print("Numero de elementos en la tupla de videojuegos:",len(tuple))

#La funcion len() tambien se puede utilizar para contar la cantidad de caracteres que tiene un texto
Texto = input("Ingrese un texto: ")
print("Numero de caracteres en el texto:",len(Texto))

#La funcion len() tambien se puede utilizar para contar la cantidad de caracteres que tiene un numero
Numero = input("Ingrese un numero: ")
print("Numero de caracteres en el numero:",len(Numero))

#La funcion len() tambien se puede utilizar para contar la cantidad de valores que tiene un diccionario
diccionario = {"Nombre":"Juan","Edad":25,"Sexo":"Masculino"}
print("Numero de elementos en el diccionario:",len(diccionario))