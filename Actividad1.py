def Minimo(lista): #funsion que calcula el minimo de la litsa
    min = lista[0]
    for elemento in range (5):
        if lista[elemento] < min:
            min = lista[elemento]
    print(f"El elemento menor es: {min}" ) 

lista = [] #lista vacia 
print ("INGRESE 5 NUMEROS ENTEROS")
for  elemento in range(5): #Llena la lista
    lista.append(int(input(f"Ingrese el numero {elemento + 1}: ")))
#Menu de opciones
print ("""Que desa hacer con ellos:
    1 - Sumarlos
    2 - Obtener Su Promedio
    3 - Encontrar El Numero Mas Grande
    4 - Encontrar El Numero Mas Pequeño""")

a = int(input("Ingrese su Opcion: "))
if a == 1:
    suma=sum(lista)
    print=("el resultado de la sumas es: ",suma) #Suma()
elif a == 2:
    print("Aca va la funcion")
    #Promedio()
elif a == 3:
    print("Aca va la funcion")
    #Maximo()
elif a == 4:
    Minimo(lista)#Llama a la funcion minimo y le pasa como argumanto la lista creada
    