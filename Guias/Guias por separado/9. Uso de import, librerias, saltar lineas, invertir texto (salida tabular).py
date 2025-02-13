#Uso de import, librerias, salto de linea, invertir una lista o tupla (segun progra 1 ujap)
#Import se utiliza para importar una libreria completa o una funcion especifica de una libreria, las librerias son un conjunto de funciones que se pueden utilizar en un programa
# Importamos randint
from random import randint
#Al usar from ramdom import randint, no es necesario escribir random.randint(), solo se escribe randint(), ademas de que solo importamos la funcion randint en lugar de todas las funciones de la libreria random
cant = 0
numeros = []  # Crea una lista en blanco
i = 0
limInf = limSup = 0  # Limites del intervalo de randint

# Entrada de datos
cant = int(input("Cantidad de elementos aleatorios: "))
limInf = int(input("Limite inferior: "))
limSup = int(input("Limite superior: "))

# Llenado de la lista
for i in range(cant):
    numeros.append(randint(limInf, limSup))

print("\n", numeros)  # Imprime la lista en el orden correcto

# Imprime la lista en el orden inverso
for i in range(cant):
    print(numeros[-i], end=", ")
#end=", " se utiliza para al final de cada valor de la lista se imprima una coma y un espacio o lo deseado
#"\n" se utiliza para hacer un salto de linea
print("\n")
for i in range(cant):
    print(numeros[-i], end=" ")

#salida en formato de tabular (tabla)
# Inicializar variables
nom = ""
genero = ""
estatus = ""

n1 = 0
n2 = 0
n3 = 0

prom = 0.0
promMR = 0.0
porcFA = 0.0

contFA = 0
contF = 0

acumMR = 0.0

contM = 0

band = 0

mnom = ""

mprom = 0.0

registro = ""

# Abrimos el archivo
archivo = open("Colegio.txt")

# Títulos cabeceras de la tabla de salida
print("Nombre    Nota Final   Estatus")

# Ciclo para leer los registros de un archivo
for registro in archivo:
    campos = registro.split(",")  # Fragmentación del registro en campos
    nom = campos[0]  # Asignación de los campos a las variables

    genero = campos[1]
    n1 = int(campos[2])
    n2 = int(campos[3])
    n3 = int(campos[4])

    # 1. Calculamos promedio del estudiante
    prom = (n1 + n2 + n3) / 3

    if prom >= 9.5:  # Validamos si el alumno aprobó
        estatus = "APROBÓ"  # Corregido: falta la tilde en "APROBÓ"
    else:
        estatus = "REPROBÓ"  # Corregido: falta la tilde en "REPROBÓ"

    print("{0:12} {1:12.2f} {2:12}".format(nom, prom, estatus))  # Formato de salida corregido

    # Cálculos para todos los alumnos
    # 2. Determinar valores cálculo porcentaje
    if genero == "F" or genero == "f":
        contF += 1  # Cuántas alumnas
        if prom >= 9.5:
            contFA += 1  # Cuenta alumnas aprobadas

    # 3. Determinar valores cálculo promedio
    if (genero == "M" or genero == "m") and (prom < 9.5):
        acumMR += prom
        contM += 1

    # 4. Determinamos alumno con el mayor promedio
    if band == 0:  # Corregido: Se agregó la comparación ==
        mnom = nom
        mprom = prom
        band = 1  # Se movió la asignación a la línea 45
    elif mprom < prom:  # Corregido: Se agregó la comparación <
        mnom = nom
        mprom = prom

print()
print("Cálculos finales y salida resultados")

# Calculamos el porcentaje
if contF > 0:
    porc = (contFA / contF) * 100  # Corregido: Se agregó paréntesis y se corrigió la fórmula
    print("Porcentaje de alumnas que aprobaron:", porc, "%")  # Corregido: Se agregó coma para separar los elementos
else:
    print("No hay alumnas en el curso")  # Corregido: Se corrigió la palabra "cuerso"

if contM > 0:
    promMR = acumMR / contM  # Corregido: Se agregó la asignación "="
    print("Nota promedio alumnos reprobados:", promMR)  # Corregido: Se agregó coma para separar los elementos
else:
    print("No hay alumnos en el curso")

print("Estudiante con la mayor calificación:", mnom)  # Corregido: Se agregó la tilde en "calificación"
archivo.close()
print(archivo.closed)
print("Fin programa")