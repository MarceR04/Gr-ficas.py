import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, label="Estudiantes", color="b", marker="o")
plt.xlabel("Calificaciones de Matemáticas")
plt.ylabel("Calificaciones de Ciencias")
plt.title("Gráfico de Dispersión: Matemáticas vs. Ciencias")
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de barras de error
materias = ["Matemáticas", "Ciencias", "Literatura"]
promedios = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

fig, ax = plt.subplots(figsize=(8, 6))
x = np.arange(len(materias))
ax.bar(
    x,
    promedios,
    yerr=np.transpose(errores),
    align="center",
    alpha=0.7,
    ecolor="black",
    capsize=10,
)
ax.set_xlabel("Materias")
ax.set_ylabel("Calificaciones Promedio")
ax.set_title("Gráfico de Barras de Error: Calificaciones Promedio por Materia")
ax.set_xticks(x)
ax.set_xticklabels(materias)
ax.legend(["Calificaciones Promedio"])
plt.grid(True)
plt.show()

# Histograma de Matemáticas
plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, edgecolor="black", alpha=0.7, color="skyblue")
plt.xlabel("Calificaciones de Matemáticas")
plt.ylabel("Frecuencia")
plt.title("Histograma de Calificaciones de Matemáticas")
plt.grid(True)
plt.show()
