listaTest = [1, 2, "Hola Mundo", 0.9, True] #Lista
tuplaTest = (1, 2, 3) #Tupla, no se puede modificar
diccionario = {"Nombre": "Camilo",
               "Edad": 20, #Diccionario 
               "Correo": "test@test.com"}

print(listaTest[3]) #Hola Mundo
print(tuplaTest[2]) #3

print("Imprimir lista")
for i  in listaTest: 
    print(i)

print("Imprimir Tupla")
for i  in tuplaTest: 
    print(i)

print("Imprimir Diccionario")
for clave, valor in diccionario.items(): 
    print(f"Esta es la clave {clave} y este el valor {valor}")

print("---Impimiendo lista con WHILE---")
tamanoLista = len(listaTest)
contador = 0
while (contador < tamanoLista):
    print(listaTest[contador])
    contador += 1

print("---Impimiendo lista con WHILE---")
claves = list(diccionario.keys())
lenClaves = len (claves)
i = 0
while (i < lenClaves):
    print("Esta es mi clave: ", claves[i])
    print(f"Este es el valor de mi cale{diccionario[claves[i]]}")
    i += 1

print("---Convirtiendo texto a lista---")
texto = "Hola mundo, bienenidos"
print(list(texto))

print("Trabajando con lista")
frutas = ["Pera","Manzana","Fresas","Banana","Uva"]
print(frutas[2]) #Fresa
print(frutas[0:2]) #[Pera, Manzanas]
print(frutas[-1]) #Uva
print(frutas[-1:]) #[Uva]
print(frutas[:-1]) #"Pera","Manzana","Fresas","Banana","Uva"
print(frutas[::2]) #"Pera","Fresas","Uva" Cada 2 elementos

frutas.pop()
print("Quitamos un elemento")
print(frutas)
print("Agregamos un elemento")
frutas.append("Mora")
print(frutas)
print("Quito un elemento por indice")
frutas.pop(1) #Quita el elemento por posicion
print(frutas)
print("Quito elemento por nombre")
frutas.remove("Fresas")
print(frutas)
print("Agregar elemeto")
frutas.insert(1, "Guanabana")
print(frutas)
print("Modificar elemento por posicion")
frutas[1] = "Kiwi"
print(frutas)

diccionario["Edad", "Correo"] = 25, "correo@correo"
print(diccionario)