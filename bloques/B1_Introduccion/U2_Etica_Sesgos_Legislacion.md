# U2 - Ética, sesgos y legislación en IA

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad, el estudiante será capaz de:

- **Analizar** las implicaciones éticas del uso de IA en aplicaciones web
- **Identificar** diferentes tipos de sesgos algorítmicos y sus consecuencias
- **Evaluar** el marco legal actual que regula la IA (GDPR, Ley de IA de la UE)
- **Aplicar** principios de IA responsable en el desarrollo de proyectos
- **Argumentar** sobre dilemas éticos en sistemas automatizados de decisión

## ⏱️ Duración estimada

**9 horas** distribuidas en 3 semanas (3 sesiones de 3 horas cada una)

## 📚 Contenidos

### 1. Principios éticos en IA

#### Los cinco pilares de la IA ética

**1. Fairness (Equidad)**
- Tratamiento justo para todos los grupos demográficos
- Ausencia de discriminación sistemática
- Igualdad de oportunidades en los resultados

**2. Accountability (Responsabilidad)**
- Capacidad de explicar decisiones algorítmicas
- Responsabilidad clara en caso de errores
- Mecanismos de supervisión y control

**3. Transparency (Transparencia)**
- Claridad sobre cómo funcionan los algoritmos
- Información accesible para usuarios finales
- Documentación de procesos de entrenamiento

**4. Explainability (Explicabilidad)**
- Capacidad de interpretar resultados
- Comunicación comprensible de decisiones
- Trazabilidad del razonamiento algorítmico

**5. Privacy (Privacidad)**
- Protección de datos personales
- Minimización de recolección de información
- Seguridad en el almacenamiento y procesamiento

#### Dilemas éticos frecuentes

**Caso 1: Sistema de contratación automático**
```
Problema: Un algoritmo de selección de CVs descarta 
sistemáticamente candidatas mujeres para puestos técnicos.

Análisis ético:
- ¿Es el algoritmo sesgado o refleja sesgos históricos?
- ¿Quién es responsable: desarrolladores, empresa, datos?
- ¿Cómo balancear eficiencia vs equidad?
```

**Caso 2: Recomendador de contenido**
```
Problema: Una plataforma de videos recomienda contenido 
cada vez más extremo para mantener engagement.

Consideraciones:
- Responsabilidad social vs beneficios comerciales
- Libertad de elección vs manipulación algorítmica
- Impacto en la sociedad y polarización
```

### 2. Sesgos algorítmicos

#### Tipos de sesgos

**Sesgo de datos históricos**
- Los datos reflejan discriminaciones pasadas
- Perpetuación de desigualdades existentes
- Ejemplo: Algoritmos de crédito que discriminan por código postal

**Sesgo de representación**
- Ciertos grupos están sub-representados en los datos
- Menor precisión para minorías
- Ejemplo: Reconocimiento facial menos preciso en personas de piel oscura

**Sesgo de confirmación**
- Selección de datos que confirman hipótesis previas
- Interpretación sesgada de resultados
- Ejemplo: Búsquedas que refuerzan estereotipos

**Sesgo de medición**
- Diferentes formas de medir pueden favorece a ciertos grupos
- Métricas inadecuadas para el contexto
- Ejemplo: Evaluar inteligencia solo con un tipo de test

#### Detección de sesgos

**Análisis estadístico**
```python
# Ejemplo: Detectar sesgo por género en contratación
import pandas as pd

# Cargar datos de contratación
contrataciones = pd.read_csv('contrataciones.csv')

# Calcular tasas por género
tasa_hombres = contrataciones[contrataciones['genero'] == 'M']['contratado'].mean()
tasa_mujeres = contrataciones[contrataciones['genero'] == 'F']['contratado'].mean()

# Calcular disparidad
disparidad = tasa_hombres / tasa_mujeres
print(f"Disparidad de género: {disparidad:.2f}")

# Si disparidad > 1.2 o < 0.8, posible sesgo
if disparidad > 1.2 or disparidad < 0.8:
    print("⚠️ Posible sesgo detectado")
```

**Métricas de equidad**
- **Demographic Parity**: Misma tasa de predicción positiva por grupo
- **Equalized Odds**: Misma sensibilidad y especificidad por grupo
- **Calibration**: Misma precisión de predicciones por grupo

#### Mitigación de sesgos

**En los datos**
- Recolección más representativa
- Técnicas de balanceo (oversampling, undersampling)
- Datos sintéticos para grupos minoritarios

**En el algoritmo**
- Regularización para penalizar discriminación
- Restricciones de equidad durante entrenamiento
- Post-procesamiento de resultados

**En la implementación**
- Monitoreo continuo de métricas de equidad
- Auditorías regulares por grupos externos
- Feedback loops para detectar deriva

### 3. Marco legal y regulatorio

#### GDPR (Reglamento General de Protección de Datos)

**Principios clave para IA**
- **Consentimiento explícito**: Los usuarios deben saber cómo se usan sus datos
- **Derecho de explicación**: Los usuarios pueden solicitar explicaciones de decisiones automatizadas
- **Portabilidad de datos**: Los usuarios pueden transferir sus datos
- **Derecho al olvido**: Los usuarios pueden solicitar eliminación de datos

**Artículo 22: Decisiones automatizadas**
```
"El interesado tendrá derecho a no ser objeto de una decisión 
basada únicamente en el tratamiento automatizado, incluida la 
elaboración de perfiles, que produzca efectos jurídicos en él 
o le afecte significativamente de modo similar."
```

**Implicaciones para desarrollo web**
- Interfaces claras para gestión de consentimiento
- Sistemas de explicación de algoritmos
- Herramientas de descarga/eliminación de datos

#### Ley de IA de la Unión Europea (2024)

**Clasificación por riesgo**

**Riesgo inaceptable (Prohibidas)**
- Sistemas de puntuación social gubernamental
- Manipulación subliminal de comportamiento
- Categorización biométrica por características sensibles

**Alto riesgo (Regulación estricta)**
- Sistemas de gestión de recursos humanos
- Evaluación crediticia y seguros
- Sistemas educativos de evaluación

**Riesgo limitado (Transparencia obligatoria)**
- Chatbots y asistentes virtuales
- Sistemas de recomendación
- Deepfakes y contenido generado por IA

**Riesgo mínimo (Sin restricciones especiales)**
- Filtros de spam
- Videojuegos con IA
- Sistemas de inventario

#### Otras normativas relevantes

**Algorithmic Accountability Act (EE.UU.)**
- Auditorías obligatorias para sistemas de alto impacto
- Evaluación de sesgos y discriminación
- Transparencia en procesos algorítmicos

**Principios de IA de la OCDE**
- IA centrada en el ser humano
- Transparencia y explicabilidad
- Robustez, seguridad y protección
- Responsabilidad y rendición de cuentas

### 4. IA responsable en la práctica

#### Desarrollo de aplicaciones web éticas

**Fase de diseño**
```python
# Checklist de consideraciones éticas
class EthicalChecklist:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.checks = {
            'datos_representativos': False,
            'metricas_equidad': False,
            'explicabilidad': False,
            'consentimiento_claro': False,
            'auditoria_sesgos': False
        }
    
    def evaluar_datos(self):
        """Verificar representatividad de datos"""
        # Análisis demográfico del dataset
        # Verificar balance entre grupos
        # Documentar limitaciones
        pass
    
    def definir_metricas(self):
        """Establecer métricas de equidad"""
        # Además de precisión, incluir:
        # - Paridad demográfica
        # - Igualdad de oportunidades
        # - Calibración por grupos
        pass
```

**Fase de implementación**
```javascript
// Ejemplo: Consentimiento transparente para IA
class AIConsentManager {
    constructor() {
        this.consentimientos = {};
    }
    
    mostrarInformacionIA(tipoIA) {
        const info = {
            'recomendacion': 'Usamos IA para personalizar tu experiencia',
            'chatbot': 'Este chat es atendido por IA, no por humanos',
            'analisis': 'Analizamos tu comportamiento para mejorar el servicio'
        };
        
        return `
            <div class="ai-consent">
                <h3>Uso de Inteligencia Artificial</h3>
                <p>${info[tipoIA]}</p>
                <details>
                    <summary>¿Cómo funciona?</summary>
                    <p>Explicación técnica accesible...</p>
                </details>
                <button onclick="this.otorgarConsentimiento('${tipoIA}')">
                    Acepto
                </button>
            </div>
        `;
    }
}
```

#### Auditoría y monitoreo

**Dashboard de métricas éticas**
```python
# Sistema de monitoreo de equidad
import matplotlib.pyplot as plt
import seaborn as sns

class EthicsMonitor:
    def __init__(self, modelo, datos):
        self.modelo = modelo
        self.datos = datos
    
    def calcular_metricas_equidad(self, grupo_protegido):
        """Calcular métricas de equidad por grupo"""
        grupos = self.datos.groupby(grupo_protegido)
        
        metricas = {}
        for nombre, grupo in grupos:
            predicciones = self.modelo.predict(grupo)
            metricas[nombre] = {
                'precision': precision_score(grupo['target'], predicciones),
                'recall': recall_score(grupo['target'], predicciones),
                'f1': f1_score(grupo['target'], predicciones)
            }
        
        return metricas
    
    def generar_reporte_equidad(self):
        """Generar reporte visual de equidad"""
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Gráfico de precisión por grupo
        # Gráfico de recall por grupo  
        # Gráfico de F1 por grupo
        
        plt.tight_layout()
        return fig
```

## 🔍 Casos de estudio reales

### Caso 1: Amazon - Algoritmo de contratación sesgado (2018)

**Contexto**: Amazon desarrolló un sistema de IA para evaluar currículums automáticamente.

**Problema identificado**:
- El sistema penalizaba CVs que incluían palabras como "women's" (ej: "women's chess club captain")
- Favorecía sistemáticamente candidatos masculinos
- Se entrenó con datos históricos de contrataciones (mayoritariamente hombres)

**Consecuencias**:
- Amazon canceló el proyecto
- Pérdida de confianza en sistemas automatizados de RRHH
- Mayor scrutinio regulatorio

**Lecciones aprendidas**:
1. Los datos históricos pueden perpetuar sesgos
2. La diversidad en equipos de desarrollo es crucial
3. Las auditorías externas son necesarias

### Caso 2: Netflix - Algoritmo de recomendación ético

**Enfoque responsable**:
- Transparencia sobre el uso de datos
- Control de usuario sobre recomendaciones
- Diversidad en contenido recomendado

**Implementación**:
```python
# Ejemplo simplificado de recomendación diversa
class RecomendadorEtico:
    def __init__(self, usuario):
        self.usuario = usuario
        self.objetivos_diversidad = {
            'generos': 5,  # Mínimo 5 géneros diferentes
            'idiomas': 2,  # Al menos 2 idiomas
            'antigüedad': True  # Incluir contenido antiguo y nuevo
        }
    
    def generar_recomendaciones(self, num_items=10):
        recomendaciones = self.algoritmo_base()
        
        # Aplicar filtros de diversidad
        recomendaciones_diversas = self.aplicar_diversidad(recomendaciones)
        
        # Verificar que cumple objetivos éticos
        if self.verificar_diversidad(recomendaciones_diversas):
            return recomendaciones_diversas
        else:
            return self.rebalancear_recomendaciones()
```

### Caso 3: Microsoft Tay - Chatbot que aprendió sesgos

**Contexto**: Microsoft lanzó un chatbot en Twitter que aprendía de conversaciones públicas.

**Problema**:
- En 24 horas, el bot comenzó a publicar contenido ofensivo y discriminatorio
- Aprendió de usuarios malintencionados que lo "entrenaron" con contenido tóxico

**Respuesta**:
- Microsoft retiró el bot inmediatamente
- Implementó filtros y moderación más estricta
- Desarrolló principios de IA responsable

## 💡 Ejercicios prácticos

### Ejercicio 1: Análisis de sesgo en dataset

```python
# Dataset: contrataciones_tech.csv
# Analiza si existe sesgo de género en contrataciones

import pandas as pd
import matplotlib.pyplot as plt

# Tu código aquí:
# 1. Cargar el dataset
# 2. Calcular tasa de contratación por género
# 3. Visualizar las diferencias
# 4. Calcular métricas de disparidad
# 5. Proponer soluciones
```

### Ejercicio 2: Consentimiento transparente

Diseña una interfaz web que explique claramente cómo una aplicación usa IA para:
- Recomendaciones de productos
- Análisis de sentimientos en reseñas
- Personalización de contenido

### Ejercicio 3: Evaluación ética de proyecto

Evalúa un proyecto de IA web usando esta rúbrica:

| Criterio | Sí | Parcial | No |
|----------|----|---------|----|
| ¿Los datos son representativos? | | | |
| ¿Se monitorizan sesgos? | | | |
| ¿Hay transparencia sobre el uso de IA? | | | |
| ¿Los usuarios pueden controlar la IA? | | | |
| ¿Hay mecanismos de apelación? | | | |

## 📝 Quiz de autoevaluación

### Pregunta 1
¿Cuál de estos NO es un principio de IA ética?

**a)** Fairness (Equidad)  
**b)** Transparency (Transparencia)  
**c)** Efficiency (Eficiencia)  
**d)** Accountability (Responsabilidad)

### Pregunta 2
El sesgo de representación ocurre cuando:

**a)** Los datos reflejan discriminaciones históricas  
**b)** Ciertos grupos están sub-representados en los datos de entrenamiento  
**c)** Los desarrolladores tienen prejuicios conscientes  
**d)** El algoritmo es técnicamente deficiente

### Pregunta 3
Según el GDPR, los usuarios tienen derecho a:

**a)** Solo ver sus datos personales  
**b)** Obtener explicaciones de decisiones automatizadas  
**c)** Modificar algoritmos que los afecten  
**d)** Todas las anteriores

### Pregunta 4
En la Ley de IA de la UE, los chatbots se clasifican como:

**a)** Riesgo inaceptable  
**b)** Alto riesgo  
**c)** Riesgo limitado  
**d)** Riesgo mínimo

### Pregunta 5
La "paridad demográfica" significa que:

**a)** Todos los grupos tienen el mismo tamaño en el dataset  
**b)** El algoritmo tiene la misma precisión para todos los grupos  
**c)** Todos los grupos tienen la misma tasa de predicciones positivas  
**d)** No existe discriminación en los datos

## 🎯 Proyecto: Manifiesto de IA Responsable

### Instrucciones
Crea un "Manifiesto de IA Responsable" para una empresa de desarrollo web que incluya:

1. **Principios fundamentales** (máximo 5)
2. **Compromisos específicos** con ejemplos prácticos
3. **Proceso de auditoría** para proyectos con IA
4. **Métricas de seguimiento** para evaluar cumplimiento
5. **Plan de respuesta** ante problemas éticos

### Formato
- Documento de 2-3 páginas
- Lenguaje accesible para no técnicos
- Ejemplos concretos de implementación
- Referencias a legislación aplicable

## 🔗 Recursos adicionales

### Lecturas obligatorias
- **"Weapons of Math Destruction"** - Cathy O'Neil (Capítulos 1-3)
- **EU AI Act** - Resumen ejecutivo oficial
- **Partnership on AI - Principios** (documento completo)

### Videos recomendados
- **"The Coded Bias"** - Documental sobre sesgos algorítmicos
- **"AI Ethics: The Good, The Bad, The Ugly"** - TEDx Talk
- **Cathy O'Neil en TED**: "The era of blind faith in big data must end"

### Herramientas prácticas
- **AI Fairness 360** (IBM) - Detección y mitigación de sesgos
- **What-If Tool** (Google) - Exploración de modelos
- **Fairlearn** (Microsoft) - Equidad en machine learning

## 📋 Actividades de debate

### Debate 1: "¿Debería prohibirse el reconocimiento facial en espacios públicos?"

**Posiciones**:
- **A favor**: Riesgos de privacidad y sesgos discriminatorios
- **En contra**: Beneficios de seguridad y conveniencia

**Preparación**: Cada estudiante debe traer 3 argumentos y 2 evidencias

### Debate 2: "IA vs Empleos: ¿Responsabilidad social o evolución natural?"

**Contexto**: Una empresa quiere automatizar atención al cliente con chatbots

**Consideraciones**:
- Impacto en empleo humano
- Beneficios para consumidores
- Responsabilidad corporativa
- Transición justa para trabajadores

## 🎯 Evaluación de la unidad

Esta unidad se evalúa mediante:
- **P02**: Debate estructurado + ensayo reflexivo (sumativa 8%)
- **Participación**: En discusiones y análisis de casos
- **Proyecto**: Manifiesto de IA Responsable

---

**Unidad elaborada por**: Departamento de Informática y Comunicaciones  
**Última actualización**: 26 de octubre de 2025