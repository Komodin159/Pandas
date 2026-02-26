def saludo (nombre):
    print("hola mundo", nombre)

saludo("camilo")
saludo("juan")

for numero in range (1,3):
    print (numero)
    print ("-----------------------------------------")

    nombre = input("Ingrese su nombre")
    if nombre.lower().strip()== "salir":
        break
    saludo(nombre)

while (True):
    print("Aqui inica el while")
    nombre = input("Ingrese su nombre")
    if nombre.upper().strip == "SALIR":
        break

    saludo(nombre)