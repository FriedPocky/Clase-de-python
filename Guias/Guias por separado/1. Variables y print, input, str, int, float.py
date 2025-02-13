#Inicializacion de variables

Box1 = 0
Box2 = 1
Box3 = 2.5
Texto = "Hola"
Texto2 = "Salchicha"
"etc"

#Uso del print(), input(), str(), int(), float()
#Uso de print() y capturar textos
Texto = input("Ingrese un texto: ")
print("Los numeros dentro de Box1, Box2 y Box3 son:",Box1, Box2, Box3)
print("Haz cambiado la variable Texto a:", Texto,"; La variable Texto 2 se mantuvo como:",Texto2)

#Capturar valores y diferencias entre str, int y float
Box1 = input("Ingrese un numero: ")
Box2 = input("Ingrese otro numero: ")
print("Como los numeros estan en str se suman de la siguiente manera:",Box1 + Box2)
Box1 = int(input("Ingrese un numero: "))
Box2 = int(input("Ingrese otro numero: "))
print("Como los numeros estan en int se suman de la siguiente manera:",Box1 + Box2)
Box1 = float(input("Ingrese un numero: "))
Box2 = float(input("Ingrese otro numero: "))
print("Como los numeros estan en float se suman de la siguiente manera:",Box1 + Box2)

#Tenemos dos opciones para ingresar un numero y un texto a la vez en un print, la primera es separar los valores por comas y la segunda es concatenar los valores con el signo +
#En el caso de la concatenacion se debe convertir los valores numericos a texto con la funcion str()y realizar los espacios de manera manual con comillas
print("Usted ingreso los numeros", Box1,"y", Box2)
print("Usted ingreso los numeros "+str(Box1)+(" ")+str(Box2))

#Podemos guardar el resultado de la suma en una variable y mostrarla en pantalla
Box1 = float(input("Ingrese un numero: "))
Box2 = float(input("Ingrese otro numero: "))
Resultado = Box1 + Box2
print("La suma de los numeros es:",Resultado)
print("Si concatenamos estaria expresado asi "+str(Resultado))