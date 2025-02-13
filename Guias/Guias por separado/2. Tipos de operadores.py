#Tipos de operadores
#Operadores aritmeticos, suma, resta, multiplicacion, division, division entera, modulo (residuo de una division), exponente
Box1 = float(input("Ingrese un numero para operaciones aritmeticas: "))
Box2 = float(input("Ingrese otro numero para operaciones aritmeticas: "))
print("Suma: ", Box1 + Box2)
print("Resta: ", Box1 - Box2)
print("Multiplicacion: ", Box1 * Box2)
print("Division: ", Box1 / Box2)
print("Division entera: ", Box1 // Box2)
print("Modulo: ", Box1 % Box2)
print("Exponente: ", Box1 ** Box2)

#Operadores relacionales o de comparacion, igualdad =, desigualdad !=, mayor que >, menor que <, mayor o igual que >=, menor o igual que <=
Box1 = float(input("Ingrese un numero para operaciones relacionales o de comparacion: "))
Box2 = float(input("Ingrese otro numero para operaciones relacionales o de comparacion: "))
print("Igualdad; Sera " + str(Box1) + " igual que " + str(Box2) + "?" + " Resultado:", Box1 == Box2)
print("Desigualdad; Sera " + str(Box1) + " diferente que " + str(Box2) + "?" + " Resultado:", Box1 != Box2)
print("Mayor que; Sera " + str(Box1) + " mayor que " + str(Box2) +"?" + " Resultado:", Box1 > Box2)
print("Menor que; Sera " + str(Box1) + " menor que " + str(Box2) + "?" + " Resultado:", Box1 < Box2)
print("Mayor o igual que; Sera " + str(Box1) + " Mayor o igual que " + str(Box2) + "?" + " Resultado:", Box1 >= Box2)
print("Menor o igual que; Sera " + str(Box1) + " Menor o igual que " + str(Box2) + "?" + " Resultado:", Box1 <= Box2)

#Operadores logicos, and, or, not
#and, si ambos valores son verdaderos, el resultado sera verdadero
Box1 = float(input("Ingrese un numero (a) para operaciones logicas: "))
Box2 = float(input("Ingrese otro numero (b) para operaciones logicas: "))
Box3 = float(input("Ingrese un tercer numero (c) para operaciones logicas: "))
Resultado = (Box1 < Box2) and (Box2 < Box3)
print("Operacion (a < b) and (b < c), resultado: ", Resultado)

#or, si uno de los valores es verdadero, el resultado sera verdadero
Resultado = (Box1 < Box2) or (Box2 > Box3)
print("Operacion (a < b) or (b > c), resultado: ", Resultado)

#not, si el valor es falso, el resultado sera verdadero, estas operaciones tambien se pueden encerrar en variables o expresarse directamente en el print
Resultado2 = (Box1 < Box2)
Resultado = not(Box1 < Box2)
print("Operacion (a < b), resultado: ", Resultado2)
print("Operacion not(a < b), resultado: ", Resultado)

#Operadores de asignacion, =, +=, -=, *=, /=, %=, **=, //=
Box1 = float(input("Ingrese un numero para operaciones de asignacion: "))
Box2 = float(input("Ingrese otro numero para operaciones de asignacion: "))

#Se remplaza el valor de Box1 (la primera variable) por el resultado de la operacion Box1 + Box2 (suma de la primera y segunda variable)
Box1 += Box2
print("Suma con asignacion: ", Box1)
Box1 -= Box2
print("Resta con asignacion: ", Box1)
Box1 *= Box2
print("Multiplicacion con asignacion: ", Box1)
Box1 /= Box2
print("Division con asignacion: ", Box1)
Box1 %= Box2
print("Modulo con asignacion: ", Box1)
Box1 **= Box2
print("Exponente con asignacion: ", Box1)
Box1 //= Box2
print("Division entera con asignacion: ", Box1)