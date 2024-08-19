#--------------EJERCICIO 1: NUMEROS Y CADENAS DE CARACTERES--------------
"""
#1-
n1 = int(input(("Ingrese un numero entero: ")))
n2 = int(input(("Ingrese otro numero entero: ")))
#Le puse el INT delante para que el numero no sea de tipo string sino de tipo entero.
print("La suma de ambos numeros es", n1+n2)
print("El producto de ambos numeros es",n1*n2)
print("La concatenacion de ambos numeros es",str(n1)+str(n2)) 
#Le puse STR adelante de cada variable para castearlo y sea de tipo string y asi poder concatenarlo.

#2-
texto = input("Ingrese una cadena de texto: ")
print(texto.upper()) #MAYUSCULA
print(texto.__len__()) #TAMAÑO DE LA CADENA 
print(texto[::-1]) #CADENA INVERTIDA
#El primer : toma la cadena desde el principio hasta el final.
#El segundo : indica que el final esta incluido. 
#El -1 significa "recorrer la cadena en dirección inversa".
letra = input("Indica qué letra quieres contar: ") #CANT VECES QUE APARECE UNA LETRA
print(f"La letra {letra} aprece {texto.count(letra)} veces en el texto. ")

#4-
cantRepeticiones = int(input("Ingrese la cantidad de veces a repetir la cadena: "))
for i in range (cantRepeticiones):
    print(texto)
"""
#------------------------EJERCICIO 2: LISTAS Y TUPLAS--------------------------
"""
#1-
lista =["manzana","naranja","banana"]
lista.append("frutilla")
lista.append("kiwi")
lista.sort()
print(lista)
lista.remove("manzana")
print(lista)

#2-
tupla = ("Paris","Madrid")
print("El primer elemento de la tupla es:",tupla[0]) #DEVUELVE EL PRIMER ELEMENTO
print("El ultimo elemento de la tupla es:",tupla[-1]) #DEVUELVE EL ULTIMO ELEMENTO
deTupla_a_lista = list(tupla) 
deTupla_a_lista.append("Buenos Aires")
print(deTupla_a_lista) 

#3-
numeros = [1,2,3,4,5]
suma=0
#ME DEVUELVE EL MAYOR NUMERO DE LA LISTA
for i in range (len(numeros)):
    num = numeros[0]
    if numeros[i] > num:
        num = numeros[i]
print(num)

#ME DEVUELVE EL MENOR NUMERO DE LA LISTA
for i in range (len(numeros)):
    num = numeros[0]
    if numeros[i] < num:
        num = numeros[i]
print(num)

#ME DEVUELVE EL PROMEDIO DE LA LISTA
for i in range (len(numeros)):
    suma+= numeros[i]
print(suma/len(numeros))

#4-
lista_cadenas=["hola","como","estas"]

def lista_minusc_a_mayusc(lista):
    for cadena in lista:
        print(cadena.upper())
        
lista_minusc_a_mayusc(lista_cadenas)
"""
#---------------------EJERCICIO 3: CONTROLADORES DE FLUJO--------------------
"""
#1-
def esPar (num):
    if num % 2 == 0:
        return True
    else:
        return False 

print(esPar(8))
#2-
def saludos ():
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    #Uso un bucle while True para mostrar el menú y pedirle la opción al usuario hasta que elija la opción 3 y sale.
    while True :
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
         print("¡Hola! ¿Cómo estás?")  
        elif opcion == 2:
            print("¡Adiós! Que tengas un buen día.")
        elif opcion == 3:
            print("Saliendo del programa.") 
            break #Finaliza el bucle
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
 
saludos() #Llamo a la funcion 

#4
def determinar_positividad():
    num = int(input("Ingrese un numero +, - ó 0: "))
    salida = "Es Positivo" #Si no es cero ni negativo entonces la salida no cambia y la unica opcion que queda es que sea positivo.
    if num == 0:
        salida = "Es Cero"
    if num < 0:
        salida = "Es negativo"
    return salida 

print(determinar_positividad()) #Llamo a la funcion

def num_del_1_al_10 ():
    for i in range (10):
        print(i+1) #Le sume 1 porque bucle arranca desde el 0

num_del_1_al_10()

def suma_del_1_al_100():
   suma = 0
   numero = 1 
   while numero <= 100:
        suma += numero
        numero += 1
   return suma
        
print(suma_del_1_al_100())      

"""
#-----------------------EJERCICIO 4: CONJUNTOS Y DICCIONARIOS---------------------
"""
#1-
c1 = {1,2,3,4}
c2 = {2,4,6,8}
print(c1.union(c2))
print(c1.difference(c2))
print(c1.intersection(c2))

#2-
edades = {"juan":26,"ana":15,"benicio":58}
print(edades[list(edades.keys())[0]]) 
# Lo que esta dentro de los corchetes me devuelve la primer clave del diccionario
# Y luego hace edades["juan"] y me devuelve lo que esa asociado a juan que es 26
edades["carlos"] = 35
print(edades)
print(edades.pop("benicio"))
print(edades)

#3-
precios = {"shampoo":100, "jabon":50, "gaseosa":155, "pan":60, "queso":48}
print(precios.get("jabon"))
print(precios)
for p in precios:
    precios[p]+= precios[p]*0.1 
    #A lo que tiene precios en el valor de p 
    #Le sumo a el mismo mas el 10 porciento 
print(precios) 

#4-
c1 = {1,2,3,4,5}
c2 = {4,5,6,7,8}
print(c1.intersection(c2))
print(c1.symmetric_difference(c2))
"""
#-------------------------EJERCICIO 5: FUNCIONES---------------------------------
"""
#1-
def saludar(nombre):
    print("HOLA", nombre.upper(),"QUE GUSTO QUE VUELVAS!" )
saludar("Belen")

#2-
def suma(a,b):
    return a + b
print(suma(10,50))
print(suma(15,25))

#3-
def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False
print(esMayorDeEdad(5))
print(esMayorDeEdad(18))
print(esMayorDeEdad(50))
"""