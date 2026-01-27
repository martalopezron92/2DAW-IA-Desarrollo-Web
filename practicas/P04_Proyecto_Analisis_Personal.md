# P04 - Proyecto de análisis de datos personalizados

## 📋 Información general

- **Unidad**: U4 - Pandas y análisis de datos
- **Bloque**: B2 - Fundamentos técnicos
- **Modalidad**: Individual
- **Entrega**: Repositorio códigos + presentación de resultados

## Objetivos

Al completar esta práctica, el estudiante será capaz de:

- **Crear** datasets personalizados basados en información real
- **Aplicar** técnicas de limpieza y manipulación de datos con Pandas
- **Calcular** estadísticas descriptivas e inferir patrones
- **Visualizar** información de forma efectiva con Matplotlib/Seaborn
- **Documentar** hallazgos y conclusiones técnicas
- **Presentar** resultados de análisis de forma profesional

## Descripción de la práctica

### Contexto

Esta práctica te permite aplicar todo lo aprendido sobre análisis de datos a un tema de tu interés personal. Deberás crear tu propio dataset, limpiarlo, analizarlo y extraer conclusiones significativas.

### Opciones de proyecto

Elige **UNA** de las siguientes opciones:

#### Opción A: Análisis de tu música

**Objetivo:** Analizar tus gustos musicales mediante un dataset personalizado

**Dataset requerido:**
- Mínimo 20 canciones de tu biblioteca personal
- Columnas obligatorias:
  - `artista` (str): Nombre del artista o banda
  - `cancion` (str): Título de la canción
  - `genero` (str): Género musical
  - `duracion` (int): Duración en segundos
  - `año` (int): Año de lanzamiento
  - `puntuacion` (float): Tu puntuación personal (0-10)
  - `reproducciones` (int): Número de veces que la has escuchado (opcional)
  - `album` (str): Nombre del álbum (opcional)

**Análisis sugerido:**
- ¿Qué géneros musicales predominan en tus gustos?
- ¿Hay relación entre el año de lanzamiento y tu puntuación?
- ¿Cuál es la duración promedio de tus canciones favoritas?
- ¿Tus artistas más escuchados?

#### Opción B: Análisis de videojuegos

**Objetivo:** Analizar tu historial y preferencias de videojuegos

**Dataset requerido:**
- Mínimo 20 videojuegos que hayas jugado
- Columnas obligatorias:
  - `nombre` (str): Título del juego
  - `plataforma` (str): PC, PlayStation, Xbox, Switch, etc.
  - `genero` (str): RPG, FPS, Strategy, etc.
  - `año` (int): Año de lanzamiento
  - `horas_jugadas` (float): Horas que has invertido
  - `puntuacion` (float): Tu puntuación personal (0-10)
  - `desarrolladora` (str): Estudio desarrollador (opcional)
  - `completado` (bool): Si has completado el juego (opcional)

**Análisis sugerido:**
- ¿Qué géneros de juegos prefieres?
- ¿Cuántas horas inviertes en promedio por juego?
- ¿Relación entre horas jugadas y tu puntuación?
- ¿Plataforma favorita?

#### Opción C: Análisis de series

**Objetivo:** Analizar tus hábitos de visualización de series

**Dataset requerido:**
- Mínimo 20 series que hayas visto (completas o en progreso)
- Columnas obligatorias:
  - `titulo` (str): Nombre de la serie
  - `genero` (str): Drama, Comedia, Thriller, etc.
  - `temporadas` (int): Número total de temporadas
  - `capitulos_vistos` (int): Capítulos que has visto
  - `puntuacion` (float): Tu puntuación personal (0-10)
  - `año_inicio` (int): Año de estreno
  - `plataforma` (str): Netflix, HBO, Amazon Prime, etc. (opcional)
  - `estado` (str): Completada, En progreso, Abandonada (opcional)

**Análisis sugerido:**
- ¿Qué géneros de series ves más?
- ¿Cuál es tu plataforma de streaming favorita?
- ¿Terminas las series que empiezas?
- ¿Relación entre número de temporadas y tu puntuación?

## Requisitos técnicos

### 1. Dataset (20 puntos)

- ✅ **Mínimo 15 registros** (recomendado 20+)
- ✅ **Mínimo 5 columnas** con datos relevantes
- ✅ Datos **reales y veraces** sobre tus gustos
- ✅ Formato CSV con codificación UTF-8
- ✅ Nombres de columnas descriptivos y en minúsculas

### 2. Limpieza de datos (15 puntos)

Documenta y ejecuta en tu notebook:
- ✅ Verificación de tipos de datos (`dtypes`)
- ✅ Identificación y tratamiento de valores nulos
- ✅ Detección de duplicados
- ✅ Normalización de datos (si aplica)
- ✅ Conversión de tipos de datos (si necesario)

**Código esperado:**
```python
# Ejemplo de limpieza
df.info()
df.isnull().sum()
df.duplicated().sum()
df['columna'] = df['columna'].astype('tipo_correcto')
```

### 3. Análisis estadístico (25 puntos)

Calcula **al menos 5 estadísticas diferentes**, incluyendo:

**Obligatorias:**
- Estadísticas descriptivas básicas (`describe()`)
- Medias, medianas o modas relevantes
- Conteo de valores por categoría (`value_counts()`)

**Adicionales (elige al menos 2):**
- Correlaciones entre variables numéricas
- Agrupaciones con `groupby()`
- Ranking de top elementos
- Porcentajes y proporciones
- Comparaciones entre grupos


### 4. Visualizaciones (25 puntos)

Crea **al menos 3 gráficos diferentes**, incluyendo:

**Tipos de gráficos requeridos (mínimo 3 diferentes):**
- Gráfico de barras (`bar` o `barh`)
- Histograma (`hist`)
- Gráfico de dispersión (`scatter`)
- Gráfico de caja (`boxplot`)
- Gráfico de líneas (`plot`)
- Gráfico circular (`pie`)

**Requisitos de calidad:**
- Títulos descriptivos
- Etiquetas en ejes X e Y
- Leyendas cuando sea necesario
- Colores apropiados y legibles
- Tamaño de figura adecuado

### 5. Conclusiones y documentación (15 puntos)

Incluye en el README de tu repositorio:
- **Introducción:** Describe qué vas a analizar y por qué
- **Metodología:** Explica cómo recopilaste los datos
- **Hallazgos:** Interpreta cada análisis y gráfico
- **Conclusiones finales:** Resume los insights más importantes
- **Código comentado:** Explica secciones clave del código

**Estructura recomendada del documento:**
```markdown
# 1. Introducción
# 2. Carga y exploración inicial de datos
# 3. Limpieza de datos
# 4. Análisis estadístico
# 5. Visualizaciones
# 6. Conclusiones
```

## Entregables

### Archivos requeridos:

1. **`dataset_[tema].csv`**
   - Tu dataset original en formato CSV
   - Ejemplo: `dataset_musica.csv`, `dataset_videojuegos.csv`

2. **`analisis_[nombre].py`**
   - Código ejecutable y bien comentado

3. **`requirements.txt`**
   - Lista de librerías utilizadas con versiones
   - Generado con `pip freeze > requirements.txt`

4. **`README.md`** 
   - Breve descripción del proyecto
   - Principales conclusiones

### Formato de entrega:

Enlace del repositorio de GITHUB


## Criterios de evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Dataset** | 20 | Calidad, cantidad y relevancia de los datos |
| **Limpieza** | 15 | Proceso de limpieza documentado y ejecutado |
| **Estadísticas** | 25 | Variedad y profundidad de análisis realizados |
| **Visualizaciones** | 25 | Calidad, variedad e interpretación de gráficos |
| **Documentación** | 15 | Claridad, estructura y conclusiones |
| **TOTAL** | **100** | |
