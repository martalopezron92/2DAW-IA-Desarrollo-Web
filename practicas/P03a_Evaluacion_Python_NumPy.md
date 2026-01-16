# P03a - Evaluación práctica: Fundamentos de Python y NumPy

## 🎯 Objetivos

Al completar esta práctica evaluativa, demostrarás que eres capaz de:

- **Aplicar** sintaxis y estructuras de control de Python
- **Manipular** estructuras de datos nativas (listas, diccionarios, tuplas, sets)
- **Implementar** funciones y aplicar programación funcional
- **Trabajar** con arrays de NumPy eficientemente
- **Resolver** problemas reales de procesamiento de datos

## ⏱️ Duración estimada

**2 horas** (120 minutos)
- **Parte 1 - Ejercicios prácticos**: 90 minutos
- **Parte 2 - Test de conocimientos**: 30 minutos

## 📋 Prerrequisitos

- Haber completado las unidades **U3 - Fundamentos de Python para IA** y **U4 - NumPy**
- Haber realizado los ejercicios de refuerzo de ambas unidades
- Tener instalado Python 3.11+ y NumPy

## 🛠️ Materiales necesarios

### Software
- Python 3.11+
- NumPy instalado (`pip install numpy`)
- Editor de código (VS Code recomendado) o Jupyter Notebook

### Entrega
- **Archivo Python**: `apellido_nombre_P03b.py` con los ejercicios resueltos
- **Archivo de respuestas**: `apellido_nombre_P03b_TEST.md` con las respuestas del test
- **Formato de entrega**: Archivo ZIP con ambos archivos

## ⚠️ IMPORTANTE - Normas de evaluación

1. **Esta práctica es INDIVIDUAL**
2. **Se realizará un test posterior** para verificar que has adquirido los conocimientos
3. **El uso de IA está permitido SOLO para consultas puntuales**, no para resolver ejercicios completos
4. **Debes ser capaz de explicar tu código** en el test posterior
5. **La nota final será**: 70% ejercicios prácticos + 30% test de conocimientos

---

# PARTE 1: EJERCICIOS PRÁCTICOS (70 puntos)

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

---

# PARTE 2: TEST DE CONOCIMIENTOS (30 puntos)

**⚠️ IMPORTANTE**: Este test se realizará **sin acceso al código** ni a internet. Responde en el archivo `apellido_nombre_P03b_TEST.md`.

## Instrucciones del test

- **Duración**: 30 minutos
- **Formato**: Respuestas cortas y opción múltiple
- **Sin material de apoyo**: No se puede consultar código, apuntes ni internet
- **Entrega**: Archivo Markdown con las respuestas

---

## Sección 1: Python Básico (10 puntos)

### Pregunta 1 (2 puntos)
¿Cuál es la salida del siguiente código?
```python
x = [1, 2, 3, 4, 5]
resultado = x[1:4]
print(resultado)
```

**Opciones:**
- a) `[1, 2, 3]`
- b) `[2, 3, 4]`
- c) `[2, 3, 4, 5]`
- d) `[1, 2, 3, 4]`

**Respuesta**: ___

---

### Pregunta 2 (2 puntos)
¿Qué estructura de datos usarías para almacenar elementos únicos sin orden específico?

**Opciones:**
- a) Lista
- b) Tupla
- c) Set
- d) Diccionario

**Respuesta**: ___

---

### Pregunta 3 (3 puntos)
Explica en **2-3 líneas** qué hace este código y cuál es su salida:
```python
numeros = [1, 2, 3, 4, 5, 6]
resultado = list(filter(lambda x: x % 2 == 0, numeros))
```

**Tu explicación**:
```
___________________________________
___________________________________
___________________________________
```

---

### Pregunta 4 (3 puntos)
Escribe en **pseudocódigo o Python** (sin ejecutar) una función que reciba una lista de números y devuelva solo los que son mayores que su promedio.

**Tu código**:
```python
# Tu respuesta aquí
```

---

## Sección 2: NumPy (10 puntos)

### Pregunta 5 (2 puntos)
¿Cuál es la diferencia principal entre una lista de Python y un array de NumPy?

**Opciones:**
- a) Las listas son mutables, los arrays no
- b) Los arrays de NumPy son más rápidos para operaciones numéricas
- c) Las listas solo pueden contener números
- d) Los arrays no pueden ser multidimensionales

**Respuesta**: ___

---

### Pregunta 6 (3 puntos)
Dado este código, ¿cuál es el shape del array resultante?
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
resultado = arr.T
```

**Opciones:**
- a) `(2, 3)`
- b) `(3, 2)`
- c) `(6,)`
- d) `(1, 6)`

**Respuesta**: ___

**Justifica tu respuesta (1 línea)**:
```
___________________________________
```

---

### Pregunta 7 (2 puntos)
¿Qué es el "broadcasting" en NumPy?

**Opciones:**
- a) Una forma de transmitir datos por red
- b) Un mecanismo para operar arrays de diferentes formas
- c) Una función para hacer arrays más grandes
- d) Un tipo especial de array

**Respuesta**: ___

---

### Pregunta 8 (3 puntos)
Escribe en **pseudocódigo o Python** cómo crearías un array de NumPy de 10x10 con:
- Todos los elementos en 0
- Excepto la diagonal principal que debe ser 1

**Tu código**:
```python
# Tu respuesta aquí
```

---

## Sección 3: Integración y Resolución de Problemas (10 puntos)

### Pregunta 9 (5 puntos)
Tienes este diccionario:
```python
ventas = {
    "producto_a": [100, 150, 200],
    "producto_b": [80, 90, 100],
    "producto_c": [200, 250, 300]
}
```

Explica en **4-5 líneas** cómo calcularías:
1. El total de ventas de cada producto
2. El producto con mayores ventas totales

**Usa Python estándar O NumPy** (indica cuál prefieres y por qué).

**Tu explicación**:
```
___________________________________
___________________________________
___________________________________
___________________________________
___________________________________
```

---

### Pregunta 10 (5 puntos)
Imagina que tienes un array NumPy de temperaturas y necesitas:
1. Identificar valores atípicos (outliers) como aquellos que están a más de 2 desviaciones estándar de la media
2. Reemplazar esos valores por la mediana del array

Describe en **pseudocódigo** (o Python) los pasos que seguirías. **No es necesario código perfecto**, solo la lógica.

**Tu respuesta**:
```python
# Tu pseudocódigo aquí
```

---

# 📤 FORMATO DE ENTREGA

Crea un archivo ZIP llamado `apellido_nombre_P03b.zip` que contenga:

```
apellido_nombre_P03b.zip
│
├── apellido_nombre_P03b.py          # Ejercicios 1-4 resueltos
└── apellido_nombre_P03b_TEST.md     # Respuestas del test (Preguntas 1-10)
```

## Ejemplo del archivo Python:

```python
"""
P03b - Evaluación Python y NumPy
Alumno: [Tu nombre completo]
Fecha: [Fecha de entrega]
"""

import numpy as np
from functools import reduce

# ============================================
# EJERCICIO 1: ANÁLISIS DE VENTAS
# ============================================

print("="*50)
print("EJERCICIO 1: ANÁLISIS DE VENTAS")
print("="*50)

ventas = [15000, 18000, 22000, 17000, 25000, 30000, 28000, 32000, 27000, 29000, 35000, 40000]

# a) Total de ventas
# Tu código aquí

# b) Función calcular_estadisticas
# Tu código aquí

# c) Ventas sobre promedio con list comprehension
# Tu código aquí

# d) map() y filter()
# Tu código aquí

# ============================================
# EJERCICIO 2: GESTIÓN DE INVENTARIO
# ============================================

# ... continúa con los demás ejercicios
```

## Ejemplo del archivo TEST:

```markdown
# P03b - Test de Conocimientos

**Alumno**: [Tu nombre completo]
**Fecha**: [Fecha]

---

## Sección 1: Python Básico

### Pregunta 1
**Respuesta**: b

### Pregunta 2
**Respuesta**: c

### Pregunta 3
**Explicación**: 
Este código filtra los números pares de la lista usando filter() y una función lambda...

[... continúa con todas las preguntas ...]
```

---

# 🎓 Consejos para el éxito

1. **Lee todo el enunciado** antes de empezar
2. **Gestiona tu tiempo**: 90 min para ejercicios, 30 min para el test
3. **Comenta tu código** para que se entienda tu razonamiento
4. **Prueba cada ejercicio** antes de pasar al siguiente
5. **En el test**, si no sabes algo, escribe tu razonamiento
6. **Revisa** antes de entregar

---

# ❓ Preguntas frecuentes

**P: ¿Puedo usar internet durante los ejercicios?**
R: Sí, para consultar documentación oficial de Python/NumPy. NO para buscar soluciones completas.

**P: ¿Qué pasa si no termino todos los ejercicios?**
R: Entrega lo que tengas. Es mejor código parcial bien hecho que todo mal hecho.

**P: ¿El test es con ordenador?**
R: Sí, pero sin acceso a internet ni a tus archivos de código.

**P: ¿Puedo usar ChatGPT/Copilot?**
R: Para consultas puntuales sí, pero recuerda que el test verificará que realmente entiendes. Si copias todo, suspenderás el test.

---

**¡Mucha suerte! 🚀**
