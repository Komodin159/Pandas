import os

    TOPE_AUXILIO = 2000000
    VALOR_AUXILIO = 160000
    DEDUCCIONES = 0.08 #8%


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_nomina(lista_empleados):
    print("---Nomina General---")

    if not lista_empleados:
        print("No hay empleados")
        return

    print("-" * 75)

    total_nomina = 0

    for emp in lista_empleados:

        sueldo_proporcional =  (emp["Salario"] / 30) * emp["Dias"]
        auxilio = 0

        if emp ["Salario"] > TOPE_AUXILIO:
            auxilio = (VALOR_AUXILIO / 30) * emp["Dias"]

        deducciones = sueldo_proporcional * DEDUCCIONES
        neto = sueldo_proporcional + auxilio + deducciones
        total_nomina += neto

        print("Nombre empleado %s y sueldo %d con un auxilio de: %d" % (emp["Nombre"], sueldo_proporcional, auxilio))

    print("-" * 75)
    print(f"Total empleados: {total_nomina}")
    input("Pressione ENTER para sair...")



if __name__ == "__main__":
    pass