# 🤔 Ética, Sesgos y Legislación en IA
## Presentación interactiva para 2º DAW

---

## 🚨 Pregunta de apertura

### ¿Puede una máquina ser racista?

<!-- **💭 Reflexiona:**
- ¿Has notado alguna vez que un algoritmo te trata de forma diferente?
- ¿Crees que los algoritmos son más objetivos que los humanos?
- ¿Qué pasaría si una IA decidiera si consigues un trabajo?

**⏰ Tiempo de reflexión: 2 minutos** -->

---

## 🎯 Lo que vamos a descubrir

### Al final de esta sesión entenderás:
- ✅ **Por qué** la IA puede ser discriminatoria
- ✅ **Cómo** detectar y prevenir sesgos algorítmicos
- ✅ **Qué** dice la ley sobre IA en Europa
- ✅ **Cómo** desarrollar IA de forma responsable

---

## 🤖 Caso real: Amazon y la IA machista

### 📰 **Los hechos (2018):**
Amazon desarrolló un sistema de IA para evaluar currículums automáticamente.

### 🚨 **El problema:**
```python
# Lo que hacía el algoritmo (simplificado)
def evaluar_curriculum(cv):
    puntuacion = 0
    
 
    if "women's" in cv:  # ej: "women's chess club captain"
        puntuacion -= 10
    
    if "female" in cv:   # ej: "female software engineer"
        puntuacion -= 5
    
    if "executed" in cv or "captured" in cv:
        puntuacion += 10
    
    return puntuacion
```

### 🤔 **Pregunta clave:**
**¿Por qué crees que la IA se volvió "machista"?**

---

## 🧠 La respuesta: Datos sesgados

### 📊 **El origen del problema:**

| Datos de entrenamiento | Resultado |
|------------------------|-----------|
| 📈 **10 años de CVs exitosos** | → Mayoritariamente hombres |
| 🏢 **Sector tecnológico** | → Históricamente masculino |
| ✅ **CVs de contratados** | → Patrones "masculinos" |

### 💡 **La IA aprendió:**
> **"Para ser exitoso, hay que parecerse a los exitosos del pasado"**

### 🔄 **El ciclo del sesgo:**
```
Sociedad sesgada → Datos sesgados → IA sesgada → Decisiones sesgadas → Sociedad más sesgada
```

### 💭 **Pregunta de reflexión:**
**¿Es culpa de la IA o de nosotros como sociedad?**

---

## 🎭 Los 4 tipos de sesgos que debes conocer

### 1. 📚 **Sesgo de datos históricos**
**¿Qué es?** Los datos reflejan discriminaciones pasadas

**Ejemplo práctico:**
```python
# Algoritmo de crédito bancario
def aprobar_credito(codigo_postal, ingresos):
    # Si vives en zona "problemática" → más difícil
    if codigo_postal in zonas_historicamente_pobres:
        umbral_ingresos = ingresos * 1.5  # Más exigente
    else:
        umbral_ingresos = ingresos
    
    return umbral_ingresos > 30000
```

### 2. 🎨 **Sesgo de representación**
**¿Qué es?** Ciertos grupos están sub-representados

**Ejemplo famoso:**
- 👨🏻 Reconocimiento facial: 99% precisión en hombres blancos
- 👩🏿 Reconocimiento facial: 65% precisión en mujeres negras

### 💭 **¿Por qué crees que ocurre esta diferencia?**

---

## 🔍 Los otros dos sesgos

### 3. 🧠 **Sesgo de confirmación**
**¿Qué es?** Buscar datos que confirmen lo que ya creemos

**Ejemplo en buscadores:**
```javascript
// Búsqueda sesgada
function buscar(termino) {
    if (termino === "CEO exitoso") {
        // Muestra más resultados de hombres blancos
        return resultados.filter(r => r.demografia === "hombre_blanco");
    }
}
```

### 4. 📏 **Sesgo de medición**
**¿Qué es?** Medir mal o con herramientas inadecuadas

**Ejemplo:** Evaluar inteligencia solo con tests de matemáticas
- ¿Descarta a personas creativas?
- ¿Favorece ciertos tipos de educación?

### 🤔 **Pregunta clave:**
**¿Cómo podríamos detectar estos sesgos en nuestras aplicaciones web?**

---

## 🔧 Detectando sesgos: El código que necesitas

### 📊 **Herramienta básica de detección:**

```python
import pandas as pd

def detectar_sesgo_genero(datos):
    """Detecta sesgo de género en contrataciones"""
    
    # Calcular tasas por género
    hombres = datos[datos['genero'] == 'M']
    mujeres = datos[datos['genero'] == 'F']
    
    tasa_hombres = hombres['contratado'].mean()
    tasa_mujeres = mujeres['contratado'].mean()
    
    # Calcular disparidad
    disparidad = tasa_hombres / tasa_mujeres
    
    print(f"Tasa contratación hombres: {tasa_hombres:.2%}")
    print(f"Tasa contratación mujeres: {tasa_mujeres:.2%}")
    print(f"Disparidad: {disparidad:.2f}")
    
    # Regla práctica: disparidad > 1.2 o < 0.8 = posible sesgo
    if disparidad > 1.2:
        return "⚠️ Posible sesgo a favor de hombres"
    elif disparidad < 0.8:
        return "⚠️ Posible sesgo a favor de mujeres"
    else:
        return "✅ No se detecta sesgo significativo"
```

### 💭 **¿Qué otros grupos deberíamos analizar además del género?**

---

## ⚖️ ¿Qué dice la ley? GDPR y más

### 🇪🇺 **GDPR: Tus derechos ante la IA**

#### 📜 **Artículo 22 - El más importante:**
> *"Derecho a no ser objeto de una decisión basada únicamente en tratamiento automatizado"*

#### 🔍 **¿Qué significa en la práctica?**

```javascript
// ANTES: Decisión 100% automática
function aprobar_prestamo(datos_usuario) {
    return algoritmo_ia.decidir(datos_usuario); // ❌ Ilegal
}

// DESPUÉS: Supervisión humana obligatoria
function aprobar_prestamo_legal(datos_usuario) {
    recomendacion_ia = algoritmo_ia.sugerir(datos_usuario);
    decision_final = humano.revisar(recomendacion_ia, datos_usuario);
    
    // Guardar justificación
    log.guardar({
        'recomendacion_ia': recomendacion_ia,
        'decision_humana': decision_final,
        'justificacion': humano.explicacion
    });
    
    return decision_final; // ✅ Legal
}
```

### 🛡️ **Tus derechos como usuario:**
1. **🔍 Derecho de explicación:** "¿Por qué me negaron el crédito?"
2. **📥 Portabilidad:** Llevarte tus datos a otra empresa
3. **🗑️ Derecho al olvido:** Eliminar tus datos
4. **👥 Supervisión humana:** Que una persona revise decisiones importantes

---

## 🇪🇺 Nueva Ley de IA Europea (2024)

### 🚦 **Sistema de semáforos por riesgo:**

#### 🔴 **RIESGO INACEPTABLE** (Prohibido)
- 🏛️ Sistemas de puntuación social (como en China)
- 🧠 Manipulación subliminal del comportamiento
- 👁️ Categorización biométrica por raza/religión

#### 🟠 **ALTO RIESGO** (Regulación estricta)
- 💼 Selección de personal automatizada
- 💰 Evaluación crediticia
- 🎓 Sistemas de calificación educativa

### 💭 **¿En qué categoría pondrías un sistema de recomendación de Netflix?**

---

## 🟡 **RIESGO LIMITADO** (Transparencia obligatoria)

### 📱 **Ejemplos que usas diariamente:**
- 🤖 Chatbots y asistentes virtuales
- 📺 Sistemas de recomendación (Netflix, YouTube)
- 🖼️ Deepfakes y contenido generado por IA

### 📋 **Obligaciones legales:**
```html
<!-- ANTES: Sin avisos -->
<div class="chat">
    <p>¡Hola! ¿En qué puedo ayudarte?</p>
</div>

<!-- DESPUÉS: Transparencia obligatoria -->
<div class="chat">
    <div class="ai-notice">
        🤖 Este chat es atendido por inteligencia artificial
        <a href="/info-ai">Más información</a>
    </div>
    <p>¡Hola! ¿En qué puedo ayudarte?</p>
</div>
```

### 🤔 **¿Has visto avisos así en alguna web o app?**

---

## 🟢 Los 5 pilares de la IA ética

### 1. ⚖️ **Fairness (Equidad)**
**¿Qué significa?** Tratamiento justo para todos

**En la práctica:**
```python
# Verificar equidad en recomendaciones
def verificar_equidad_recomendaciones(usuarios, recomendaciones):
    # Verificar diversidad por género
    rec_hombres = recomendaciones[usuarios['genero'] == 'M']
    rec_mujeres = recomendaciones[usuarios['genero'] == 'F']
    
    # ¿Los hombres y mujeres reciben diversidad similar?
    diversidad_h = calcular_diversidad(rec_hombres)
    diversidad_m = calcular_diversidad(rec_mujeres)
    
    if abs(diversidad_h - diversidad_m) > 0.1:
        return "⚠️ Posible inequidad en diversidad"
    return "✅ Equidad verificada"
```

### 💭 **¿Qué otros aspectos deberíamos verificar además del género?**

---

## 🔍 Los otros 4 pilares éticos

### 2. 📊 **Transparency (Transparencia)**
**¿Qué hace tu IA?** Explicarlo claramente

```javascript
// Interfaz transparente
class TransparentAI {
    mostrarExplicacion() {
        return `
            <div class="ai-explanation">
                <h3>¿Cómo funciona nuestra IA?</h3>
                <p>📊 Analizamos tu historial de compras</p>
                <p>👥 Comparamos con usuarios similares</p>
                <p>🎯 Sugerimos productos que podrían gustarte</p>
                <button onclick="verMasDetalles()">Ver más detalles</button>
            </div>
        `;
    }
}
```

### 3. 🎯 **Explainability (Explicabilidad)**
**¿Por qué esta decisión?** Poder explicar cada resultado

### 4. 🛡️ **Accountability (Responsabilidad)**
**¿Quién responde si algo sale mal?** Responsabilidades claras

### 5. 🔒 **Privacy (Privacidad)**
**¿Cómo proteges los datos?** Seguridad y minimización

---

## 🔧 IA responsable: Código práctico

### 💻 **Consentimiento transparente:**

```javascript
class AIConsentManager {
    constructor() {
        this.consentimientos = {};
    }
    
    solicitarConsentimiento(tipoIA) {
        const explicaciones = {
            'recomendacion': `
                <div class="consent-card">
                    <h3>🎯 Sistema de Recomendaciones</h3>
                    <p><strong>¿Qué hace?</strong> Analiza tus compras para sugerir productos</p>
                    <p><strong>¿Qué datos usa?</strong> Historial, navegación, preferencias</p>
                    <p><strong>¿Puedes controlarlo?</strong> Sí, en configuración de privacidad</p>
                    <p><strong>¿Quién decide?</strong> El algoritmo sugiere, tú eliges</p>
                    
                    <button onclick="aceptar('recomendacion')">✅ Acepto</button>
                    <button onclick="rechazar('recomendacion')">❌ No gracias</button>
                </div>
            `
        };
        
        return explicaciones[tipoIA];
    }
}
```

### 🤔 **¿Qué información adicional incluirías para ser más transparente?**

---

## 📊 Sistema de monitoreo ético

### 🔍 **Dashboard de métricas éticas:**

```python
class EthicsMonitor:
    def generar_reporte_semanal(self):
        """Reporte automático de métricas éticas"""
        
        metricas = {
            # Equidad
            'disparidad_genero': self.calcular_disparidad('genero'),
            'disparidad_edad': self.calcular_disparidad('edad'),
            
            # Transparencia
            'usuarios_informados': self.porcentaje_usuarios_informados(),
            'explicaciones_solicitadas': self.count_explicaciones(),
            
            # Privacidad
            'datos_minimizados': self.verificar_minimizacion(),
            'consentimientos_validos': self.verificar_consentimientos()
        }
        
        # Generar alertas si algo va mal
        alertas = []
        if metricas['disparidad_genero'] > 1.2:
            alertas.append("🚨 Disparidad de género detectada")
        
        if metricas['usuarios_informados'] < 0.8:
            alertas.append("⚠️ Baja transparencia con usuarios")
            
        return {
            'metricas': metricas,
            'alertas': alertas,
            'recomendaciones': self.generar_recomendaciones(metricas)
        }
```

### 💭 **¿Qué otras métricas deberíamos monitorear?**

---

## 🔥 Caso Netflix: ¿Cómo lo hacen bien?

### 🎬 **El desafío:**
- 📊 **200+ millones** de usuarios
- 🌍 **190+ países** diferentes
- 🎭 **Diversidad** cultural enorme
- ⚖️ **Equilibrio** entre engagement y responsabilidad

### ✅ **Su enfoque ético:**

```python
class NetflixEthicalRecommender:
    def generar_recomendaciones(self, usuario):
        # 1. Recomendaciones base por preferencias
        base_recs = self.algoritmo_preferencias(usuario)
        
        # 2. Aplicar filtros de diversidad
        diverse_recs = self.aplicar_diversidad(base_recs, {
            'generos_minimos': 4,      # Al menos 4 géneros diferentes
            'idiomas_minimos': 2,      # Al menos 2 idiomas
            'epocas_variadas': True,   # Contenido nuevo y clásico
            'creadores_diversos': True # Directores de diferentes backgrounds
        })
        
        # 3. Evitar cámaras de eco
        balanced_recs = self.evitar_polarizacion(diverse_recs)
        
        # 4. Respetar controles parentales y preferencias usuario
        final_recs = self.aplicar_controles_usuario(balanced_recs, usuario)
        
        return final_recs
```

### 🤔 **¿Crees que Netflix hace suficiente para ser ético? ¿Qué mejorarías?**

---

## 💥 Caso Microsoft Tay: Cuando todo sale mal

### 🤖 **El experimento (2016):**
Microsoft lanzó un chatbot en Twitter que "aprendía" de conversaciones

### 🚨 **El desastre:**
- ⏰ **En 24 horas:** El bot se volvió racista y ofensivo
- 👥 **Usuarios maliciosos:** Lo "entrenaron" con contenido tóxico
- 📱 **Twitter:** Amplificó y viralizó el problema

### 📚 **Lo que aprendimos:**

```python
# ANTES: Aprendizaje sin filtros
class TayBot:
    def aprender_de_conversacion(self, mensaje):
        # Aprende de TODO sin filtros
        self.modelo.entrenar(mensaje)  # ❌ Peligroso
        
# DESPUÉS: Aprendizaje con filtros
class SafeBot:
    def aprender_de_conversacion(self, mensaje):
        # 1. Filtrar contenido tóxico
        if self.detector_toxicidad(mensaje) > 0.7:
            return  # No aprender de contenido tóxico
            
        # 2. Verificar fuente confiable
        if not self.fuente_confiable(usuario):
            return
            
        # 3. Supervisión humana para casos límite
        if self.detector_incertidumbre(mensaje) > 0.5:
            self.enviar_a_revision_humana(mensaje)
        else:
            self.modelo.entrenar(mensaje)  # ✅ Seguro
```

### 💭 **¿Qué lecciones podemos aplicar a nuestros proyectos web?**

---

## 🛠️ Tu checklist de IA responsable

### ✅ **Antes de lanzar cualquier IA en tu web:**

#### 📊 **Datos:**
- [ ] ¿Los datos son representativos de todos los usuarios?
- [ ] ¿He verificado sesgos históricos en mis datos?
- [ ] ¿Tengo suficiente diversidad en el dataset?

#### 🤖 **Algoritmo:**
- [ ] ¿Puedo explicar cómo funciona en términos simples?
- [ ] ¿He testado el rendimiento en diferentes grupos demográficos?
- [ ] ¿Tengo métricas de equidad además de precisión?

#### 👥 **Usuarios:**
- [ ] ¿Los usuarios saben que están interactuando con IA?
- [ ] ¿Pueden solicitar explicaciones de las decisiones?
- [ ] ¿Tienen control sobre cómo se usa la IA?

#### ⚖️ **Legal:**
- [ ] ¿Cumplo con GDPR y la Ley de IA europea?
- [ ] ¿Tengo procesos de supervisión humana?
- [ ] ¿Puedo auditar las decisiones tomadas?

---

## 🔮 El futuro de la IA ética

### 🌟 **Tendencias emergentes:**

#### 🔍 **IA Explicable (XAI)**
```python
# Futuro: IA que se explica automáticamente
class ExplainableAI:
    def decidir_y_explicar(self, datos):
        decision = self.modelo.predict(datos)
        explicacion = self.modelo.explain(datos)
        
        return {
            'decision': decision,
            'explicacion': f"Decisión basada en: {explicacion.factores_principales}",
            'confianza': explicacion.nivel_confianza,
            'alternativas': explicacion.escenarios_alternativos
        }
```

#### 🛡️ **IA Federated Learning**
- Entrenar modelos sin centralizar datos
- Mayor privacidad por diseño
- Colaboración sin comprometer seguridad

### 💭 **¿Qué otros avances crees que veremos en IA ética?**

---

## 🎯 Pregunta final de reflexión

### 🤔 **Como futuro desarrollador web:**

**¿Cuál es tu responsabilidad ética al crear aplicaciones con IA?**

**Piensa en:**
- 👥 Los usuarios que las usarán
- 🌍 El impacto social de tus decisiones
- ⚖️ La equidad y justicia en tus algoritmos
- 🔮 Las consecuencias a largo plazo

### 📝 **Comparte tu reflexión:**
*¿Cómo te asegurarás de que tu IA sea ética y responsable?*

---

## 🔗 Próximos pasos

### 📚 **Para profundizar:**
1. 📖 Lee el **EU AI Act** completo
2. 🎬 Ve el documental **"Coded Bias"**
3. 🛠️ Experimenta con **AI Fairness 360** de IBM
4. 👥 Únete a comunidades de **AI Ethics**

### 🎯 **En tu próximo proyecto:**
- Implementa un checklist ético
- Incluye métricas de equidad
- Diseña interfaces transparentes
- Planifica auditorías regulares

---

## ❓ Espacio para preguntas

### 🗣️ **Temas para debatir:**

1. **🤖 vs 👥** ¿Puede la IA ser más justa que los humanos?

2. **🔒 vs 🎯** ¿Privacidad o personalización? ¿Hay que elegir?

3. **⚖️ vs 💰** ¿Ética o beneficios? ¿Son compatibles?

4. **🌍 vs 🏢** ¿Quién debe regular la IA: gobiernos o empresas?

### ⏰ **Tiempo para preguntas: 15 minutos**

---

## 🎉 Mensaje final

### 💡 **Recuerda:**

> **"Con gran poder (de IA) viene gran responsabilidad"**

**Tu código puede:**
- 🌟 Hacer el mundo más justo y equitativo
- 🚨 O perpetuar y amplificar discriminaciones

### 🎯 **La decisión es tuya como desarrollador**

**¿Qué tipo de futuro digital quieres construir?**

---

**🔗 Próxima clase: Fundamentos técnicos de Python para IA**

*¡Gracias por vuestra atención y participación!* 🙌