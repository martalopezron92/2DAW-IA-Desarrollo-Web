# Análisis y tratamiento de datos
---

# 📊 ¿Qué significa analizar datos y para qué sirve?

## 🤔 ¿Qué es un dato?

Un **dato** es cualquier información que podemos registrar y medir. Los datos están en todas partes:

### Ejemplos cotidianos de datos:

- 📱 **Tu móvil**: número de pasos, batería restante, apps más usadas
- 🛒 **Un supermercado**: ventas diarias, productos más comprados, stock disponible
- 🎓 **En clase**: notas de exámenes, asistencia, tiempo de entrega de trabajos
- 🌡️ **El tiempo**: temperatura, humedad, probabilidad de lluvia
- 💰 **Tu economía**: gastos mensuales, ahorros, suscripciones activas
- 🎮 **Videojuegos**: puntuación, tiempo jugado, nivel alcanzado

> **💡 Dato importante**: Un dato por sí solo puede no significar nada. Por ejemplo, el número "23" solo es información útil si sabemos que es:
> - La temperatura actual (23°C)
> - Tu edad (23 años)
> - El número de alumnos en clase (23 personas)

## 🔍 ¿Qué es analizar datos?

**Analizar datos** significa examinar información para encontrar patrones, responder preguntas y tomar decisiones.

Es como ser detective, pero en lugar de buscar pistas en una escena del crimen, buscas patrones en números y textos.

### Ejemplo sencillo:

Imagina que tienes estas notas de programación:
```
7, 8, 4, 9, 7, 8, 10, 6, 8, 7
```

**Sin analizar**: Solo ves números.

**Analizando**:
- Tu nota media es **7.4**
- Tu nota más baja es **4**
- Tu nota más frecuente es **8** (aparece 3 veces)
- Hay una tendencia: estás mejorando (últimas notas más altas)

➡️ **Conclusión**: Vas bien, pero debes reforzar para evitar más 4s.

## 🎯 ¿Para qué sirve analizar datos?

El análisis de datos sirve para:

### 1. **Tomar mejores decisiones**
- Netflix analiza qué ves para recomendarte series
- Amazon analiza tus búsquedas para sugerirte productos
- Una tienda analiza ventas para decidir qué productos reponer

### 2. **Detectar problemas**
- Un hospital analiza tiempos de espera para mejorar el servicio
- Una app analiza errores para saber qué fallos corregir primero
- Un e-commerce detecta en qué paso los usuarios abandonan la compra

### 3. **Predecir el futuro**
- Spotify predice qué canción te gustará
- Una tienda predice cuánto venderá en Navidad
- Un banco predice si alguien puede devolver un préstamo

### 4. **Entender qué está pasando**
- ¿Por qué cayeron las ventas en marzo?
- ¿Qué perfil de usuario compra más?
- ¿A qué hora hay más visitas en nuestra web?

## 📈 Tipos de análisis de datos

Existen diferentes tipos de análisis según lo que queramos conseguir:

### 1️⃣ **Análisis Descriptivo** (¿Qué pasó?)

**Objetivo**: Describir y resumir lo que ya ocurrió.

**Ejemplo**: 
- "El mes pasado vendimos 500 productos"
- "La nota media de la clase es 6.5"
- "El producto más vendido fue el iPhone"

**Herramientas típicas**: 
- Tablas resumen
- Gráficos de barras
- Medias, medianas, porcentajes

---

### 2️⃣ **Análisis Diagnóstico** (¿Por qué pasó?)

**Objetivo**: Entender las causas de lo que ocurrió.

**Ejemplo**:
- "Las ventas bajaron porque subimos los precios un 15%"
- "Muchos alumnos suspendieron porque el examen fue muy largo"
- "La web cayó porque recibimos 10 veces más visitas de lo normal"

**Herramientas típicas**:
- Comparación de datos (antes/después)
- Análisis de correlaciones
- Identificación de anomalías

---

### 3️⃣ **Análisis Predictivo** (¿Qué pasará?)

**Objetivo**: Predecir comportamientos futuros basándose en datos históricos.

**Ejemplo**:
- "Según las ventas de años anteriores, venderemos 2000 unidades en diciembre"
- "Este alumno tiene alta probabilidad de aprobar el curso"
- "Mañana habrá picos de tráfico web a las 12h y 19h"

**Herramientas típicas**:
- Machine Learning (básico)
- Modelos estadísticos
- Series temporales

> ⚠️ **Nota**: En este curso nos centraremos en lo **conceptual**. No programaremos modelos predictivos avanzados.

---

### 4️⃣ **Análisis Prescriptivo** (¿Qué deberíamos hacer?)

**Objetivo**: Recomendar acciones para optimizar resultados.

**Ejemplo**:
- "Deberías enviar emails promocionales los martes a las 18h"
- "Contrata 3 empleados más para el Black Friday"
- "Reduce el stock de este producto porque no se venderá"

**Herramientas típicas**:
- Optimización
- Simulación de escenarios
- Inteligencia artificial

> ⚠️ **Nota**: Este es el nivel más avanzado y solo lo veremos de forma conceptual.

---

## 🌟 Ejemplos aplicados a tu día a día

### Ejemplo 1: Análisis de tus gastos mensuales

| Categoría | Gasto (€) |
|-----------|-----------|
| Comida | 250 |
| Transporte | 60 |
| Ocio | 120 |
| Suscripciones | 30 |
| Otros | 40 |
| **TOTAL** | **500** |

**Análisis descriptivo**: Gastas 500€ al mes, el 50% va a comida.

**Análisis diagnóstico**: Gastas mucho en comida porque comes fuera 3 veces por semana.

**Análisis predictivo**: Si sigues así, gastarás 6000€ al año.

**Análisis prescriptivo**: Deberías cocinar más en casa para ahorrar 100€/mes.

---

### Ejemplo 2: Análisis de una web de e-commerce

**Datos recogidos**:
- 10.000 visitas al mes
- 500 compras realizadas
- Ticket medio: 50€

**Análisis descriptivo**: Solo el 5% de visitantes compra.

**Análisis diagnóstico**: El 60% abandona en el paso de pago (proceso muy lento).

**Análisis predictivo**: Si mejoramos el checkout, podríamos llegar a 800 compras/mes.

**Análisis prescriptivo**: Implementar pago en 1 clic y ofrecer envío gratis desde 40€.

---

# 🔄 Ciclo de Vida del Dato

## 🎯 ¿Qué es el ciclo de vida del dato?

El **ciclo de vida del dato** es el camino completo que recorre la información desde que se obtiene hasta que se usa para tomar decisiones.

Es como una **cadena de montaje** donde cada paso es importante para obtener información útil.

> 💡 **Analogía**: Es como cocinar:
> 1. Compras ingredientes (obtención)
> 2. Los guardas en la nevera (almacenamiento)
> 3. Los lavas y pelas (limpieza)
> 4. Los cocinas (análisis)
> 5. Los emplateas bonito (visualización)
> 6. Los pruebas (interpretación)
> 7. Decides si repetir la receta (toma de decisiones)

---

## 📊 Las 7 fases del ciclo de vida del dato

```
┌─────────────┐
│  1. OBTENCIÓN  │
└───────┬───────┘
        │
┌───────▼──────────┐
│  2. ALMACENAMIENTO  │
└───────┬───────────┘
        │
┌───────▼──────┐
│  3. LIMPIEZA   │
└───────┬────────┘
        │
┌───────▼─────┐
│  4. ANÁLISIS  │
└───────┬───────┘
        │
┌───────▼─────────┐
│  5. VISUALIZACIÓN │
└───────┬─────────┘
        │
┌───────▼──────────┐
│  6. INTERPRETACIÓN │
└───────┬──────────┘
        │
┌───────▼────────────────┐
│  7. TOMA DE DECISIONES  │
└────────────────────────┘
```

---

## 1️⃣ **OBTENCIÓN** de datos

### ¿Qué es?
Es el proceso de **recoger o capturar** la información que necesitamos.

### ¿Cómo se obtienen datos?

#### 🌐 En el mundo web:
- **Formularios**: Cuando un usuario se registra o rellena una encuesta
- **Cookies y tracking**: Rastreo de comportamiento (páginas visitadas, tiempo en la web)
- **APIs**: Obtener datos de servicios externos (clima, redes sociales, bancos)
- **Web scraping**: Extraer datos automáticamente de páginas web
- **Logs del servidor**: Registros automáticos de errores, accesos, peticiones

#### 📱 En aplicaciones:
- Eventos de usuario (clics, scroll, búsquedas)
- Sensores del móvil (GPS, acelerómetro, micrófono)
- Notificaciones push (aceptadas/rechazadas)

#### 📊 En empresas:
- Ventas en tienda física (TPV)
- Encuestas a clientes
- Datos públicos (INE, gobierno, organismos)
- Compra de bases de datos

### Ejemplo práctico:
Un e-commerce obtiene datos cuando:
- Un usuario crea una cuenta ➡️ Email, nombre, fecha nacimiento
- Alguien compra ➡️ Producto, precio, fecha, forma de pago
- Alguien abandona el carrito ➡️ Productos en carrito, momento de abandono

---

## 2️⃣ **ALMACENAMIENTO** de datos

### ¿Qué es?
Una vez obtenidos, los datos deben **guardarse de forma organizada** para poder acceder a ellos después.

### ¿Dónde se almacenan?

| Tipo de almacenamiento | Descripción | Ejemplo |
|------------------------|-------------|---------|
| **Bases de datos relacionales** | Tablas estructuradas con relaciones | MySQL, PostgreSQL |
| **Bases de datos NoSQL** | Datos flexibles, no estructurados | MongoDB, Redis |
| **Archivos planos** | CSV, Excel, JSON, XML | ventas.csv, usuarios.json |
| **Data Lakes** | Almacén masivo de datos en bruto | AWS S3, Azure Data Lake |
| **Data Warehouses** | Almacén optimizado para análisis | Google BigQuery, Snowflake |

### Ejemplo práctico:
```
Formulario web → MySQL (almacenamiento)
└── Tabla: usuarios
    ├── id
    ├── nombre
    ├── email
    └── fecha_registro
```

> ⚠️ **Importante**: Unos datos bien almacenados son fáciles de recuperar y analizar. Datos desorganizados = pesadilla futura.

---

## 3️⃣ **LIMPIEZA** de datos

### ¿Qué es?
Preparar los datos para que sean **útiles y fiables**. Los datos en bruto suelen tener errores.

### ¿Qué problemas encontramos?

#### 🚫 Datos nulos o vacíos
```python
nombre,edad,ciudad
Ana,25,Madrid
Pedro,,Barcelona  # Falta la edad
Luis,30,          # Falta la ciudad
```

#### 🔄 Datos duplicados
```python
email,nombre
ana@mail.com,Ana
ana@mail.com,Ana  # Duplicado
```

#### 🤯 Formatos inconsistentes
```python
fecha_nacimiento
15/03/1998
1998-03-15
15-marzo-98
```

#### 📏 Valores atípicos (outliers)
```python
edad: 25, 30, 22, 28, 150  # 150 es un error evidente
```

### Tareas típicas de limpieza:
✅ Eliminar duplicados  
✅ Rellenar o eliminar valores nulos  
✅ Corregir errores de formato  
✅ Convertir tipos de datos (texto a número, etc.)  
✅ Estandarizar nomenclaturas  

### Ejemplo práctico:
```python
# ANTES (datos sucios)
nombre,edad,ciudad
Ana Martínez,25,madrid
ANA MARTINEZ,25,Madrid  # Duplicado con diferente formato
Pedro,,barcelona        # Falta edad
Luis,treinta,Barcelona  # Edad en texto

# DESPUÉS (datos limpios)
nombre,edad,ciudad
Ana Martínez,25,Madrid
Pedro,28,Barcelona      # Edad estimada o valor por defecto
Luis,30,Barcelona       # Convertido a número
```

> 💡 **Regla de oro**: Se dice que el 80% del tiempo de un analista de datos se dedica a limpiar datos.

---

## 4️⃣ **ANÁLISIS** de datos

### ¿Qué es?
Aplicar técnicas estadísticas y matemáticas para **descubrir patrones, tendencias y relaciones** en los datos.

### Tipos de análisis:
- **Estadística descriptiva**: Calcular medias, medianas, porcentajes
- **Segmentación**: Dividir datos en grupos (clientes premium vs básicos)
- **Correlación**: Ver si dos variables están relacionadas (ventas vs temperatura)
- **Comparación**: Antes vs después, grupo A vs grupo B

### Ejemplo práctico:

**Datos de ventas**:
```
Mes,Ventas
Enero,5000
Febrero,5200
Marzo,4800
Abril,6000
Mayo,7500
```

**Análisis**:
- Venta media: 5.700€
- Mes con más ventas: Mayo (7.500€)
- Tendencia: Crecimiento desde marzo
- Incremento Enero-Mayo: +50%

---

## 5️⃣ **VISUALIZACIÓN** de datos

### ¿Qué es?
Representar los datos de forma **gráfica y visual** para que sean más fáciles de entender.

### ¿Por qué visualizar?
🧠 Nuestro cerebro procesa imágenes 60.000 veces más rápido que texto.

Una tabla con 1000 filas es difícil de entender. Un gráfico muestra patrones al instante.

### Tipos de gráficos:

| Gráfico | Cuándo usarlo | Ejemplo |
|---------|---------------|---------|
| 📊 **Barras** | Comparar categorías | Ventas por producto |
| 📈 **Líneas** | Evolución en el tiempo | Visitas web por mes |
| 🥧 **Tarta (Pie)** | Mostrar porcentajes de un total | % de usuarios por país |
| 📉 **Histograma** | Distribución de valores | Edades de los usuarios |
| 🔵 **Dispersión** | Relación entre dos variables | Precio vs ventas |

### Ejemplo práctico:

**Tabla de datos** (difícil de ver tendencias):
```
Mes,Ventas
Ene,5000
Feb,5200
Mar,4800
Abr,6000
May,7500
```

**Gráfico de líneas** (tendencia clara al instante):
```
Ventas
  │
8k┤                    ●
  │                   ╱
6k┤               ●  ╱
  │              ╱  ╱
4k┤  ●───●───●  ╱
  │
  └───────────────────
    E  F  M  A  M
```
➡️ **Se ve claramente**: Ventas estables hasta marzo, luego crecimiento acelerado.

---

## 6️⃣ **INTERPRETACIÓN** de resultados

### ¿Qué es?
Dar **significado y contexto** a los números. Pasar de "qué dicen los datos" a "qué significa esto".

### Del número a la conclusión:

| Dato | Interpretación |
|------|----------------|
| La tasa de rebote es 70% | **Problema**: Los usuarios se van sin interactuar. Revisar la página de inicio. |
| El 80% de ventas vienen del 20% de clientes | **Oportunidad**: Enfocarse en retener a esos clientes VIP. |
| Las ventas suben los viernes | **Acción**: Lanzar ofertas especiales los jueves por la noche. |

### Ejemplo práctico:

**Análisis**:
```python
Carrito abandonado: 65% de los usuarios
```

**Interpretación posible**:
- ❌ "El 65% de usuarios no compran" (descripción)
- ✅ "Algo en el proceso de pago hace que 2 de cada 3 usuarios se vayan. Posibles causas: costes de envío inesperados, proceso largo, falta de opciones de pago." (interpretación)

> 💡 **Importante**: Interpretar requiere conocer el contexto del negocio, no solo los números.

---

## 7️⃣ **TOMA DE DECISIONES**

### ¿Qué es?
Usar las conclusiones del análisis para **actuar y mejorar**.

Este es el objetivo final de todo el proceso.

### Tipos de decisiones:

#### 🚀 Decisiones operativas (día a día)
- "Reponer stock de este producto"
- "Enviar email de recordatorio de carrito abandonado"

#### 📋 Decisiones tácticas (medio plazo)
- "Rediseñar el checkout de la web"
- "Contratar más personal para Navidades"

#### 🎯 Decisiones estratégicas (largo plazo)
- "Expandirse a un nuevo país"
- "Lanzar una nueva línea de productos"

### Ejemplo completo de ciclo:

**Escenario**: Una tienda online nota que las ventas han bajado.

1. **Obtención**: Recopilar datos de ventas, tráfico web, productos
2. **Almacenamiento**: Guardar en base de datos (MySQL)
3. **Limpieza**: Corregir duplicados, completar datos faltantes
4. **Análisis**: Calcular que el 60% de usuarios abandonan en el checkout
5. **Visualización**: Crear gráfico del embudo de conversión
6. **Interpretación**: "El proceso de pago es demasiado largo (5 pasos)"
7. **Decisión**: Reducir el checkout a 2 pasos y añadir más métodos de pago

**Resultado**: ⬆️ Aumento del 25% en conversiones.

---

## 🔁 El ciclo es iterativo

El ciclo no termina nunca:

```
Decisión → Nueva obtención de datos → Análisis de resultados → Nueva decisión
```

**Ejemplo**:
1. Decides enviar emails los martes
2. Obtienes datos de apertura de emails
3. Analizas: Los jueves funcionan mejor
4. Decides cambiar a jueves
5. Obtienes nuevos datos...
6. Y así sucesivamente ♾️

---
# 📋 Tipos de Datos

## 🎯 ¿Por qué es importante conocer los tipos de datos?

No todos los datos son iguales. Según el tipo de dato, podremos hacer unas operaciones u otras.

> 💡 **Analogía**: Es como ingredientes en cocina:
> - Con harina puedes hacer pan (operaciones matemáticas)
> - Con lechuga haces ensalada (operaciones de texto)
> - No puedes sumar lechugas con harina (tipos incompatibles)

**Conocer el tipo de dato nos permite:**
- ✅ Elegir el análisis correcto
- ✅ Hacer cálculos adecuados
- ✅ Crear visualizaciones apropiadas
- ✅ Evitar errores

---

## 🔢 Clasificación principal: Cualitativos vs Cuantitativos

### **Datos CUALITATIVOS** (Categorías)

**Definición**: Describen **cualidades o características**. No son números con los que podamos operar matemáticamente.

**Ejemplos**:
- Color: rojo, azul, verde
- Género: masculino, femenino, otro
- Estado civil: soltero, casado, divorciado
- Categoría de producto: electrónica, ropa, comida
- Nivel de satisfacción: bajo, medio, alto

**Lo que SÍ puedes hacer**:
- Contar cuántos hay de cada categoría
- Calcular porcentajes
- Crear gráficos de barras o tartas

**Lo que NO puedes hacer**:
- Calcular la media de "rojo" y "azul"
- Sumar "soltero" + "casado"

#### Subtipos de datos cualitativos:

##### 🏷️ **Nominales** (sin orden)
Categorías sin jerarquía.

**Ejemplos**:
- País: España, Francia, Italia
- Marca: Nike, Adidas, Puma
- Navegador: Chrome, Firefox, Safari

##### 📊 **Ordinales** (con orden)
Categorías con un orden lógico.

**Ejemplos**:
- Nivel de estudios: Primaria < ESO < Bachiller < Universidad
- Talla de ropa: S < M < L < XL
- Calificación: Suspenso < Aprobado < Notable < Sobresaliente

---

### **Datos CUANTITATIVOS** (Números)

**Definición**: Representan **cantidades medibles**. Son números con los que podemos hacer operaciones matemáticas.

**Ejemplos**:
- Edad: 25 años
- Precio: 49.99€
- Altura: 1.75m
- Número de visitas: 1.523
- Temperatura: 23°C

**Lo que SÍ puedes hacer**:
- Calcular media, mediana, moda
- Sumar, restar, multiplicar
- Crear histogramas, gráficos de líneas

#### Subtipos de datos cuantitativos:

##### 🔢 **Discretos** (números enteros)
Valores que no pueden tener decimales. Se cuentan.

**Ejemplos**:
- Número de estudiantes: 25 (no puede haber 25.5)
- Número de clics: 342
- Cantidad de productos vendidos: 10
- Número de hijos: 2

##### 📏 **Continuos** (pueden tener decimales)
Valores que pueden tener cualquier valor dentro de un rango. Se miden.

**Ejemplos**:
- Peso: 72.5 kg
- Altura: 1.76 m
- Temperatura: 23.4°C
- Tiempo de carga web: 2.37 segundos
- Precio: 49.99€

---

## 📊 Resumen visual

```
                    TIPOS DE DATOS
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
   CUALITATIVOS                      CUANTITATIVOS
   (Categorías)                        (Números)
        │                                   │
   ┌────┴────┐                         ┌────┴────┐
   │         │                         │         │
NOMINALES ORDINALES                 DISCRETOS CONTINUOS
(sin orden)(con orden)               (enteros) (decimales)
   │         │                         │         │
 Colores   Tallas                   Personas  Precios
 Países   Niveles                    Clics    Pesos
```

---

## 🗂️ Tipos de datos en tablas (CSV, Excel, bases de datos)

Cuando trabajamos con datos en formato tabla, encontramos estos tipos:

### 1. **Numéricos** (int, float)

#### Enteros (int)
```python
edad = 25
cantidad = 100
año = 2024
```

#### Decimales (float)
```python
precio = 49.99
temperatura = 23.5
altura = 1.76
```

**Operaciones típicas**:
```python
suma = 10 + 20           # 30
media = (10 + 20) / 2    # 15
```

---

### 2. **Texto** (string, str)

Cualquier cadena de caracteres.

```python
nombre = "Ana García"
email = "ana@mail.com"
descripcion = "Producto de alta calidad"
codigo_postal = "28001"  # ⚠️ Aunque parezca número, es texto
```

**Operaciones típicas**:
```python
nombre_completo = "Ana" + " " + "García"  # "Ana García"
mayusculas = "hola".upper()                # "HOLA"
```

> ⚠️ **Importante**: A veces los números se guardan como texto. Ejemplo: "25" (texto) vs 25 (número)
> ```python
> "25" + "30" = "2530"  # Concatenación de texto
> 25 + 30 = 55           # Suma matemática
> ```

---

### 3. **Fechas** (date, datetime)

Representan momentos en el tiempo.

```python
fecha_nacimiento = "1998-03-15"
fecha_compra = "2024-01-15 14:30:00"
hora = "14:30:00"
```

**Operaciones típicas**:
```python
# Calcular edad
hoy - fecha_nacimiento = 26 años

# Extraer partes
dia = 15
mes = "Enero"
año = 2024
```

**Formatos comunes**:
- `YYYY-MM-DD`: 2024-01-15 (formato ISO, el mejor)
- `DD/MM/YYYY`: 15/01/2024 (formato europeo)
- `MM/DD/YYYY`: 01/15/2024 (formato americano)

---

### 4. **Booleanos** (bool)

Solo pueden tener dos valores: **Verdadero o Falso**.

```python
activo = True
acepta_condiciones = False
mayor_edad = True
```

**Usos típicos**:
- Indicadores: ¿Ha pagado? ¿Está activo?
- Filtros: Mostrar solo usuarios activos
- Condiciones: Si es mayor de edad, permitir acceso

**En datos a veces se representan como**:
- `1` / `0`
- `Sí` / `No`
- `True` / `False`

---

## 📋 Ejemplo completo: Tabla de usuarios

```csv
id,nombre,edad,ciudad,premium,fecha_registro,gasto_total
1,Ana García,25,Madrid,True,2023-01-15,234.50
2,Pedro López,30,Barcelona,False,2023-02-20,89.99
3,Laura Ruiz,22,Valencia,True,2023-03-10,456.00
```

**Análisis de tipos**:

| Campo | Tipo | Clasificación |
|-------|------|---------------|
| `id` | Numérico (int) | Cuantitativo Discreto |
| `nombre` | Texto (string) | Cualitativo Nominal |
| `edad` | Numérico (int) | Cuantitativo Discreto |
| `ciudad` | Texto (string) | Cualitativo Nominal |
| `premium` | Booleano (bool) | Cualitativo Nominal |
| `fecha_registro` | Fecha (date) | - |
| `gasto_total` | Numérico (float) | Cuantitativo Continuo |

---

## 🎯 ¿Qué análisis podemos hacer según el tipo?

### Con datos **cualitativos**:
✅ Frecuencias (¿cuántos hay de cada categoría?)
```
Madrid: 35%
Barcelona: 25%
Valencia: 20%
```

✅ Moda (¿cuál es la categoría más frecuente?)
```
Ciudad más común: Madrid
```

✅ Gráficos de barras o tartas

---

### Con datos **cuantitativos**:
✅ Media, mediana, moda
```
Edad media: 27 años
```

✅ Máximo, mínimo, rango
```
Edad más baja: 18
Edad más alta: 65
```

✅ Desviación estándar (variabilidad)

✅ Histogramas, gráficos de líneas

---

### Con **fechas**:
✅ Análisis temporal (evolución)
```
Usuarios por mes
```

✅ Cálculo de duración
```
Tiempo desde el registro: 6 meses
```

✅ Detección de patrones estacionales
```
Más ventas en diciembre
```

---

## ⚠️ Errores comunes con tipos de datos

### ❌ Error 1: Tratar texto como número
```python
codigo_postal = "28001"
codigo_postal + 1  # ❌ Error: no se puede sumar texto
```

**Solución**: Convertir el tipo
```python
codigo_postal = int("28001")  # Ahora es número
codigo_postal + 1  # ✅ 28002
```

---

### ❌ Error 2: Tratar números como categorías
```python
# Tienes códigos de producto: 1, 2, 3
media_producto = (1 + 2 + 3) / 3  # ❌ No tiene sentido
```

**Solución**: Tratarlos como texto/categorías
```python
productos = ["P1", "P2", "P3"]  # Mejor como categorías
```

---

### ❌ Error 3: Fechas en formato incorrecto
```python
fecha = "15/01/2024"    # Texto, no fecha
fecha + 10  # ❌ No puedes sumar 10 días a texto
```

**Solución**: Convertir a formato fecha
```python
from datetime import datetime
fecha = datetime.strptime("15/01/2024", "%d/%m/%Y")
fecha + timedelta(days=10)  # ✅ 25/01/2024
```

---
# 📊 Estadística Descriptiva Básica

## 🎯 ¿Qué es la estadística descriptiva?

La **estadística descriptiva** es el conjunto de técnicas que usamos para **resumir y describir** las características principales de un conjunto de datos.

> 💡 **Analogía**: Es como hacer un resumen de un libro de 300 páginas en una sola hoja.
> En lugar de leer todas las notas de 100 alumnos, calculas la media y ya sabes el nivel general.

**Objetivo**: Entender rápidamente un conjunto de datos sin tener que ver todos los valores uno por uno.

---

## 📐 Medidas de Tendencia Central

Nos dicen "alrededor de qué valor se concentran los datos".

### 1️⃣ **MEDIA** (Promedio)

**¿Qué es?**
La suma de todos los valores dividida por el número total de valores.

**Fórmula**:
$$\text{Media} = \frac{\text{Suma de todos los valores}}{\text{Cantidad de valores}}$$

**Ejemplo 1**: Notas de un examen
```
Notas: 5, 7, 8, 6, 9

Media = (5 + 7 + 8 + 6 + 9) / 5 = 35 / 5 = 7
```
➡️ **Interpretación**: La nota media es 7.

**Ejemplo 2**: Ventas diarias
```
Ventas (€): 100, 150, 200, 180, 120

Media = (100 + 150 + 200 + 180 + 120) / 5 = 750 / 5 = 150€
```
➡️ **Interpretación**: En promedio vendes 150€ al día.

**⚠️ Cuidado con la media**:
La media es sensible a **valores extremos**.

```
Salarios (€): 1200, 1300, 1250, 1400, 15000

Media = (1200 + 1300 + 1250 + 1400 + 15000) / 5 = 4030€
```
➡️ ❌ La media dice 4030€, pero 4 de 5 personas ganan menos de 1500€.
➡️ El salario de 15000€ distorsiona la media.

---

### 2️⃣ **MEDIANA**

**¿Qué es?**
El valor que está **en el centro** cuando ordenamos los datos de menor a mayor.

**Cómo calcularla**:
1. Ordena los valores
2. Si hay cantidad impar de valores: coge el del centro
3. Si hay cantidad par: calcula la media de los dos centrales

**Ejemplo 1**: Cantidad impar de valores
```
Notas: 5, 7, 8, 6, 9

Paso 1 - Ordenar: 5, 6, 7, 8, 9
Paso 2 - Coger el central: 7

Mediana = 7
```

**Ejemplo 2**: Cantidad par de valores
```
Ventas: 100, 150, 200, 180, 120, 140

Paso 1 - Ordenar: 100, 120, 140, 150, 180, 200
Paso 2 - Los dos centrales: 140 y 150
Paso 3 - Media de ambos: (140 + 150) / 2 = 145

Mediana = 145€
```

**✅ Ventaja de la mediana**:
NO es sensible a valores extremos.

```
Salarios (€): 1200, 1300, 1250, 1400, 15000

Ordenar: 1200, 1250, 1300, 1400, 15000
Mediana = 1300€
```
➡️ ✅ La mediana (1300€) representa mejor el salario típico que la media (4030€).

---

### 3️⃣ **MODA**

**¿Qué es?**
El valor que **aparece más veces** en el conjunto de datos.

**Ejemplo 1**: Notas
```
Notas: 5, 7, 8, 7, 9, 7, 6

Frecuencias:
5 → 1 vez
6 → 1 vez
7 → 3 veces  ← Más frecuente
8 → 1 vez
9 → 1 vez

Moda = 7
```

**Ejemplo 2**: Tallas de camiseta vendidas
```
Ventas: S, M, L, M, M, L, S, M, XL

Frecuencias:
S → 2 veces
M → 4 veces  ← Más frecuente
L → 2 veces
XL → 1 vez

Moda = M
```
➡️ **Interpretación**: La talla M es la más vendida.

**💡 Casos especiales**:
- **Sin moda**: Todos los valores aparecen la misma cantidad de veces
- **Bimodal**: Dos valores con la misma frecuencia máxima
- **Multimodal**: Más de dos valores con frecuencia máxima

---

### 🤔 ¿Cuándo usar cada una?

| Medida | Cuándo usarla | Ejemplo |
|--------|---------------|---------|
| **Media** | Datos sin valores extremos | Notas de clase homogéneas |
| **Mediana** | Datos con valores extremos | Precios de viviendas (hay muy caras) |
| **Moda** | Datos categóricos o discretos | Talla más vendida, color favorito |

**Ejemplo práctico**:
```
Precios de pisos en una zona (€):
150k, 160k, 155k, 600k, 165k

Media = 246k    ← Distorsionada por el piso de 600k
Mediana = 160k  ← Mejor representación
Moda = No hay   ← Todos diferentes
```
➡️ **Conclusión**: Usa la mediana para reportar el "precio típico".

---

## 📏 Medidas de Dispersión

Nos dicen "qué tan separados están los datos".

### 1️⃣ **RANGO** (Máximo - Mínimo)

**¿Qué es?**
La diferencia entre el valor más alto y el más bajo.

**Fórmula**:
$$\text{Rango} = \text{Máximo} - \text{Mínimo}$$

**Ejemplo**:
```
Temperaturas de la semana (°C): 15, 18, 20, 22, 17, 19, 21

Máximo = 22°C
Mínimo = 15°C
Rango = 22 - 15 = 7°C
```
➡️ **Interpretación**: La temperatura varió 7 grados durante la semana.

---

### 2️⃣ **DESVIACIÓN ESTÁNDAR** (σ)

**¿Qué es?**
Mide **cuánto se alejan los datos de la media** en promedio.

- **Desviación baja** ➡️ Datos concentrados cerca de la media
- **Desviación alta** ➡️ Datos muy dispersos

**Explicación intuitiva**:

Imagina dos clases:

**Clase A**: Notas → 6, 6, 7, 7, 6
- Media = 6.4
- Todos cerca de la media
- **Desviación baja** → Clase homogénea

**Clase B**: Notas → 1, 3, 7, 9, 10
- Media = 6
- Valores muy dispersos
- **Desviación alta** → Clase heterogénea

**Fórmula** (no te preocupes, Python lo calcula automáticamente):
$$\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$$

**Ejemplo con cálculo manual simplificado**:
```
Datos: 2, 4, 6, 8

Media = (2 + 4 + 6 + 8) / 4 = 5

Diferencias con la media:
2 - 5 = -3  →  (-3)² = 9
4 - 5 = -1  →  (-1)² = 1
6 - 5 = 1   →  (1)² = 1
8 - 5 = 3   →  (3)² = 9

Suma de diferencias al cuadrado = 9 + 1 + 1 + 9 = 20
Media de esas diferencias = 20 / 4 = 5
Desviación estándar = √5 ≈ 2.24
```

**Interpretación**:
- Desviación = 2.24
- Los datos se alejan **en promedio 2.24 unidades** de la media (5)

---

### 🔍 Valores importantes: Máximo, Mínimo

**Máximo**: El valor más grande del conjunto.
**Mínimo**: El valor más pequeño del conjunto.

```
Ventas (€): 100, 150, 200, 180, 120, 90

Mínimo = 90€   → Peor día
Máximo = 200€  → Mejor día
```

---

## 📊 Ejemplo completo: Análisis de salarios

```
Salarios mensuales (€): 1200, 1300, 1250, 1400, 1350, 1280, 1500

1️⃣ Media
(1200+1300+1250+1400+1350+1280+1500) / 7 = 1325.71€

2️⃣ Mediana
Ordenar: 1200, 1250, 1280, 1300, 1350, 1400, 1500
Central: 1300€

3️⃣ Moda
Todos diferentes → No hay moda

4️⃣ Máximo y Mínimo
Máximo = 1500€
Mínimo = 1200€

5️⃣ Rango
1500 - 1200 = 300€

6️⃣ Desviación estándar (calculada con Python)
Aprox. 95.9€
```

**📋 Interpretación completa**:
- Salario medio: **1325.71€**
- Salario típico (mediana): **1300€**
- Los salarios varían hasta **300€** entre el más bajo y el más alto
- En promedio, los salarios se alejan **95.9€** del salario medio
- **Conclusión**: Los salarios son bastante homogéneos (baja dispersión)

---

## 🎯 ¿Cuándo usar cada medida?

### Para responder "¿Cuál es el valor típico?"
- Usa la **media** si no hay valores extremos
- Usa la **mediana** si hay valores extremos
- Usa la **moda** si trabajas con categorías

### Para responder "¿Cuánto varían los datos?"
- Usa el **rango** para una idea rápida
- Usa la **desviación estándar** para una medida precisa

---

## 💡 Ejemplos aplicados

### Ejemplo 1: Análisis de edad de usuarios web

```
Edades: 22, 25, 28, 30, 24, 26, 27, 65

Media = 30.9 años     ← Distorsionada por el de 65
Mediana = 26.5 años   ← Mejor representación
Moda = No hay
```
➡️ **Decisión**: Reporta la mediana como "edad típica del usuario".

---

### Ejemplo 2: Tiempos de carga de una web

```
Tiempos (segundos): 1.2, 1.5, 1.3, 1.4, 1.2, 8.5

Media = 2.52s         ← Distorsionada por el 8.5s
Mediana = 1.35s       ← Representa mejor el rendimiento normal
Desviación = 2.84s    ← Alta variabilidad (hay un valor atípico)
```
➡️ **Decisión**: Investigar qué causó ese pico de 8.5s (posible error o problema técnico).

---

### Ejemplo 3: Productos vendidos por día

```
Ventas: 10, 12, 11, 10, 15, 10, 13

Media = 11.57
Mediana = 11
Moda = 10              ← Vendes 10 unidades más frecuentemente
Desviación = 1.72      ← Ventas consistentes (baja dispersión)
```
➡️ **Decisión**: Mantén stock de al menos 12 unidades diarias (por encima de la media).

---
# 🧹 Calidad del Dato

## 🎯 ¿Por qué es importante la calidad del dato?

La calidad de los datos es **fundamental** para obtener análisis correctos y tomar buenas decisiones.

> 💡 **Regla de oro**: "Basura entra, basura sale" (Garbage In, Garbage Out)
> 
> Si analizas datos de mala calidad, obtendrás conclusiones incorrectas.

**Ejemplo real**:
Una tienda online calcula que sus clientes gastan en promedio **250€**. Pero resulta que hay **100 pedidos con precio = 0€** por un error en la base de datos.
- ❌ Análisis con datos sucios: Media = 250€
- ✅ Análisis con datos limpios: Media = 320€

➡️ **Consecuencia**: Decisiones empresariales equivocadas (mal inventario, malas campañas...)

---

## 🚨 Problemas comunes de calidad

### 1️⃣ **DATOS NULOS O VACÍOS** (Missing Data)

**¿Qué son?**
Valores que **faltan** en el conjunto de datos.

**Causas**:
- Usuario no rellenó un campo del formulario
- Error en la recopilación de datos
- Sensor que dejó de funcionar
- Importación incorrecta desde otra base de datos

**Ejemplo en una tabla**:
```csv
nombre,edad,ciudad,email
Ana García,25,Madrid,ana@mail.com
Pedro López,,Barcelona,pedro@mail.com    ← Falta edad
María Ruiz,30,,maria@mail.com            ← Falta ciudad
Luis Pérez,28,Valencia,                  ← Falta email
```

#### ¿Cómo se representan?
- `NaN` (Not a Number)
- `None`
- `NULL`
- Campo vacío: ` ` (espacio en blanco)
- Cadena vacía: `""`

#### ¿Qué hacer con datos nulos?

##### Opción 1: **Eliminar** la fila completa
```python
# ANTES
nombre,edad,ciudad
Ana,25,Madrid
Pedro,,Barcelona
María,30,Valencia

# DESPUÉS (eliminamos fila con edad nula)
nombre,edad,ciudad
Ana,25,Madrid
María,30,Valencia
```

⚠️ **Cuidado**: Solo hazlo si:
- Tienes muchos datos y puedes permitirte perder algunos
- El dato faltante es crítico para tu análisis

##### Opción 2: **Rellenar** con un valor por defecto
```python
# Rellenar edad nula con la media (27.5)
nombre,edad,ciudad
Ana,25,Madrid
Pedro,27.5,Barcelona  ← Rellenado con media
María,30,Valencia
```

##### Opción 3: **Rellenar** con categoría especial
```python
# Para datos categóricos
ciudad: Madrid, Barcelona, Desconocido
```

##### Opción 4: **Mantener** y marcar como desconocido
Analizar por separado los casos con datos faltantes.

---

### 2️⃣ **DATOS DUPLICADOS**

**¿Qué son?**
Filas repetidas en el conjunto de datos.

**Causas**:
- Usuario envió el formulario dos veces
- Error al importar datos
- Problema en la base de datos (falta clave primaria)

**Ejemplo**:
```csv
email,nombre,fecha_registro
ana@mail.com,Ana García,2024-01-15
pedro@mail.com,Pedro López,2024-01-20
ana@mail.com,Ana García,2024-01-15  ← DUPLICADO exacto
```

#### Tipos de duplicados:

##### **Duplicados exactos** (fáciles de detectar)
```csv
id,nombre,edad
1,Ana,25
2,Pedro,30
1,Ana,25  ← Idéntico
```

##### **Duplicados parciales** (más difíciles)
```csv
email,nombre
ana@mail.com,Ana García
ana@mail.com,ANA GARCIA     ← Mismo email, diferente formato
ana@mail.com,A. García       ← Mismo email, nombre abreviado
```

#### ¿Qué hacer?

##### Opción 1: **Eliminar duplicados exactos**
```python
# ANTES
Ana,25
Pedro,30
Ana,25

# DESPUÉS
Ana,25
Pedro,30
```

##### Opción 2: **Unificar duplicados parciales**
```python
# ANTES
ana@mail.com → Ana García
ana@mail.com → ANA GARCIA

# DESPUÉS (mantener el primero o el más completo)
ana@mail.com → Ana García
```

---

### 3️⃣ **ERRORES DE FORMATO**

**¿Qué son?**
Datos correctos pero expresados de forma **inconsistente**.

#### Ejemplo 1: Fechas en diferentes formatos
```csv
fecha_nacimiento
15/03/1998        ← DD/MM/YYYY
1998-03-15        ← YYYY-MM-DD (ISO)
15-marzo-1998     ← DD-mes-YYYY
03/15/1998        ← MM/DD/YYYY (americano)
```

**Problema**: Python no puede interpretar correctamente. Debes **estandarizar**.

**Solución**:
```python
# Convertir todo a formato ISO (YYYY-MM-DD)
1998-03-15
1998-03-15
1998-03-15
1998-03-15
```

---

#### Ejemplo 2: Texto con mayúsculas/minúsculas inconsistentes
```csv
ciudad
Madrid
madrid
MADRID
MaDrId
```

**Problema**: Python ve 4 ciudades diferentes.

**Solución**:
```python
# Normalizar a formato único
Madrid
Madrid
Madrid
Madrid
```

---

#### Ejemplo 3: Números como texto
```csv
precio
"49.99"     ← Texto (entre comillas)
49.99       ← Número
"50,00"     ← Texto con coma europea
```

**Problema**: No puedes calcular la media de texto.

**Solución**:
```python
# Convertir todo a número (float)
49.99
49.99
50.00
```

---

#### Ejemplo 4: Espacios en blanco
```csv
email
" ana@mail.com"      ← Espacio al inicio
"pedro@mail.com "    ← Espacio al final
" luis@mail.com "    ← Espacios en ambos lados
```

**Solución**:
```python
# Eliminar espacios (trim/strip)
"ana@mail.com"
"pedro@mail.com"
"luis@mail.com"
```

---

### 4️⃣ **VALORES ATÍPICOS** (Outliers)

**¿Qué son?**
Valores que se alejan **anormalmente** del resto de los datos.

**Pueden ser**:
- ✅ **Válidos**: Casos reales pero excepcionales
- ❌ **Errores**: Datos mal introducidos o capturados

#### Ejemplo 1: Edad
```csv
edad
25, 30, 28, 22, 150, 27, 29
                ↑
            Outlier (probablemente error)
```

**Análisis**:
- Edad 150 años es **imposible** → Error de introducción
- Probablemente quisieron poner 15 o se confundieron

---

#### Ejemplo 2: Precio de producto
```csv
precio
49.99, 59.99, 45.00, 4999.00, 52.00
                     ↑
            Outlier (¿error o producto premium?)
```

**Análisis**:
- Puede ser un error (falta un punto decimal: 49.99)
- O puede ser un producto premium real

➡️ **Importante**: Debes **investigar** antes de decidir.

---

#### Ejemplo 3: Ventas diarias
```csv
ventas
100, 120, 110, 115, 1000, 105, 118
                    ↑
            Outlier (¿Black Friday? ¿Error?)
```

**Análisis**:
- Puede ser un día especial (promoción, evento)
- O puede ser un error de registro

---

#### ¿Cómo detectar outliers?

##### Método 1: **Visualización** (gráficos)
```
    │
    │                                ●  ← Outlier muy separado
1000│
    │
 500│
    │
    │  ● ● ● ● ● ●  ← Datos normales agrupados
    └────────────────
```

##### Método 2: **Rango intercuartílico (IQR)**
Valores que están muy alejados del 50% central de los datos.

##### Método 3: **Desviación estándar**
Valores que se alejan más de 2-3 desviaciones estándar de la media.

**Regla práctica**:
```python
Si valor > media + 3×desviación → Posible outlier
Si valor < media - 3×desviación → Posible outlier
```

---

#### ¿Qué hacer con outliers?

##### Opción 1: **Investigar** si es error o dato real
```
edad = 150 → Error evidente → Eliminar o corregir
ventas = 1000 en Black Friday → Real → Mantener
```

##### Opción 2: **Mantener** y analizar por separado
```python
# Análisis general (sin outliers)
media_ventas_normal = 110€

# Análisis de días especiales (con outliers)
media_dias_especiales = 850€
```

##### Opción 3: **Eliminar** si distorsionan el análisis
Solo si estás seguro de que son errores.

##### Opción 4: **Transformar** (técnicas avanzadas)
Aplicar logaritmos u otras transformaciones para reducir su impacto.

---

## 🛠️ Proceso de verificación de calidad

### Checklist antes de analizar datos:

✅ **1. Revisar valores nulos**
```
¿Cuántas filas tienen datos faltantes?
¿En qué columnas?
¿Podemos rellenarlos o debemos eliminarlos?
```

✅ **2. Buscar duplicados**
```
¿Hay filas repetidas?
¿Hay duplicados parciales (mismo email, diferente nombre)?
```

✅ **3. Verificar formatos**
```
¿Las fechas están en el mismo formato?
¿Los textos están normalizados (mayúsculas/minúsculas)?
¿Los números son números o texto?
```

✅ **4. Detectar outliers**
```
¿Hay valores sospechosamente altos o bajos?
¿Son errores o casos excepcionales reales?
```

✅ **5. Validar rangos lógicos**
```
Edad: ¿Entre 0 y 120?
Precio: ¿Mayor que 0?
Porcentaje: ¿Entre 0 y 100?
```

---

## 📊 Ejemplo completo: Limpieza de datos de ventas

### DATOS ORIGINALES (sucios):
```csv
id,producto,precio,cantidad,fecha
1,Laptop,899.99,1,2024-01-15
2,Mouse,"25.99",2,15/01/2024
3,Teclado,45.00,0,2024-01-16
4,Laptop,899.99,1,2024-01-15  ← Duplicado
5,Monitor,,1,2024/01/17        ← Precio nulo
6,Webcam,1500.00,1,2024-01-18  ← Outlier sospechoso
7,Auriculares,  30.00 ,2,16-ene-2024  ← Espacios
```

### PROBLEMAS DETECTADOS:
1. Fila 2: Precio como texto ("25.99")
2. Fila 3: Cantidad = 0 (¿venta válida?)
3. Fila 4: Duplicado de fila 1
4. Fila 5: Precio nulo
5. Fila 6: Precio 1500€ (webcams cuestan 50-100€ normalmente)
6. Fila 7: Espacios en precio, formato fecha diferente
7. Fechas en 3 formatos diferentes

### DATOS LIMPIOS:
```csv
id,producto,precio,cantidad,fecha
1,Laptop,899.99,1,2024-01-15
2,Mouse,25.99,2,2024-01-15
3,Monitor,75.00,1,2024-01-17   ← Precio rellenado con media de monitores
6,Webcam,150.00,1,2024-01-18   ← Precio corregido (quitamos un 0)
7,Auriculares,30.00,2,2024-01-16
```

**Acciones tomadas**:
✅ Convertir precio de texto a número (fila 2)  
✅ Eliminar venta con cantidad 0 (fila 3)  
✅ Eliminar duplicado (fila 4)  
✅ Rellenar precio nulo con valor típico (fila 5)  
✅ Corregir outlier verificando fuente (fila 6)  
✅ Eliminar espacios y unificar formato fecha (fila 7)  

---
