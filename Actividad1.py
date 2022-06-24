from distutils.command.clean import clean
from re import X
from unittest import result


def Minimo(lista): #funsion que calcula el minimo de la litsa
    min = lista[0]
    for elemento in range (5):
        if lista[elemento] < min:
            min = lista[elemento]
    print(f"El elemento menor es: {min}" ) 

def Sumar(lista):
    suma=0
    for numero in lista:
        suma += numero
    return suma

lista = [] #lista vacia 
print ("INGRESE 5 NUMEROS ENTEROS\n")

for  elemento in range(5): #Llena la lista
    lista.append(int(input(f"Ingrese el numero {elemento + 1}: ")))
print()
#Menu de opciones
print ("""Que desa hacer con ellos:
    1 - Sumarlos
    2 - Obtener Su Promedio
    3 - Encontrar El Numero Mas Grande
    4 - Encontrar El Numero Mas Pequeño\n""")

a = int(input("Ingrese su Opcion: "))
if a == 1:
    print()
    print("La suma de los numeros ingresados es igual a: ",Sumar(lista)) 
    #Suma()
elif a == 2:
    print("Aca va la funcion")
    #Promedio()
elif a == 3:
    print("Aca va la funcion")
    #Maximo()
elif a == 4:
    Minimo(lista)#Llama a la funcion minimo y le pasa como argumanto la lista creada