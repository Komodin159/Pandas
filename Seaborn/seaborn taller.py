from statistics import correlation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid", palette="pastel")
df_ventas = pd.read_csv("datos_completos.csv")
plt.figure(figsize=(8, 5))
sns.countplot(data=df_ventas, x="categoria")
plt.title("Cantidad de transacciones por categoria")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df_ventas, x="vendedor", y="Total_Ingreso", estimator=sum)
plt.title("Cantidad de transacciones por categoria")
plt.show()

df_numero = df_ventas[['precio', 'cantidad', 'Total_Ingreso']]
correlacion = df_numero.corr()

plt.figure(figsize=(8, 5))
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Matriz de correlacion")
plt.show()

resumen = df_ventas.groupby('vendedor')["Total_Ingreso"].sum().reset_index()
resumen = resumen.sort_values(by=['Total_Ingreso'], ascending=False)

tabla_html = resumen.to_html(classes="table table-striped", index=False)
codigo_html = f""" 
<!DOCTYPE html> 
<html> 
<head> 
 <title>Reporte de Ventas</title> 
 <style> 
 body {{ font-family: Arial, sans-serif; margin: 40px; }} 
 h1 {{ color: #2C3E50; }} 
 .table {{ width: 50%; border-collapse: collapse; margin-top: 20px; }} 
 .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }} 
 .table th {{ background-color: #4CAF50; color: white; }} 
 </style> 
</head> 
<body> 
 <h1>Reporte Ejecutivo de Ventas 2026</h1> 
 <p>A continuación se presenta el rendimiento del equipo comercial:</p> 

 <!-- Aquí inyectamos la variable de Python que tiene la tabla --> 
 {tabla_html} 

</body> 
</html> 
"""

# Guardar el string en un archivo real
with open("reporte_final.html", "w", encoding="utf-8") as archivo:
 archivo.write(codigo_html)

print("¡Página web generada con éxito! Abre 'reporte_final.html' en tu navegador.")