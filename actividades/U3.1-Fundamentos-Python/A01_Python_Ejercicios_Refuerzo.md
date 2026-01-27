# A01 - Ejercicios de Refuerzo: Fundamentos de Python

## Objetivo

Practicar y reforzar los conceptos fundamentales de Python necesarios para trabajar con librerías de ciencia de datos e inteligencia artificial. Estos ejercicios **no son evaluables**, sino que están diseñados para consolidar tu aprendizaje mediante la práctica.

## Instrucciones generales

- Crea un archivo `.py` para cada ejercicio
- Prueba tu código con diferentes valores de entrada
- Si te atascas, revisa los apuntes de la U3.1


---

## Nivel 1: Fundamentos básicos

### Ejercicio 1: Conversor de unidades

Crea un programa que convierta temperaturas entre Celsius, Fahrenheit y Kelvin.

**Requisitos:**
- Pide al usuario la temperatura y la unidad de origen
- Pide la unidad de destino
- Muestra el resultado con 2 decimales
- Usa funciones para cada conversión

**Fórmulas:**
- Celsius a Fahrenheit: `(C × 9/5) + 32`
- Celsius a Kelvin: `C + 273.15`
- Fahrenheit a Celsius: `(F - 32) × 5/9`

```python
# Ejemplo de salida esperada:
# Ingrese la temperatura: 25
# Unidad de origen (C/F/K): C
# Unidad de destino (C/F/K): F
# 25.0°C = 77.0°F
```

---

### Ejercicio 2: Analizador de palabras

Crea un programa que analice un texto proporcionado por el usuario.

**Requisitos:**
- Cuenta el número de palabras
- Encuentra la palabra más larga
- Cuenta cuántas veces aparece cada vocal (a, e, i, o, u)
- Muestra las 3 palabras más largas
- Ignora mayúsculas/minúsculas para el conteo de vocales

```python
# Ejemplo de entrada:
texto = "Python es un lenguaje de programación increíble para ciencia de datos"

# Salida esperada:
# Número de palabras: 11
# Palabra más larga: programación (12 caracteres)
# Vocales: a=6, e=8, i=5, o=4, u=2
# Top 3 palabras más largas: programación, increíble, lenguaje
```

---

### Ejercicio 3: Calculadora de estadísticas

Crea una función que calcule estadísticas básicas de una lista de números.

**Requisitos:**
- Recibe una lista de números
- Calcula: media, mediana, moda, rango (max - min), varianza
- Devuelve un diccionario con los resultados
- **NO uses librerías** (implementa los cálculos tú mismo)

```python
def calcular_estadisticas(numeros):
    # Tu código aquí
    pass

# Ejemplo de uso:
datos = [23, 45, 67, 45, 89, 12, 45, 34, 56, 78]
resultados = calcular_estadisticas(datos)
print(resultados)
# {'media': 49.4, 'mediana': 45, 'moda': 45, 'rango': 77, 'varianza': 512.84}
```

**Pistas:**
- Media: suma de todos / cantidad
- Mediana: valor central de la lista ordenada
- Moda: valor que más se repite
- Varianza: promedio de las diferencias al cuadrado respecto a la media

---

## Nivel 2: Estructuras de datos

### Ejercicio 4: Gestor de inventario

Crea un sistema simple de gestión de inventario usando diccionarios.

**Requisitos:**
- Usa un diccionario para almacenar productos (clave: nombre, valor: diccionario con precio y cantidad)
- Implementa funciones para: agregar producto, actualizar precio, actualizar stock, eliminar producto
- Función para mostrar el inventario ordenado por precio
- Función para calcular el valor total del inventario

```python
inventario = {}

def agregar_producto(nombre, precio, cantidad):
    # Tu código aquí
    pass

def valor_total_inventario():
    # Tu código aquí
    pass

# Ejemplo de uso:
agregar_producto("Laptop", 899.99, 5)
agregar_producto("Mouse", 15.99, 20)
agregar_producto("Teclado", 45.50, 15)
print(valor_total_inventario())  # 5116.75
```

---

### Ejercicio 5: Procesador de datos de estudiantes

Trabaja con una lista de diccionarios que representan estudiantes.

**Requisitos:**
- Crea una lista con al menos 10 estudiantes (nombre, edad, nota_media, asignaturas_aprobadas)
- Filtra estudiantes con nota_media >= 7.0
- Encuentra al estudiante con más asignaturas aprobadas
- Calcula la edad promedio de los estudiantes aprobados
- Usa **comprehensions** donde sea posible

```python
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota_media": 8.5, "asignaturas_aprobadas": 12},
    {"nombre": "Carlos", "edad": 22, "nota_media": 6.2, "asignaturas_aprobadas": 9},
    # ... más estudiantes
]

# Implementa las funciones necesarias
```

---

### Ejercicio 6: Análisis de ventas

Procesa datos de ventas mensuales usando conjuntos y diccionarios.

**Requisitos:**
- Diccionario con ventas por mes: `{"Enero": [120, 150, 200], "Febrero": [180, 190, 210], ...}`
- Calcula el total de ventas por mes
- Encuentra el mes con mayores ventas
- Identifica los días con ventas superiores al promedio general
- Usa `map()`, `filter()` y `reduce()`

```python
from functools import reduce

ventas_mensuales = {
    "Enero": [120, 150, 200, 180, 210],
    "Febrero": [180, 190, 210, 200, 230],
    "Marzo": [150, 160, 170, 180, 190]
}

# Implementa el análisis
```

---

## Nivel 3: Programación funcional

### Ejercicio 7: Pipeline de transformación de datos

Crea un pipeline que procese una lista de datos usando map, filter y reduce.

**Requisitos:**
- Lista inicial: números del 1 al 100
- Filtra solo los múltiplos de 3 o 5
- Eleva cada número al cuadrado
- Suma todos los resultados
- Implementa todo en **una sola expresión** encadenando las funciones

```python
from functools import reduce

# Tu código aquí (una sola línea)
resultado = ...

print(resultado)  # Debe dar un número específico
```

---

### Ejercicio 8: Generador de reportes

Crea funciones que procesen listas de transacciones financieras.

**Requisitos:**
- Lista de transacciones: `[{"tipo": "ingreso/gasto", "cantidad": float, "categoria": str, "fecha": str}]`
- Usa `map()` para extraer solo las cantidades
- Usa `filter()` para separar ingresos de gastos
- Usa `reduce()` para calcular balance total
- Crea una función que agrupe por categoría usando comprehensions

```python
transacciones = [
    {"tipo": "ingreso", "cantidad": 1500.00, "categoria": "salario", "fecha": "2025-01-01"},
    {"tipo": "gasto", "cantidad": 50.00, "categoria": "comida", "fecha": "2025-01-02"},
    {"tipo": "gasto", "cantidad": 800.00, "categoria": "alquiler", "fecha": "2025-01-03"},
    # ... más transacciones
]

# Implementa las funciones
```

---

### Ejercicio 9: Sistema de recomendaciones simple

Implementa un sistema básico de recomendación usando conjuntos.

**Requisitos:**
- Diccionario de usuarios y sus intereses (conjuntos)
- Función que encuentre usuarios con intereses similares
- Función que recomiende nuevos intereses basados en usuarios similares
- Usa operaciones de conjuntos (intersección, unión, diferencia)

```python
usuarios_intereses = {
    "Ana": {"Python", "Machine Learning", "Data Science", "Música"},
    "Carlos": {"JavaScript", "React", "Node.js", "Videojuegos"},
    "Elena": {"Python", "Data Science", "Estadística", "Lectura"},
    "David": {"Python", "Django", "PostgreSQL", "Música"},
    # ... más usuarios
}

def encontrar_usuarios_similares(usuario, minimo_coincidencias=2):
    # Tu código aquí
    pass

def recomendar_intereses(usuario):
    # Tu código aquí
    pass

print(recomendar_intereses("Ana"))
# ["Estadística", "Django", "PostgreSQL"] (intereses de usuarios similares que Ana no tiene)
```

---

## Nivel 4: Desafío avanzado

### Ejercicio 10: Validador de contraseñas robusto

Crea un validador de contraseñas con múltiples criterios.

**Requisitos:**
- Longitud mínima de 12 caracteres
- Al menos 2 mayúsculas, 2 minúsculas, 2 números, 2 símbolos
- No puede contener palabras comunes (diccionario de 20 palabras)
- No puede tener 3 caracteres consecutivos iguales
- Devuelve `(bool, [lista de errores])`

```python
def validar_password(password):
    errores = []
    # Tu código aquí
    return len(errores) == 0, errores

# Ejemplo:
valida, errores = validar_password("MiPass123!@")
print(valida, errores)
# (False, ['Longitud insuficiente', 'Solo 1 mayúscula'])
```

---

## Consejos para resolver los ejercicios

1. **Lee el ejercicio completo** antes de empezar a programar
2. **Divide el problema** en partes más pequeñas
3. **Prueba con ejemplos simples** antes de casos complejos
4. **No te frustres** si algo no sale a la primera - es parte del aprendizaje
5. **Experimenta**: prueba diferentes enfoques para resolver el mismo problema
6. **Comenta tu código**: explica qué hace cada parte
7. **Busca en la documentación** de Python cuando no sepas cómo hacer algo
8. **Compara con compañeros**: ver diferentes soluciones enriquece el aprendizaje

## 📚 Recursos útiles

- Documentación oficial de Python: https://docs.python.org/es/3/
- Python Tutor (visualizador de código): https://pythontutor.com/
- Real Python (tutoriales): https://realpython.com/
- Stack Overflow en español: https://es.stackoverflow.com/

---

## ⚠️ Importante

**Estos ejercicios NO son evaluables**. Su único propósito es ayudarte a:
- Practicar los conceptos vistos en clase
- Ganar confianza con Python
- Identificar áreas donde necesitas reforzar
- Prepararte para proyectos más complejos con datos reales

Si tienes dudas o quieres compartir tus soluciones, puedes hacerlo en clase o consultarme.

**¡Buena suerte y a programar!** 
