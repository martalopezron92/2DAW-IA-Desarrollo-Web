# P03 - Evaluación práctica: Fundamentos de Python y NumPy

## Prerrequisitos

- Haber completado las unidades **U3 - Fundamentos de Python para IA** y **U4 - NumPy**
- Haber realizado los ejercicios de refuerzo de ambas unidades
- Tener instalado Python 3.11+ y NumPy

## Materiales necesarios

### Software
- Python 3.11+
- NumPy instalado (`pip install numpy`)
- Editor de código (VS Code recomendado) o Jupyter Notebook

### Entrega
- **Archivo Python**: `apellido_nombre_P03.py` con los ejercicios resueltos
- **Formato de entrega**: Archivo ZIP con ambos archivos

## ⚠️ IMPORTANTE - Normas de evaluación

1. **Esta práctica es INDIVIDUAL**
2. **Se realizará un test posterior** para verificar que has adquirido los conocimientos
3. **El uso de IA está permitido SOLO para consultas puntuales**, no para resolver ejercicios completos
4. **Debes ser capaz de explicar tu código**
5. **La nota final será**:70% ejercicios prácticos + 30% test de conocimientos

---

# PARTE 1: EJERCICIOS PRÁCTICOS 

## Ejercicio 1: Análisis de ventas (15 puntos)

**Contexto**: Tienes datos de ventas mensuales de una tienda online.

```python
# Ventas mensuales en euros (Enero a Diciembre)
ventas = [15000, 18000, 22000, 17000, 25000, 30000, 28000, 32000, 27000, 29000, 35000, 40000]
```

### Tareas:

**a) (3 puntos)** Calcula el total de ventas del año usando una función apropiada.

**b) (4 puntos)** Crea una función `calcular_estadisticas(lista)` que reciba la lista de ventas y devuelva una tupla con: `(total, promedio, mes_mejor, mes_peor)` donde mes_mejor y mes_peor son los índices (0-11).

**c) (4 puntos)** Usa **list comprehension** para crear una nueva lista con las ventas que superaron el promedio. Muestra el resultado con el formato: `"Mes X: €Y"`.

**d) (4 puntos)** Usa las funciones `map()` y `filter()` para:
   - Aplicar un incremento del 15% a todas las ventas (simulando inflación)
   - Filtrar solo los meses donde las ventas con incremento superan los 30.000€
   - Muestra el resultado

```python
# TU CÓDIGO AQUÍ

```

---

## Ejercicio 2: Gestión de inventario (15 puntos)

**Contexto**: Gestionas el inventario de productos de un almacén.

```python
# Inventario inicial
productos = {
    "laptop": {"precio": 850, "stock": 15, "categoria": "informatica"},
    "raton": {"precio": 25, "stock": 50, "categoria": "informatica"},
    "teclado": {"precio": 45, "stock": 30, "categoria": "informatica"},
    "monitor": {"precio": 200, "stock": 20, "categoria": "informatica"},
    "silla": {"precio": 150, "stock": 10, "categoria": "mobiliario"},
    "mesa": {"precio": 300, "stock": 5, "categoria": "mobiliario"}
}
```

### Tareas:

**a) (3 puntos)** Crea una función `valor_total_inventario(productos)` que calcule el valor total del inventario (precio × stock de todos los productos).

**b) (4 puntos)** Crea una función `productos_por_categoria(productos, categoria)` que devuelva un **nuevo diccionario** solo con los productos de esa categoría.

**c) (4 puntos)** Usa **dict comprehension** para crear un nuevo diccionario llamado `productos_bajo_stock` que contenga solo los productos con stock menor a 20 unidades. El formato debe ser: `{nombre: stock}`.

**d) (4 puntos)** Implementa una función `actualizar_precios(productos, porcentaje)` que:
   - Aumente el precio de todos los productos según el porcentaje dado
   - Modifique el diccionario original (no crees uno nuevo)
   - Devuelva una lista con los nombres de productos cuyo nuevo precio supera los 200€

```python
# TU CÓDIGO AQUÍ

```

---

## Ejercicio 3: Procesamiento de datos con NumPy (20 puntos)

**Contexto**: Trabajas analizando datos de sensores de temperatura.

```python
import numpy as np

# Datos de sensores: 5 sensores, 7 días de mediciones
# Cada fila es un sensor, cada columna un día
np.random.seed(42)
temperaturas = np.random.uniform(15, 35, size=(5, 7))
```

### Tareas:

**a) (3 puntos)** Crea un array NumPy con los datos y muestra:
   - La forma (shape) del array
   - La temperatura media global
   - La temperatura máxima y mínima registradas

**b) (4 puntos)** Calcula y muestra:
   - La temperatura media de cada sensor (promedio por fila)
   - La temperatura media de cada día (promedio por columna)
   - El sensor con mayor temperatura promedio (índice)

**c) (5 puntos)** Crea una **máscara booleana** para identificar:
   - Temperaturas superiores a 28°C
   - Reemplaza esas temperaturas por exactamente 28 (simula un límite de seguridad)
   - Muestra cuántas temperaturas fueron ajustadas

**d) (4 puntos)** Normaliza los datos usando la fórmula Min-Max:
   ```
   temperatura_normalizada = (temperatura - min) / (max - min)
   ```
   - Los valores deben quedar entre 0 y 1
   - Muestra las primeras 3 filas normalizadas

**e) (4 puntos)** Usa **broadcasting** para:
   - Crear un array de "alertas" (bonos) de [10, 20, 15, 25, 18] € por sensor
   - Sumar estas alertas a CADA DÍA de medición de cada sensor
   - Mostrar el array resultante (shape debe seguir siendo 5x7)

```python
# TU CÓDIGO AQUÍ

```

---

## Ejercicio 4: Análisis de estudiantes (20 puntos)

**Contexto**: Tienes datos de calificaciones de estudiantes en diferentes asignaturas.

```python
import numpy as np

# Calificaciones: 20 estudiantes, 5 asignaturas
# Filas = estudiantes, Columnas = asignaturas
np.random.seed(123)
calificaciones = np.random.uniform(4, 10, size=(20, 5))
calificaciones = np.round(calificaciones, 1)

asignaturas = ["Matemáticas", "Física", "Programación", "Inglés", "Historia"]
```

### Tareas:

**a) (4 puntos)** Crea una función `estudiantes_aprobados(calificaciones, nota_minima=5.0)` que:
   - Devuelva un array booleano indicando qué estudiantes aprobaron TODAS las asignaturas
   - Muestre cuántos estudiantes aprobaron todo
   - Devuelva los índices de esos estudiantes

**b) (5 puntos)** Calcula y muestra:
   - La nota media de cada asignatura
   - La asignatura con mejor nota media (usa `np.argmax` y el array de nombres)
   - La asignatura con peor nota media
   - La desviación estándar de cada asignatura (indica cuál tiene más variabilidad)

**c) (5 puntos)** Crea un sistema de clasificación:
   - **Excelente**: nota media ≥ 9
   - **Notable**: 7 ≤ nota media < 9
   - **Bien**: 6 ≤ nota media < 7
   - **Aprobado**: 5 ≤ nota media < 6
   - **Suspenso**: nota media < 5
   
   Usa `np.where` o máscaras booleanas para crear un array con la clasificación de cada estudiante según su nota media.

**d) (6 puntos)** Análisis avanzado:
   - Encuentra el estudiante con mayor nota en cada asignatura (5 estudiantes, pueden repetirse)
   - Crea una "matriz de diferencias" que muestre la diferencia de cada estudiante respecto a la media de cada asignatura (resta la media de cada columna)
   - Identifica qué estudiante tiene la mayor desviación positiva total (suma de todas sus diferencias positivas)

```python
# TU CÓDIGO AQUÍ

```
