def suma(valor1, valor2):
    "Recibe dos parametros y los suma (+)"

    resultado = 0
    resultado = valor1 + valor2
    print("El resultado es: ", resultado)
    pass 
def multi(valor1, valor2):
    "Recibe dos parametros y los multiplica (*)"

    resultado = 0
    resultado = valor1 * valor2
    print("El resultado es: ", resultado)
    pass
def restar(valor1, valor2):
    "Recibe dos parametros y los resta (-)"

    resultado = 0
    resultado = valor1 - valor2
    print("El resultado es: ", resultado)
    pass
def dividir(valor1, valor2):
    "Recibe dos parametros y los divide (/)"

    resultado = 0
    resultado = valor1 / valor2
    print("El resultado es: ", resultado)
    pass

numero2 = 0
numero1 = 0

mensaje = """
Por favor ingrese la operacion que quiere realizar: 
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
"""

operacion_usuario = 0
operacion_usuario = int(input(mensaje))

numero1 = int(input("Ingrese valor 1: "))
numero2 = int(input("Ingrese valor 2: "))

if operacion_usuario == 1:
    suma(numero1, numero2)
elif operacion_usuario == 2:
    restar(numero1, numero2)
elif operacion_usuario == 3:
    multi(numero1, numero2)
elif operacion_usuario == 4:
    dividir(numero1, numero2)
else:
    print("La opcion ingresada no es valida")
    