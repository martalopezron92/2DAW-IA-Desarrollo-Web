# U1 - ¿Qué es la inteligencia artificial?

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad, el estudiante será capaz de:

- **Definir** qué es la inteligencia artificial y sus características principales
- **Identificar** los diferentes tipos de IA y sus aplicaciones
- **Analizar** la evolución histórica de la IA desde sus orígenes hasta la actualidad
- **Relacionar** las aplicaciones de IA con casos de uso en desarrollo web
- **Evaluar** el impacto de la IA en la sociedad y el mundo profesional

## ⏱️ Duración estimada

**6 horas** distribuidas en 2 semanas (3 sesiones de 2 horas cada una)

## 📚 Contenidos

### 1. Definición y conceptos fundamentales

#### ¿Qué es la inteligencia artificial?

La **Inteligencia Artificial (IA)** es la capacidad de las máquinas para realizar tareas que tradicionalmente requieren inteligencia humana, como:

- **Razonamiento**: Proceso de llegar a conclusiones lógicas
- **Aprendizaje**: Capacidad de mejorar el rendimiento con la experiencia
- **Percepción**: Interpretar información del entorno
- **Comprensión del lenguaje**: Procesar y generar lenguaje natural
- **Resolución de problemas**: Encontrar soluciones a situaciones complejas

#### Características clave de la IA

1. **Automatización inteligente**: Va más allá de la automatización simple
2. **Adaptabilidad**: Puede ajustarse a nuevas situaciones
3. **Procesamiento de grandes volúmenes de datos**: Capacidad de análisis masivo
4. **Patrones complejos**: Identifica relaciones no evidentes para humanos
5. **Mejora continua**: Aprende y se optimiza con el tiempo

### 2. Tipos de inteligencia artificial

#### Por capacidad cognitiva

**IA Débil (Narrow AI)**
- Diseñada para tareas específicas
- No tiene conciencia general
- Ejemplos: Siri, Google Translate, recomendadores de Netflix
- **Estado actual**: La mayoría de IA comercial

**IA Fuerte (General AI)**
- Inteligencia equivalente a la humana en todos los dominios
- Capacidad de razonamiento general
- **Estado actual**: Objetivo a largo plazo, no alcanzado

**Super IA**
- Supera la inteligencia humana en todos los aspectos
- **Estado actual**: Concepto teórico

#### Por funcionalidad

**IA Reactiva**
- Responde a estímulos del entorno
- No tiene memoria de experiencias pasadas
- Ejemplo: Deep Blue (ajedrez)

**IA con Memoria Limitada**
- Usa experiencias pasadas para tomar decisiones
- Ejemplo: Coches autónomos, ChatGPT

**IA con Teoría de la Mente**
- Comprende emociones y pensamientos ajenos
- **Estado actual**: En desarrollo

**IA Autoconsciente**
- Tiene conciencia de sí misma
- **Estado actual**: Concepto teórico

### 3. Historia de la inteligencia artificial

#### Prehistoria (1940-1956)

**1943**: Warren McCulloch y Walter Pitts
- Primer modelo matemático de neurona artificial
- Base para las redes neuronales

**1950**: Alan Turing
- Test de Turing: criterio para determinar si una máquina puede "pensar"
- Artículo "Computing Machinery and Intelligence"

#### Nacimiento oficial (1956)

**Conferencia de Dartmouth**
- Acuña el término "Artificial Intelligence"
- Participantes: John McCarthy, Marvin Minsky, Allen Newell, Herbert Simon
- Optimismo inicial: "resolver IA en un verano"

#### Primera época dorada (1957-1974)

**Logros importantes**:
- **1957**: Perceptrón de Frank Rosenblatt
- **1966**: ELIZA (Joseph Weizenbaum) - primer chatbot
- **1969**: SHAKEY - primer robot móvil inteligente

#### Primer invierno de la IA (1974-1980)

**Causas del estancamiento**:
- Limitaciones computacionales
- Problemas de escalabilidad
- Expectativas no cumplidas
- Reducción de financiación

#### Resurgimiento (1980-1987)

**Sistemas expertos**:
- MYCIN (diagnóstico médico)
- DENDRAL (análisis químico)
- Comercialización de la IA

#### Segundo invierno (1987-1993)

**Nuevas limitaciones**:
- Hardware insuficiente
- Coste de mantenimiento de sistemas expertos
- Competencia de PCs más baratos

#### Renacimiento moderno (1993-2011)

**Avances clave**:
- **1997**: Deep Blue vence a Kasparov en ajedrez
- **2005**: DARPA Grand Challenge (coches autónomos)
- **2011**: Watson gana en Jeopardy!

#### Era del Deep Learning (2012-presente)

**Revolución actual**:
- **2012**: AlexNet revoluciona visión por computador
- **2016**: AlphaGo vence al campeón mundial de Go
- **2018**: BERT transforma el procesamiento de lenguaje natural
- **2020**: GPT-3 demuestra capacidades generativas impresionantes
- **2022**: ChatGPT democratiza la IA conversacional
- **2024**: Modelos multimodales (texto, imagen, audio)

### 4. Aplicaciones actuales de la IA

#### En desarrollo web

**Frontend**
- **Personalización**: Contenido adaptado al usuario
- **UX inteligente**: Interfaces que se adaptan al comportamiento
- **Accesibilidad**: Herramientas de asistencia automática
- **Testing**: Pruebas automatizadas inteligentes

**Backend**
- **APIs inteligentes**: Servicios con capacidades de IA
- **Optimización**: Rendimiento adaptativo
- **Seguridad**: Detección de amenazas en tiempo real
- **Escalabilidad**: Gestión automática de recursos

**Casos de uso específicos**
- **Chatbots**: Atención al cliente automatizada
- **Recomendadores**: Sugerencias personalizadas
- **Búsqueda semántica**: Resultados más relevantes
- **Generación de contenido**: Textos e imágenes automáticas
- **Análisis de sentimientos**: Comprensión de feedback
- **Detección de fraude**: Transacciones seguras

#### En otras industrias

**Salud**
- Diagnóstico por imagen médica
- Descubrimiento de fármacos
- Medicina personalizada

**Finanzas**
- Trading algorítmico
- Evaluación de riesgo crediticio
- Detección de lavado de dinero

**Transporte**
- Vehículos autónomos
- Optimización de rutas
- Gestión de tráfico

**Entretenimiento**
- Generación de música y arte
- Efectos especiales cinematográficos
- Videojuegos con NPCs inteligentes

## 🔍 Ejemplos prácticos

### Ejemplo 1: IA en Netflix

**Problema**: ¿Cómo recomendar contenido relevante a 200+ millones de usuarios?

**Solución IA**:
```python
# Algoritmo simplificado de recomendación
def recomendar_contenido(usuario, historial_visualizacion):
    # 1. Análisis del perfil del usuario
    preferencias = analizar_gustos(historial_visualizacion)
    
    # 2. Filtrado colaborativo
    usuarios_similares = encontrar_usuarios_similares(usuario)
    
    # 3. Filtrado basado en contenido
    contenido_similar = buscar_contenido_similar(preferencias)
    
    # 4. Combinación de enfoques
    recomendaciones = combinar_algoritmos(usuarios_similares, contenido_similar)
    
    return recomendaciones
```

**Impacto**: 80% del contenido visto en Netflix proviene de recomendaciones

### Ejemplo 2: IA en comercio electrónico

**Problema**: Optimizar precios dinámicamente según demanda, competencia y inventario

**Solución IA**:
- **Machine Learning**: Predice demanda futura
- **Análisis competitivo**: Monitorea precios de la competencia
- **Optimización**: Ajusta precios en tiempo real

**Resultado**: Incremento del 25% en beneficios

### Ejemplo 3: IA en desarrollo web

**Herramientas actuales**:
- **GitHub Copilot**: Autocompletado inteligente de código
- **Figma**: Generación automática de diseños
- **Vercel**: Optimización automática de performance
- **Cloudflare**: Protección inteligente contra ataques

## 💡 Mini-ejercicios

### Ejercicio 1: Clasificación de IA
Clasifica las siguientes aplicaciones según el tipo de IA:

1. **Google Translate**: [ ] IA Débil [ ] IA Fuerte
2. **Asistente médico que diagnostica cualquier enfermedad**: [ ] IA Débil [ ] IA Fuerte
3. **Sistema de recomendación de Spotify**: [ ] IA Débil [ ] IA Fuerte
4. **Robot que entiende emociones humanas**: [ ] Reactiva [ ] Memoria Limitada [ ] Teoría de la Mente

### Ejercicio 2: Línea temporal
Ordena cronológicamente estos hitos:
- [ ] ChatGPT se hace viral
- [ ] Test de Turing propuesto  
- [ ] Deep Blue vence a Kasparov
- [ ] Conferencia de Dartmouth
- [ ] AlphaGo vence al campeón de Go

### Ejercicio 3: Identificación de aplicaciones web
Identifica qué tipo de IA usan estas funcionalidades web:

1. **Autocompletado de búsqueda en Google**
2. **Filtro de spam en Gmail**
3. **Reconocimiento facial en fotos de Facebook**
4. **Chatbot de atención al cliente**
5. **Sugerencias de conexión en LinkedIn**

## 📝 Quiz de autoevaluación

### Pregunta 1
¿Cuál es la principal diferencia entre IA débil e IA fuerte?

**a)** La IA débil es más antigua que la IA fuerte  
**b)** La IA débil está especializada en tareas específicas, la IA fuerte tiene inteligencia general  
**c)** La IA débil usa menos recursos computacionales  
**d)** No hay diferencia real entre ambas

### Pregunta 2
¿Qué evento marca el nacimiento oficial de la IA?

**a)** El Test de Turing (1950)  
**b)** La invención del perceptrón (1957)  
**c)** La Conferencia de Dartmouth (1956)  
**d)** La victoria de Deep Blue (1997)

### Pregunta 3
¿Cuál de estas NO es una característica de la IA moderna?

**a)** Procesamiento de grandes volúmenes de datos  
**b)** Conciencia y emociones como los humanos  
**c)** Capacidad de aprendizaje y mejora  
**d)** Identificación de patrones complejos

### Pregunta 4
En el contexto del desarrollo web, ¿cuál es un ejemplo de IA reactiva?

**a)** Un chatbot que recuerda conversaciones anteriores  
**b)** Un sistema que ajusta precios según el historial de compras  
**c)** Un captcha que responde a la entrada actual del usuario  
**d)** Un recomendador que aprende de preferencias pasadas

### Pregunta 5
¿Qué porcentaje aproximado del contenido visto en Netflix proviene de su sistema de recomendación por IA?

**a)** 40%  
**b)** 60%  
**c)** 80%  
**d)** 95%

## 🔗 Recursos adicionales

### Lecturas recomendadas
- **"Artificial Intelligence: A Modern Approach"** - Stuart Russell & Peter Norvig
- **"The Master Algorithm"** - Pedro Domingos
- **"Life 3.0"** - Max Tegmark

### Videos y documentales
- **"AlphaGo"** (2017) - Documental sobre IA y el juego de Go
- **"The Age of AI"** - Serie de YouTube Originals
- **"AI Explained"** - Canal de YouTube educativo

### Recursos online
- **Coursera**: "Machine Learning" por Andrew Ng
- **edX**: "Introduction to Artificial Intelligence" por MIT
- **Khan Academy**: "Intro to Algorithms"

### Papers históricos
- **"Computing Machinery and Intelligence"** - Alan Turing (1950)
- **"A Proposal for the Dartmouth Summer Research Project"** - McCarthy et al. (1955)
- **"Attention Is All You Need"** - Vaswani et al. (2017)

## 🎯 Evaluación de la unidad

Esta unidad se evalúa mediante:
- **P01**: Línea temporal interactiva + mapa mental conceptual
- **Participación**: En debates y actividades colaborativas
- **Mini-quiz**: Evaluación formativa de conceptos clave

## ➡️ Siguiente unidad

[U2 - Ética, sesgos y legislación en IA](./U2_Etica_Sesgos_Legislacion.md)

---

## 🔑 Soluciones a ejercicios

### Mini-ejercicio 1
1. IA Débil ✓, 2. IA Fuerte ✓, 3. IA Débil ✓, 4. Teoría de la Mente ✓

### Mini-ejercicio 2
Test de Turing (1950) → Conferencia de Dartmouth (1956) → Deep Blue vence a Kasparov (1997) → AlphaGo vence al campeón de Go (2016) → ChatGPT se hace viral (2022)

### Quiz
1. b) ✓, 2. c) ✓, 3. b) ✓, 4. c) ✓, 5. c) ✓

---

**Unidad elaborada por**: Departamento de Informática y Comunicaciones  
**Última actualización**: 26 de octubre de 2025