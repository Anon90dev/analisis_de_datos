import pandas as pd
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Obtener la ruta desde la variable de entorno
ruta = os.getenv("RUTA_DATOS")
base = os.getenv("base_01")
print(f"Ruta de la variable del entorno: {ruta}")
print(f"Nombre de la base de datos: {base}")

# Definir la ruta completa del archivo que se va a leer
archivo = ruta + "/" + base

# Mostrar el contenido de la información que vamos a mostrar
df = pd.read_csv(archivo)
print(df)