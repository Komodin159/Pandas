def calcular ( valor1, valor2, parametro):

    resultado = 0
    
    if parametro == "+":
        resultado = valor1 + valor2
    elif parametro == "-":
        resultado = valor1 - valor2
    elif parametro == "*":
        resultado = valor1 * valor2
    elif parametro == "/":
        resultado = valor1 / valor2
    else: 
        print("El parametro ingresado no es valido.")
        #return "NO"
    
    print("El resultado de la operacion es: ", resultado)
    #return "OK"

numero1 = 0
numero2 = 0
parametro = ""

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese el segundo numero a operar: "))

mensaje = """
    Ingrese el simbolo de la operacion que quiere realizar: 
Sumar: +
Restar: -
Multiplicar: * 
Dividir: /
"""

parametro = input(mensaje)
""" 
variableentrada= "SI" """

""" while (variableentrada != "ok"):
    parametro = input(mensaje)
    variableentrada = calcular(numero1, numero2, parametro) """

for i in range (1,5):
        numero1 = int(input("Ingrese el numero: "))
        numero2 = int(input("Ingrese el segundo numero a operar: "))
        parametro = input(mensaje)

calcular (numero1, numero2, parametro)