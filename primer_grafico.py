import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")  # Cambia estilo visual
# plt.style.use("seaborn-v0_8")
# plt.style.use("fivethirtyeight")
# plt.style.use("bmh")
# plt.style.use("dark_background")
# plt.style.use("Solarize_Light2")


# Datos de ejemplo
data = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse", "Parlantes", "Monitor"],
    "Precio": [3500, 80, 120, 900, 3500, 80, 200, 900],
    "Cantidad": [1, 3, 2, 1, 2, 1, 1, 2],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá", "Bogotá", "Medellín", "Cali", "Cali"]
}

df = pd.DataFrame(data)

# Crear columna "Valor_total"
df["Valor_total"] = df["Precio"] * df["Cantidad"]

# Agrupar ventas totales por producto
ventas_por_producto = df.groupby("Producto")["Valor_total"].sum()

# # --- GRAFICO ---
plt.figure(figsize=(8, 5))
ventas_por_producto.plot(
    kind="bar", color=["#FF5733", "#33C1FF", "#DAF7A6", "#FFC300", "#C70039"])
plt.title("Ventas Totales por Producto", fontsize=14)
plt.xlabel("Producto")
plt.ylabel("Valor Total ($)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("ventas_por_producto.png")
plt.show()

# --- Ventas totales por ciudad ---
ventas_por_ciudad = df.groupby("Ciudad")["Valor_total"].sum()

# # --- GRAFICO ---
# plt.figure(figsize=(8, 5))
# ventas_por_ciudad.plot(kind="bar", color="orange")
# plt.title("Ventas Totales por Ciudad")
# plt.xlabel("Ciudad")
# plt.ylabel("Valor Total ($)")
# plt.grid(axis="y")
# plt.show()

# ✅ Paso 3: Gráfico Circular (Pie Chart)
# --- Gráfico circular: participación por producto ---
# plt.figure(figsize=(7, 7))
# ventas_por_producto.plot(
#     kind="pie",
#     autopct="%1.1f%%",
#     startangle=90
# )
# plt.title("Participación de Ventas por Producto")
# plt.ylabel("")  # Oculta etiqueta innecesaria
# plt.show()

# ✅ Paso 4: Gráfico de Línea (ventas acumuladas en el tiempo)

# --- Simular fechas de ventas ---
# df["Fecha"] = pd.date_range(start="2025-01-01", periods=len(df), freq="D")

# --- Ordenar por fecha ---
# df = df.sort_values("Fecha")

# --- Calcular ventas acumuladas ---
# ventas_tiempo = df.groupby("Fecha")["Valor_total"].sum()

# plt.figure(figsize=(8, 5))
# ventas_tiempo.plot(kind="line", marker="o")
# plt.title("Ventas en el tiempo")
# plt.xlabel("Fecha")
# plt.ylabel("Valor Total ($)")
# plt.grid()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# ✅ Paso 6: Guardar gráficas como imágenes 🖼️
# Antes de cualquier plt.show()
# plt.savefig("ventas_por_producto.png")
