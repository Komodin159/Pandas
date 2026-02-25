def main():
    print("Inicio el programa")
    notas = []

    try:

        for i in range(1, 4):
            print("Paso", i)
            nota = float(input("Introduce una nota:\n"))
            notas.append(nota)


            if nota <3.0:
                print("Reprobo")
            elif nota >= 3.0 and nota <= 5.0:
                print("Aprobo")
            else :
                print("Ingrese un valor diferente")

        print("Estas son las notas:", notas)

        tamañoLista = len(notas)
        contador = 0
        sumaNotas = 0

        while(contador < tamañoLista):
            notawhile = notas[contador]
            sumaNotas += notawhile
            contador += 1

        print("Su promedio es:" , sumaNotas/tamañoLista)
    except Exception as e:
        print("El pragrama tiene algun fallo", e)
    finally:
        print("El programa finalizo")

if __name__ == "__main__":
    main()