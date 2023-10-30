import pandas as pd
import plotly.express as px

# Crear un DataFrame de Pandas con los datos
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

# Gráfico de boxplot para la distribución de notas
materias = df["materia"].unique()
colors = ["purple", "red", "green", "lightpurple"]
fig1 = px.box(
    df,
    x="materia",
    y="nota",
    color="materia",
    title="Distribución de Notas por Materia",
)
fig1.update_xaxes(title_text="Materia")
fig1.update_yaxes(title_text="Nota")
fig1.update_layout(showlegend=False)  # Eliminar la leyenda
fig1.show()

# Gráfico de pastel para la distribución de aprobados
aprobados = df["aprobado"].value_counts()
fig2 = px.pie(
    aprobados,
    values=aprobados.values,
    names=["Aprobado", "No Aprobado"],
    title="Distribución de Aprobados y No Aprobados",
)
fig2.update_traces(textinfo="percent")
fig2.show()
