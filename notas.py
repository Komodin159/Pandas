def notas(nota):

    if nota >= 40 and nota <= 50:
        print("Excelente")
    elif nota >= 30 and nota <= 39:
        print("Aprobo")
    elif nota >= 29 and nota <= 0:
        print("Reprobado")
    else:
        print("Invalido")
        return

nota = int(input("Ingrese su nota\n"))
notas(nota)
