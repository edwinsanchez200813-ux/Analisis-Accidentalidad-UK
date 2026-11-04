import pandas as pd
import matplotlib.pyplot as plt

# 1. CARGA
df = pd.read_excel("OriginalRoadAccidentData.xlsx") # O el nombre de tu archivo
print(f"Filas originales: {len(df)}")

# 2. LIMPIEZA
df = df.drop(columns=['Carriageway_Hazards'])
df = df.dropna(subset=['Time'])
df['Time'] = df['Time'].astype(str).str.strip()
df['Time'] = pd.to_datetime(df['Time'], errors='coerce').dt.time

# 3. CREACIÓN DE LA HORA Y LA FRANJA
df['Hour'] = pd.to_datetime(df['Time'].astype(str), format='%H:%M:%S', errors='coerce').dt.hour
if df['Hour'].isnull().sum() > 1000:
    df['Hour'] = pd.to_datetime(df['Time'].astype(str), format='%H:%M', errors='coerce').dt.hour

def obtener_franja(hora):
    if pd.isna(hora): return 'Desconocido'
    if 0 <= hora <= 5: return 'Madrugada'
    if 6 <= hora <= 11: return 'Mañana'
    if 12 <= hora <= 17: return 'Tarde'
    return 'Noche'

df['Franja'] = df['Hour'].apply(obtener_franja)

# 4. EXPORTACIÓN PARA POWER BI (El código de la ronda anterior)
cols_accidentes = ['Accident_Index', 'Accident Date', 'Time', 'Hour', 'Franja', 'Accident_Severity', 
                   'Number_of_Casualties', 'Number_of_Vehicles', 'Speed_limit', 'Latitude', 'Longitude']
df_accidentes = df[cols_accidentes].copy()

cols_condiciones = ['Accident_Index', 'Weather_Conditions', 'Road_Surface_Conditions', 'Light_Conditions', 'Urban_or_Rural_Area', 'Road_Type']
df_condiciones = df[cols_condiciones].copy()

# En tu script de Python, cambia las líneas de exportación por estas:
df_accidentes.to_csv('accidentes_clean.csv', index=False, encoding='utf-8-sig')
df_condiciones.to_csv('condiciones_clean.csv', index=False, encoding='utf-8-sig')
print("Archivos exportados con éxito.")

# ¿Cuántos Accident_Index únicos hay?
print("Total filas:", len(df_condiciones))
print("Accident_Index únicos:", df_condiciones['Accident_Index'].nunique())