#Manejo de archivos
#Los modos de apertura son: "r" para leer un archivo, "a" para agregar texto al final de un archivo, "w" para escribir en un archivo, "x" para crear un archivo
#Para abrir un archivo se utiliza la funcion open()
#Se escribe open("nombre del archivo","modo de apertura")
archivo = open("archivo.txt","w")

#Para escribir en un archivo se utiliza la funcion write()
#Se escribe archivo.write("texto")
archivo.write("Hola, este es un archivo de texto")

#Para cerrar un archivo se utiliza la funcion close()
#Se escribe archivo.close()
archivo.close()
archivo = open("archivo.txt","r")

#Para leer un archivo e imprimirlo se utiliza la funcion read()
#Se escribe archivo.read()
print(archivo.read())
archivo.close()

#Para agregar texto al final de un archivo se utiliza la funcion open() con el modo de apertura "a"
archivo = open("archivo.txt","a")

#\n se utiliza para hacer un salto de linea
archivo.write("\nEste es un texto agregado al final del archivo")
archivo.close()

#Para crear un archivo se utiliza la funcion open() con el modo de apertura "x"
archivo2 = open("archivo2.txt","x")
archivo2.write("Este es un archivo nuevo, nombrado como archivo2")
archivo2.close()
archivo2 = open("archivo2.txt","r")
print(archivo2.read())
archivo2.close()

#Para eliminar un archivo se utiliza la funcion remove()
#Se escribe remove("nombre del archivo")
import os
os.remove("archivo2.txt")

#Para verificar si un archivo existe se utiliza la funcion exists()
#Se escribe exists("nombre del archivo")
import os.path
print(os.path.exists("archivo2.txt"))

#Para renombrar un archivo se utiliza la funcion rename()
#Se escribe rename("nombre del archivo","nuevo nombre del archivo")
os.rename("archivo.txt","Primer archivo.txt")

#Para verificar si un archivo fue renombrado se utiliza la funcion exists()
print(os.path.exists("archivo.txt"))
print(os.path.exists("Primer archivo.txt"))
os.rename("Primer archivo.txt","archivo.txt")

#Para copiar un archivo se utiliza la funcion copy()
#Se escribe copy("nombre del archivo","nombre del archivo copiado")
import shutil
shutil.copy("archivo.txt","archivo copiado.txt")

#Para verificar si un archivo fue copiado se utiliza la funcion exists()
print(os.path.exists("archivo copiado.txt"))
os.remove("archivo copiado.txt")

#entre otras funciones que podemos realizar con archivos    
#Si se intenta crear un archivo con el modo de apertura "x" y el archivo ya existe, se generara un error
#Si se intenta abrir un archivo que no existe con el modo de apertura "r", se generara un error
#Si se intenta abrir un archivo que no existe con el modo de apertura "a" o "w", se creara un archivo nuevo
#No podemos imprimir un archivo si no lo abrimos con el modo de apertura "r"