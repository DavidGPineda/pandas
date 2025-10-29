# Vamos a mostrar 4 gráficos en una sola ventana usando subplots.
# ✅ Ventas por producto
# ✅ Ventas por ciudad
# ✅ Participación (pie chart)
# ✅ Ventas en el tiempo
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Datos
data = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse", "Parlantes", "Monitor"],
    "Precio": [3500, 80, 120, 900, 3500, 80, 200, 900],
    "Cantidad": [1, 3, 2, 1, 2, 1, 1, 2],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá", "Bogotá", "Medellín", "Cali", "Cali"]
}
df = pd.DataFrame(data)
df["Valor_total"] = df["Precio"] * df["Cantidad"]
df["Fecha"] = pd.date_range(start="2025-01-01", periods=len(df), freq="D")

ventas_por_producto = df.groupby("Producto")["Valor_total"].sum()
ventas_por_ciudad = df.groupby("Ciudad")["Valor_total"].sum()
ventas_tiempo = df.groupby("Fecha")["Valor_total"].sum()

# -------- DASHBOARD --------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico 1: barras por producto
axes[0, 0].bar(ventas_por_producto.index, ventas_por_producto)
axes[0, 0].set_title("Ventas por Producto")

# Gráfico 2: barras por ciudad
axes[0, 1].bar(ventas_por_ciudad.index, ventas_por_ciudad, color="orange")
axes[0, 1].set_title("Ventas por Ciudad")

# Gráfico 3: pie chart
axes[1, 0].pie(ventas_por_producto,
               labels=ventas_por_producto.index, autopct="%1.1f%%")
axes[1, 0].set_title("Participación por Producto")

# Gráfico 4: línea en el tiempo
axes[1, 1].plot(ventas_tiempo.index, ventas_tiempo, marker="o")
axes[1, 1].set_title("Ventas en el Tiempo")
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
