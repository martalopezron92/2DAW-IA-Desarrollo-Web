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

### 6. Presentación de resultados (20 puntos)

Deberás crear una presentación que resuma tu proyecto y hallazgos principales. Esta presentación simula la exposición de resultados ante un equipo técnico.

**Requisitos de la presentación:**

#### Contenido obligatorio:
- ✅ **Portada** (1 diapositiva)
  - Título del proyecto
  - Tu nombre y fecha
  - Tema elegido (música/videojuegos/series)

- ✅ **Introducción** (1-2 diapositivas)
  - Objetivo del análisis
  - Descripción del dataset (número de registros, columnas principales)
  - Metodología de recopilación de datos

- ✅ **Proceso técnico** (2-3 diapositivas)
  - Resumen del proceso de limpieza de datos
  - Código Python clave utilizado (snippets importantes)
  - Tecnologías y librerías empleadas

- ✅ **Resultados del análisis** (3-5 diapositivas)
  - Principales estadísticas encontradas
  - Visualizaciones más relevantes (gráficos del análisis)
  - Interpretación de resultados

- ✅ **Conclusiones** (1-2 diapositivas)
  - Insights más interesantes descubiertos
  - Reflexión personal sobre los hallazgos
  - Limitaciones y posibles mejoras futuras

- ✅ **Aspectos técnicos** (1 diapositiva)
  - Resumen de técnicas de Pandas utilizadas
  - Desafíos técnicos encontrados y cómo se resolvieron

**Requisitos de formato:**
- 📊 **Extensión:** 8-12 diapositivas
- 💻 **Formato:** PDF, PowerPoint (.pptx) o Google Slides (exportar a PDF)
- 🎨 **Diseño:** Profesional, limpio y coherente
- 📝 **Texto:** Claro y conciso (no sobrecargues las diapositivas)
- 🖼️ **Imágenes:** Incluye capturas de código y gráficos generados
- 📊 **Visualizaciones:** Deben ser legibles y de alta calidad

**Ejemplo de estructura:**
```
1. Portada
2. Introducción al proyecto
3. Dataset y metodología
4. Limpieza de datos y código Python
5. Análisis estadístico: Resultados principales
6. Visualización 1: [Gráfico más relevante]
7. Visualización 2: [Otro gráfico importante]
8. Visualización 3: [Tercer gráfico]
9. Insights y patrones descubiertos
10. Conclusiones y reflexiones
11. Aspectos técnicos y aprendizajes
12. Gracias + Contacto (opcional)
```

**Consejos para una buena presentación:**
- 🎯 Sé visual: Usa gráficos en lugar de tablas cuando sea posible
- 💡 Destaca lo importante: Resalta los hallazgos más interesantes
- 🔬 Muestra código: Incluye snippets clave de Python que demuestren tu trabajo
- 📈 Cuenta una historia: Guía al lector a través de tu análisis
- ✨ Mantén la coherencia: Usa la misma paleta de colores y fuentes
- 🎨 No satures: Mejor menos texto y más visual

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

5. **`presentacion_[nombre].pdf`** o **`presentacion_[nombre].pptx`**
   - Presentación de resultados (8-12 diapositivas)
   - Formato profesional con gráficos y código
   - Ejemplo: `presentacion_analisis_musica.pdf`

### Formato de entrega:

Enlace del repositorio de GITHUB


## Criterios de evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Dataset** | 15 | Calidad, cantidad y relevancia de los datos |
| **Limpieza** | 10 | Proceso de limpieza documentado y ejecutado |
| **Estadísticas** | 20 | Variedad y profundidad de análisis realizados |
| **Visualizaciones** | 20 | Calidad, variedad e interpretación de gráficos |
| **Documentación** | 15 | Claridad, estructura y conclusiones |
| **Presentación** | 20 | Calidad de la presentación y exposición de resultados |
| **TOTAL** | **100** | |
