# Práctica Evaluable: Sistema de predicción para e-commerce

#### Contexto

Trabajas en el equipo de desarrollo de una tienda online. El departamento de marketing quiere implementar dos sistemas predictivos:

1. **Sistema de abandono de carrito**: Predecir si un usuario abandonará el carrito sin comprar
2. **Sistema de predicción de ventas**: Estimar el valor de las compras mensuales de cada usuario

Tu tarea es desarrollar ambos modelos, evaluarlos y documentar tus hallazgos.

---

#### Dataset proporcionado

```python
import pandas as pd

# Datos de usuarios del último trimestre
datos_usuarios = {
    'edad': [28, 42, 35, 51, 23, 38, 45, 29, 33, 47, 26, 39, 44, 31, 50, 
             27, 36, 41, 48, 25, 34, 43, 30, 37, 46],
    'sesiones_mes': [3, 12, 7, 15, 2, 10, 18, 5, 8, 14, 4, 11, 16, 6, 13,
                     3, 9, 15, 17, 2, 7, 14, 5, 10, 19],
    'tiempo_promedio_min': [5, 25, 15, 30, 3, 20, 35, 10, 18, 28, 8, 22, 32, 12, 27,
                           6, 16, 29, 33, 4, 14, 26, 9, 21, 38],
    'productos_en_wishlist': [1, 8, 4, 10, 0, 6, 12, 2, 5, 9, 1, 7, 11, 3, 8,
                              1, 5, 9, 13, 0, 4, 10, 2, 6, 14],
    'usa_app_movil': ['No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                      'No', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'No',
                      'Sí', 'Sí', 'No', 'Sí', 'Sí'],
    'abandono_carrito': ['Sí', 'No', 'Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'No', 'No',
                        'Sí', 'No', 'No', 'Sí', 'No', 'Sí', 'No', 'No', 'No', 'Sí',
                        'No', 'No', 'Sí', 'No', 'No'],
    'valor_compras_mes': [25, 180, 85, 240, 15, 150, 290, 45, 120, 210, 30, 165, 270, 70, 200,
                         28, 110, 225, 310, 18, 95, 195, 50, 155, 340]
}

df = pd.DataFrame(datos_usuarios)
```

---

#### Tareas a realizar

### PARTE A: Modelo de Clasificación - Abandono de Carrito (50 puntos)

**A1. Identificación del problema (5 puntos)**
- Define claramente cuál es la variable objetivo
- Indica qué features usarás para predecir
- Justifica por qué es un problema de clasificación

**A2. Preparación de datos (10 puntos)**
- Convierte variables categóricas a numéricas si es necesario
- Separa X e y correctamente
- Divide en train/test (70% train, 30% test)
- Explica por qué divides los datos

**A3. Entrenamiento del modelo (10 puntos)**
- Elige un modelo apropiado (DecisionTreeClassifier, LogisticRegression, etc.)
- Entrena el modelo con los datos de train
- Documenta los hiperparámetros elegidos

**A4. Evaluación (15 puntos)**
- Calcula accuracy en train y test
- Genera y analiza la matriz de confusión
- Identifica si hay overfitting/underfitting
- Justifica si el modelo es útil para el negocio

**A5. Interpretación de negocio (10 puntos)**
- ¿Qué tipo de error es más grave en este contexto: falsos positivos o falsos negativos? Justifica.
- Propón 2 acciones concretas que marketing podría tomar con este modelo.

---

### PARTE B: Modelo de Regresión - Valor de Compras (50 puntos)

**B1. Identificación del problema (5 puntos)**
- Define la variable objetivo
- Indica las features que usarás
- Justifica por qué es un problema de regresión

**B2. Preparación de datos (10 puntos)**
- Procesa variables si es necesario
- Separa X e y
- Divide en train/test (70% train, 30% test)

**B3. Entrenamiento del modelo (10 puntos)**
- Usa LinearRegression u otro modelo de regresión
- Entrena correctamente
- Documenta tu elección de modelo

**B4. Evaluación (15 puntos)**
- Calcula MAE, RMSE y R² en train y test
- Analiza si hay overfitting/underfitting
- Interpreta qué significan las métricas obtenidas en euros

**B5. Interpretación de negocio (10 puntos)**
- ¿Es aceptable el error medio obtenido? Justifica.
- ¿Qué factores adicionales podrían mejorar las predicciones?
- Propón una aplicación concreta de este modelo en la web.

---

#### Reflexión final obligatoria (Extra: hasta 10 puntos)

Escribe un breve informe respondiendo:

1. **Limitaciones**: ¿Qué limitaciones tienen tus modelos? ¿Qué no pueden predecir?

2. **Mejoras**: Si tuvieras más tiempo y recursos, ¿cómo mejorarías los modelos?

3. **Ética**: ¿Qué riesgos éticos podrían surgir al usar estos modelos? (sesgos, discriminación, etc.)

4. **Impacto**: ¿Cómo afectarían estos sistemas a la experiencia del usuario?

---

#### Formato de entrega

**Archivos a entregar:**

1. **practica_modelos_supervisados.py** 
   - Código completo con comentarios
   - Cada apartado claramente marcado

2. **informe_resultados.md** 
   - Respuestas a todas las preguntas
   - Capturas de pantalla de salidas relevantes
   - Reflexión final

Recomendable: Compartir enlace del repositorio de github con los códigos, y en el README el informe de resultados.

**Estructura del código:**
```python
# =====================================
# PARTE A: CLASIFICACIÓN - ABANDONO DE CARRITO
# =====================================

# A1. Identificación del problema
# [Tu respuesta aquí]

# A2. Preparación de datos
# [Tu código aquí]

# A3. Entrenamiento
# [Tu código aquí]

# A4. Evaluación
# [Tu código aquí]

# A5. Interpretación de negocio
# [Tu respuesta aquí]

# =====================================
# PARTE B: REGRESIÓN - VALOR DE COMPRAS
# =====================================

# [Misma estructura...]

# =====================================
# REFLEXIÓN FINAL
# =====================================
# [Tu reflexión aquí]
```

---

#### Rúbrica de evaluación

| Criterio | Insuficiente (0-5) | Suficiente (5-7) | Notable (7-9) | Sobresaliente (9-10) |
|----------|-------------------|------------------|---------------|---------------------|
| **Identificación del problema** | No identifica correctamente tipo de problema | Identifica pero sin justificar | Identifica y justifica adecuadamente | Identifica, justifica y conecta con contexto real |
| **Uso correcto del modelo** | Errores graves en implementación | Implementa con errores menores | Implementa correctamente | Implementa correctamente y optimiza hiperparámetros |
| **Evaluación técnica** | No calcula métricas o están mal | Calcula algunas métricas correctamente | Calcula todas las métricas y las interpreta | Análisis profundo de métricas y detección de problemas |
| **Interpretación de resultados** | No interpreta o interpretación errónea | Interpretación básica | Interpretación correcta y contextualizada | Interpretación profunda con propuestas de acción |
| **Calidad del código** | Código no funciona o muy desorganizado | Funciona pero poco claro | Código claro y comentado | Código profesional, modular y bien documentado |
| **Razonamiento crítico** | No reflexiona sobre limitaciones | Reflexión superficial | Identifica limitaciones y propone mejoras | Análisis crítico profundo incluyendo aspectos éticos |

**Criterios de evaluación adicionales:**
-  El código debe ejecutarse sin errores
-  Las respuestas deben estar justificadas, no solo respondidas con "Sí/No"
-  Se valora la conexión entre teoría y práctica
-  La reflexión final es obligatoria para obtener más de 8 puntos
-  La presentación y organización cuentan: código limpio, documentado y estructurado

---