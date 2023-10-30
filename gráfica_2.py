import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos proporcionados
data = {
    "id": range(1, 21),
    "materia": ["Matemáticas", "Historia", "Ciencias", "Lenguaje"] * 5,
    "nota": [
        80,
        65,
        90,
        75,
        95,
        70,
        85,
        60,
        78,
        82,
        93,
        68,
        73,
        88,
        77,
        50,
        92,
        63,
        85,
        79,
    ],
    "aprobado": [
        "Sí",
        "No",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "No",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "No",
        "Sí",
        "No",
        "Sí",
        "Sí",
    ],
}

df = pd.DataFrame(data)

# Definir el orden de las materias
orden_materias = ["Matemáticas", "Historia", "Ciencias", "Lenguaje"]

plt.figure(figsize=(8, 6))
boxplot = df.boxplot(
    column="nota",
    by="materia",
    boxprops=dict(color="black"),
    medianprops=dict(color="red"),
)
plt.suptitle("Distribución de Notas de Estudiantes por Materia")
plt.title("")
plt.xlabel("Materia")
plt.ylabel("Notas")
plt.grid(True)
plt.xticks(rotation=0)
plt.show()
# Graficar la distribución de aprobados con un pie chart
aprobados = df[df["aprobado"] == "Sí"].shape[0]
no_aprobados = df[df["aprobado"] == "No"].shape[0]

aprobados_percent = (aprobados / (aprobados + no_aprobados)) * 100
no_aprobados_percent = (no_aprobados / (aprobados + no_aprobados)) * 100

labels = "Aprobados", "No Aprobados"
sizes = [aprobados_percent, no_aprobados_percent]
colors = ["dodgerblue", "orangered"]

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.title("Distribución de Aprobados y No Aprobados")
plt.show()
