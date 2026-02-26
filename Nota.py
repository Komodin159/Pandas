estudiante = [
    {"Nombre": "Andres", "Notas": [3.0, 4.5, 4.0]},
    {"Nombre": "Maria", "Notas": [4.0, 5.0, 3.5]},
    {"Nombre": "Fabio", "Notas": [3.6, 2.2, 2.5]},
]

print("--- Datos cargados ---")
print(f"Total de estudiantes: {len(estudiante)}")

def reporte(estudiantes):
    print("--- Reporte Final ---")
    for est in estudiantes:
        suma = sum(est["Notas"])
        promedio = suma / len(est["Notas"])

        if promedio >= 3.0:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"Estudiante: {est["Nombre"]} su estado es: {estado}")

reporte(estudiante)