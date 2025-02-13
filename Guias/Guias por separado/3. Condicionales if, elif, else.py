#if, elif, else son condicionales que se utilizan para tomar decisiones en un programa.
Box1 = float(input("Ingrese un numero para operaciones de if, elif, else: "))
Box2 = float(input("Ingrese otro numero para operaciones de if, elif, else: "))

#El if se utiliza para ejecutar un bloque de código si una condición es verdadera. En este caso, si Box1 es menor que Box2, se imprime un mensaje.
if Box1 < Box2:
    print("El numero", Box1, "es menor que", Box2)
#El elif se utiliza para ejecutar un bloque de código si la condición anterior no es verdadera y la condición del elif es verdadera. 
#En este caso, si Box1 es mayor que Box2, se imprime un mensaje.
elif Box1 > Box2:
    print("El numero", Box1, "es mayor que", Box2)
#El else se utiliza para ejecutar un bloque de código si ninguna de las condiciones anteriores es verdadera.
else:
    print("El numero", Box1, "es igual que", Box2)

Box1 = str(input("Ingrese un color (rojo, azul o verde) para operaciones de if, elif, else: "))
Box2 = str(input("Ingrese otro color (rojo, azul o verde) para operaciones de if, elif, else: "))
if Box1 == "rojo" and Box2 == "azul":
    print("El color", Box1, "es diferente que el", Box2)
elif Box1 == "rojo" and Box2 == "verde":
    print("El color", Box1, "es diferente que el", Box2)
elif Box1 == "azul" and Box2 == "verde":
    print("El color", Box1, "es diferente que el", Box2)
elif Box1 == "azul" and Box2 == "rojo":
    print("El color", Box1, "es diferente que el", Box2)
elif Box1 == "verde" and Box2 == "rojo":
    print("El color", Box1, "es diferente que el", Box2)
elif Box1 == "verde" and Box2 == "azul":
    print("El color", Box1, "es diferente que el", Box2)
else:
    print("Los colores", Box1, "y", Box2, "son iguales")