def calcular_algo():
    """
    Esta funcion calcula un area
    """
    
    resultado = 0 #Variable para guardar el reultado
    
    resultado = base * altura
    print("Esto es el area: ", resultado)

base = None #Almacena la base
altura = 0 #Almacena la altura

base = float(input('Ingrese la base: '))
base = float(input('Ingrese la altura: '))

calcular_algo() #Llamo a la funcion


