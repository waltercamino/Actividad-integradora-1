import os
import time

def Sumar(lista):
    suma  = 0
    for numero in lista:
        suma += numero
    return suma

def Minimo(lista): #funsion que calcula el minimo de la litsa
    min = lista[0]
    for elemento in range (5):
        if lista[elemento] < min:
            min = lista[elemento]
    os.system("cls")
    print(f"""            ---------------------------------
            |   El numero mas pequeño es: {min} |    
            ---------------------------------""" )            
def MenuPrincipal ():
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
            |    0 - Salir                  |
            ---------------------------------""")

<<<<<<< HEAD
    return input("                 Ingrese su Opcion: ")

def CargarLista (lista):
    print ("""            ---------------------------------
            |   INGRESE 5 NUMEROS ENTEROS   |
            ---------------------------------""")
    for  elemento in range(5): #Llena la lista
        lista.append(int(input(f"                  Ingrese el numero {elemento + 1}: ")))

lista = [] #lista bacia 
CargarLista(lista)
while True:
    os.system("cls")
    a = MenuPrincipal ()
    if a == "1":
        os.system("cls")
        print(F"""        ---------------------------------------------------------
        |   La suma de los numeros ingresados es igual a: {Sumar(lista)}    |
        ---------------------------------------------------------""")
        time.sleep(5)#detener para que se vea resultado
    elif a == "2":
        print("Aca va la funcion")
        #Promedio()
    elif a == "3":
        print("Aca va la funcion")
        #Maximo()
    elif a == "4":
        Minimo(lista)#Llama a la funcion minimo y le pasa como argumanto la lista creada
        time.sleep(5)#detener para que se vea el resultado
    elif a == "0":
        os.system("cls")
        print ("""        -----------------------------------------
        | ¡¡GRACIAS POR USAR NUESTRO PROGRAMA!! |
        -----------------------------------------""")
        break
    else: 
        os.system("cls")
        print ("""                  ----------------------
                  | OPCION NO ADMITIDA |
                  ----------------------""")
        time.sleep(5)          
=======
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
    n= int(input("ingrese la cantidad de notas a promediar"))
    suma=0
    i=1
    while(i<= n):
        print("ingrese la nota numero:",i)
        nota=float(input())
        suma=suma+nota
        i+=1
        prom = suma/n
        print("El promedio de notas es:",prom)
        
    #Promedio()
elif a == 3:
    print("Aca va la funcion")
    #Maximo()
elif a == 4:
    Minimo(lista)#Llama a la funcion minimo y le pasa como argumanto la lista creada
>>>>>>> 361e4dc221166e46068164bc9681604ecc58b62a
