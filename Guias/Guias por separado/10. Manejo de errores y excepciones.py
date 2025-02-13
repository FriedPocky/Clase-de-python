#Manejo de errores y excepciones en python
#Los errores y excepciones son problemas que pueden ocurrir durante la ejecucion de un programa
#Los errores son problemas que ocurren antes o durante la ejecucion de un programa, los errores son problemas que no se pueden manejar
#Las excepciones son problemas que ocurren durante la ejecucion de un programa, las excepciones son problemas que se pueden manejar
#Para manejar errores y excepciones en python se utiliza la estructura try, except, finally
#try se utiliza para probar un bloque de codigo
#except se utiliza para manejar una excepcion
#finally se utiliza para ejecutar un bloque de codigo, sin importar si ocurre un error o no
#En el siguiente ejemplo se intenta dividir un numero entre 0, lo cual generara un error
try:
    Box1 = 10
    Box2 = 0
    print(Box1 / Box2)
except:
    print("No se puede dividir entre 0")
#Podemos aplicar esto a casi todo tipo de situaciones
#En el siguiente ejemplo se intenta abrir un archivo que no existe, lo cual generara un error
try:
    archivo = open("archivo3.txt","r")
    print(archivo.read())
except:
    print("El archivo no existe")
#Pediremos al usuario que ingrese un numero y si el numero no es valido, se generara un error
try:
    Box1 = int(input("Ingrese un numero: "))

except:
    print("El valor ingresado no es un numero")