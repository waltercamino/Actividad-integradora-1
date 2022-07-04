import os
import time
#Integgrantes del grupo
#Walter Camino
#Nicolas Figueroa
#Alan Moreno

#Funsion Sumar
def Sumar(lista):
    suma  = 0
    for numero in lista:
        suma += numero
    return suma

#Funsion Promedio
def Promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / 5
    return promedio


#Funsion Minimo
def Minimo(lista): 
    min = lista[0]
    for elemento in range (5):
        if lista[elemento] < min:
            min = lista[elemento]
    os.system("cls")
    print(f"""            ---------------------------------
            |   El numero mas pequeño es: {min} |    
            ---------------------------------""" )    

def Maximo(lista): 
    max = lista[0]
    for elemento in range (5):
        if lista[elemento] > max:
            max = lista[elemento]
    os.system("cls")
    print(f"""            ---------------------------------
            |   El numero mas grande es: {max} |    
            ---------------------------------""" )   

lista = [] #lista vacia 
print ("INGRESE 5 NUMEROS ENTEROS\n")

for  elemento in range(5): #Llena la lista
    lista.append(int(input(f"Ingrese el numero {elemento + 1}: ")))
print()
#Menu de opciones
print ("""            ---------------------------------
            |   ¿QUE DESEA HACER CON ELLOS? |
            ---------------------------------
            |    1 - Sumarlos               |
            |    2 - Obtener Su Promedio    |
            |    3 - Encontrar El Numero    | 
            |        Mas Grande             |      
            |    4 - Encontrar El Numero    | 
            |        Mas Pequeño            |  
            ---------------------------------""")
a = int(input("Ingrese su Opcion: "))
if a == 1:
    print("La suma es igual a: ", Sumar(lista) ) 
elif a == 2:
    print("El Promedio es: ", Promedio(lista))
elif a == 3:
    Maximo(lista)
    #Maximo()
elif a == 4:
    Minimo(lista)#Llama a la funcion minimo y le pasa como argumanto la lista creada

print("\nPresiona la tecla Enter para finalizar el programa.")
input()
print("Gracias por usar nuestro programa.")
