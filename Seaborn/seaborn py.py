import pandas as pd
import numpy as np
import random

# Configuración de aleatoriedad para que los datos sean coherentes
np.random.seed(42)

# Listas de datos para la simulación
vendedores = ['Andrés', 'Beatriz', 'Carlos', 'Diana', 'Elena']
categorias = ['Tecnología', 'Hogar', 'Oficina', 'Deportes']
productos = {
 'Tecnología': ['Laptop', 'Mouse Gamer', 'Monitor 4K', 'Teclado Mecánico'],
 'Hogar': ['Cafetera', 'Lámpara LED', 'Aspiradora Robot', 'Licuadora'],
 'Oficina': ['Silla Ergonómica', 'Escritorio', 'Agenda', 'Organizador'],
 'Deportes': ['Mancuernas', 'Mat de Yoga', 'Botella Térmica', 'Bicicleta']
}
meses = ['Enero', 'Febrero', 'Marzo']

data = []

for _ in range(300):
 cat = random.choice(categorias)
 prod = random.choice(productos[cat])
 vendedor = random.choice(vendedores)
 mes = random.choice(meses)
 # Lógica de precios según categoría
 if cat == 'Tecnología': precio_base = random.uniform(50, 800)
 elif cat == 'Hogar': precio_base = random.uniform(20, 150)
 else: precio_base = random.uniform(10, 100)
 cantidad = random.randint(1, 10)
 total = round(precio_base * cantidad, 2)
 data.append([mes, vendedor, cat, prod, round(precio_base, 2), cantidad, total])

# Crear DataFrame
df = pd.DataFrame(data, columns=['mes', 'vendedor', 'categoria', 'nombre', 'precio', 'cantidad', 'Total_Ingreso'])

# Añadir algunos OUTLIERS para el ejercicio de Boxplot (Ventas inusualmente altas)
df.loc[0] = ['Marzo', 'Andrés', 'Tecnología', 'Servidor Enterprise', 5000, 1, 5000]
df.loc[1] = ['Enero', 'Elena', 'Deportes', 'Gimnasio Completo', 3500, 1, 3500]

# Guardar
df.to_csv("datos_completos.csv", index=False)
print("Archivo 'datos_completos.csv' generado con éxito.")