import pandas as pd
import numpy as np
import random

# Definir posibles valores para columnas categóricas
sexos = ["Masculino", "Femenino", "Otro"]
educacion = ["Primaria", "Secundaria", "Universidad", "Postgrado"]

# Generar datos simulados
np.random.seed(42)  # para reproducibilidad
random.seed(42)

n = 150
data = {
    "ID": range(1, n + 1),
    "Edad": np.random.randint(18, 65, size=n),
    "Sexo": [random.choice(sexos) for _ in range(n)],
    "Ingresos": np.random.normal(loc=4000, scale=1500, size=n).round(2),
    "Educación": [random.choice(educacion) for _ in range(n)],
    "Puntaje_credito": np.random.randint(300, 851, size=n),
    "Compró_producto": np.random.choice([0, 1], size=n, p=[0.6, 0.4])
}

df = pd.DataFrame(data)

# Guardar como archivo CSV (opcional)
df.to_csv("datos_practica_ml.csv", index=False)

# Ver primeras filas
print(df.head())
