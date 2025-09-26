import pandas as pd
import json
from datetime import datetime

# Ruta de tu archivo Excel
file_path = "./pubschls.xlsx"

# Leer el Excel
df = pd.read_excel(file_path)

# Filtrar solo las escuelas con StatusType = "Active"
df = df[df['StatusType'] == 'Active']

# Seleccionar solo las columnas específicas que necesitamos
columns_to_keep = [
    'StatusType', 'County', 'District', 'School', 'Street', 'StreetAbr', 
    'City', 'Zip', 'State', 'MailStreet', 'MailStrAbr', 'MailCity', 
    'MailZip', 'MailState', 'AdmFName', 'AdmLName'
]
df = df[columns_to_keep]

# Convertir fechas/timestamps a strings para que sean JSON serializable
for col in df.columns:
    if df[col].dtype == 'datetime64[ns]' or pd.api.types.is_datetime64_any_dtype(df[col]):
        df[col] = df[col].astype(str)

# Convertir cada fila en un diccionario
records = df.to_dict(orient="records")

# Convertir en JSON
json_output = json.dumps(records, indent=2, ensure_ascii=False, default=str)

# Guardar en archivo (opcional)
with open("pubschls.json", "w", encoding="utf-8") as f:
    f.write(json_output)

print(json_output)
