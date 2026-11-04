# Análisis de Siniestralidad Vial (Reino Unido) - Data Analyst Project

##  Contexto del Proyecto
Este proyecto de análisis exploratorio de datos (EDA) tiene como objetivo identificar los factores que influyen en la gravedad y letalidad de los accidentes de tránsito, utilizando un dataset histórico de ~308,000 registros del Reino Unido. El objetivo final es extraer insights accionables que puedan guiar políticas de seguridad vial.

##  Stack Tecnológico
- **Python (Pandas, Matplotlib):** Limpieza, auditoría y transformación de datos.
- **Power BI:** Modelado de datos (Star Schema), medidas DAX y visualización interactiva.
- **MySQL (Opcional a futuro):** Para manejo de la base de datos relacional.

##  Proceso de Limpieza (Python)
- Se identificó que el 98.2% de la columna `Carriageway_Hazards` estaba nula, por lo que fue eliminada.
- Se imputaron valores nulos menores en variables categóricas (clima, superficie) como 'Unknown'.
- Se estandarizó la columna de tiempo a formato `datetime` y se creó la variable `Franja` (Madrugada, Mañana, Tarde, Noche) para análisis de temporalidad.

##  Modelado (Power BI)
Se implementó un modelo relacional **Uno a Muchos (1:*)**, dejando la tabla de `accidentes_clean` como tabla de hechos única y la tabla `condiciones_clean` como dimensión. Se aplicó el concepto de deduplicación para evitar el doble conteo de víctimas.

##  Principales Insights (Hallazgos)
1. **La trampa del "Buen Clima":** Aunque la mayoría de accidentes ocurren en días despejados (volumen), los días con **viento fuerte ("Fine + high winds") tienen la tasa de letalidad más alta (1.65%)**. La confianza del conductor en condiciones "seguras" incrementa la velocidad y la gravedad del impacto.
2. **El umbral de la velocidad:** La tasa de letalidad muestra una correlación directa con el límite de velocidad, **multiplicándose por más de 4 al pasar de 20 mph a 60 mph**. 
3. **La paradoja de las autopistas (70 mph):** A pesar de los altos límites, la letalidad cae ligeramente en comparación con 60 mph. Esto se debe a la baja frecuencia de accidentes en autopistas (pocos puntos de conflicto) y a la "Ley de los números pequeños", donde menos accidentes totales generan mayor volatilidad estadística en el porcentaje.
4. **El factor horario:** La madrugada concentra la mayor tasa de letalidad, a pesar de tener un volumen total de accidentes mucho menor que la tarde.

##  Recomendaciones de Negocio
- **Enfocar campañas de velocidad** no solo en autopistas, sino en vías urbanas e interurbanas de 40 a 60 mph, donde el volumen de accidentes es alto y la letalidad ya es crítica.
- **Campañas de visibilidad y control de viento** para motociclistas en días aparentemente soleados pero con ráfagas.
- **Operativos de control (alcoholemia/velocidad)** en franjas de madrugada.

---
*Proyecto desarrollado por Edwin Andrés Sánchez Jiménez como parte de su formación en Data Analytics y Desarrollo de Software.*