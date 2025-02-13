#Ciclos for y while
#Los ciclos for se utilizan para recorrer una secuencia de elementos, como una lista, tupla, diccionario, etc o llevar una cuenta hasta un numero especifico de veces.
#Como se puede ver en el siguiente caso el digito inicial es 0 y el digito final es 9, el ciclo for se detiene en el digito final - 1, es decir, siempre comenzara en 0 y terminara en el digito final range(numero) - 1
for i in range(10):
    print(i)

#En el ciclo for tenemos 3 espacios en la funcion in range(numero), el primer espacio es el digito inicial, el segundo espacio es el digito final y el tercer espacio es cada cuantos espacios se recorrera la secuencia
#Si dejamos solo un numero en la funcion in range(numero) el ciclo for comenzara en 0 y terminara en el numero seleccionado - 1
#En el siguiente caso el digito inicial es 0, el digito final es 10 y el tercer espacio es 2, por lo que la secuencia sera 0, 2, 4, 6, 8, 10
for i in range(0, 11, 2):
    print(i)

#Tambien podemos utilizar variables en el cliclo for
Box1 = int(input("Ingrese un numero en el cual comenzara el ciclo for: "))
Box2 = int(input("Ingrese un numero en el cual terminara el ciclo for: "))
Box2+=1
i=Box1
for i in range(Box1,Box2):
    print(i)

#Los ciclos while se utilizan para repetir una accion mientras una condicion sea verdadera.
#En el siguiente caso el ciclo while se detiene cuando la variable i sea igual a 1
i = 0
while i != 1:
    print("Bienvenido a la repeticion de un ciclo while, si quieres que termine debes ingresar el numero 1")
    i = int(input("Ingrese un numero: "))
    if i != 1:
        print("El numero ingresado fue:", i,"Ese no es el numero correcto, siguiras atrapada en el ciclo while （づ￣3￣）づ╭❤️～")
    else:
        print("El numero ingresado fue:", i,"Felicidades, has salido del ciclo while (⌐■_■)")

#La condicion puede ser cualquier tipo de comparacion
while i != "Chocolatada":
    print("Bienvenido a la repeticion de un ciclo while, si quieres que termine debes ingresar la palabra Chocolatada")
    i = input("Ingrese una palabra: ")
    if i != "Chocolatada":
        print("La palabra ingresada fue:", i,"Esa no es la palabra correcta, siguiras atrapada en el ciclo while （づ￣3￣）づ╭❤️～")
    else:
        print("La palabra ingresada fue:", i,"Felicidades, has salido del ciclo while (⌐■_■)")
        
#Tanto en los ciclos for como en los ciclos while se pueden utilizar if, elif, else, operadores logicos, operadores relacionales, operadores aritmeticos, etc