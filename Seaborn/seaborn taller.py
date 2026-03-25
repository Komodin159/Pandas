import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid", palette="pastel")
df_ventas = pd.read_csv("datos_completos.csv")
plt.figure(figsize=(8, 5))
sns.countplot(data=df_ventas, x="categoria")
plt.title("Cantidad de transacciones por categoria")
plt.show()
