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

## 📏 Métricas avanzadas para detectar sesgos

### 🎯 **Las 3 métricas clave que todo developer debe conocer**

#### 1. 👥 **Demographic Parity (Paridad Demográfica)**
**¿Qué mide?** Todos los grupos reciben el mismo % de resultados positivos

<!-- ```python
def calcular_demographic_parity(datos, grupo_protegido):
    """Verificar si todos los grupos tienen misma tasa de aprobación"""
    
    resultados = {}
    for grupo in datos[grupo_protegido].unique():
        subset = datos[datos[grupo_protegido] == grupo]
        tasa_positiva = subset['resultado_positivo'].mean()
        resultados[grupo] = tasa_positiva
    
    # Mostrar resultados
    print("📊 Tasas de aprobación por grupo:")
    for grupo, tasa in resultados.items():
        print(f"  {grupo}: {tasa:.2%}")
    
    # Verificar paridad (diferencia < 5%)
    tasas = list(resultados.values())
    max_diff = max(tasas) - min(tasas)
    
    if max_diff > 0.05:
        return f"⚠️ Violación de paridad: {max_diff:.1%} diferencia"
    else:
        return "✅ Demographic Parity cumplida"

# Ejemplo: Sistema de préstamos
prestamos = pd.DataFrame({
    'etnia': ['blanco', 'negro', 'blanco', 'latino', 'negro', 'blanco'],
    'aprobado': [1, 0, 1, 1, 0, 1]
})

resultado = calcular_demographic_parity(prestamos, 'etnia')
``` -->

### 💭 **¿Es justo que todos los grupos tengan exactamente la misma tasa de aprobación?**

---

#### 2. ⚖️ **Equalized Odds (Igualdad de Oportunidades)**
**¿Qué mide?** Misma sensibilidad y especificidad para todos los grupos
<!-- 
```python
def calcular_equalized_odds(y_real, y_pred, grupo_sensible):
    """Verificar justicia en predicciones correctas"""
    
    from sklearn.metrics import confusion_matrix
    
    resultados = {}
    for grupo in grupo_sensible.unique():
        # Filtrar por grupo
        mask = grupo_sensible == grupo
        y_true_grupo = y_real[mask]
        y_pred_grupo = y_pred[mask]
        
        # Matriz de confusión
        tn, fp, fn, tp = confusion_matrix(y_true_grupo, y_pred_grupo).ravel()
        
        # Calcular métricas
        sensibilidad = tp / (tp + fn) if (tp + fn) > 0 else 0  # TPR
        especificidad = tn / (tn + fp) if (tn + fp) > 0 else 0  # TNR
        
        resultados[grupo] = {
            'sensibilidad': sensibilidad,
            'especificidad': especificidad
        }
    
    # Mostrar resultados
    print("🎯 Equalized Odds por grupo:")
    for grupo, metricas in resultados.items():
        print(f"  {grupo}:")
        print(f"    Sensibilidad: {metricas['sensibilidad']:.2%}")
        print(f"    Especificidad: {metricas['especificidad']:.2%}")
    
    return resultados

# Verificar si hay equidad en detección de fraude
resultados_equidad = calcular_equalized_odds(
    datos['es_fraude_real'], 
    datos['prediccion_fraude'], 
    datos['grupo_demografico']
)
``` -->

### 🔍 **¿Qué significa en términos simples?**
- **Sensibilidad:** "De todos los casos reales positivos, ¿cuántos detectamos?"
- **Especificidad:** "De todos los casos reales negativos, ¿cuántos identificamos bien?"

---

#### 3. 🎯 **Calibration (Calibración)**
**¿Qué mide?** Las probabilidades predichas coinciden con la realidad para todos los grupos

<!-- ```python
def verificar_calibracion(y_real, y_proba, grupo_sensible, n_bins=5):
    """Verificar si las probabilidades están bien calibradas por grupo"""
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(1, len(grupo_sensible.unique()), figsize=(15, 4))
    
    for i, grupo in enumerate(grupo_sensible.unique()):
        # Filtrar por grupo
        mask = grupo_sensible == grupo
        y_true_grupo = y_real[mask]
        y_prob_grupo = y_proba[mask]
        
        # Crear bins de probabilidad
        bins = np.linspace(0, 1, n_bins + 1)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        
        calibracion_real = []
        for j in range(n_bins):
            # Casos en este bin de probabilidad
            in_bin = (y_prob_grupo >= bins[j]) & (y_prob_grupo < bins[j+1])
            
            if np.sum(in_bin) > 0:
                # Fracción real de positivos en este bin
                frac_positivos = np.mean(y_true_grupo[in_bin])
                calibracion_real.append(frac_positivos)
            else:
                calibracion_real.append(0)
        
        # Graficar calibración
        axes[i].plot(bin_centers, calibracion_real, 'o-', label=f'Real {grupo}')
        axes[i].plot([0, 1], [0, 1], '--', label='Calibración perfecta')
        axes[i].set_title(f'Calibración - {grupo}')
        axes[i].set_xlabel('Probabilidad predicha')
        axes[i].set_ylabel('Fracción real de positivos')
        axes[i].legend()
    
    plt.tight_layout()
    return fig

# Ejemplo: ¿Las probabilidades de aprobación están bien calibradas?
fig = verificar_calibracion(
    datos['aprobado_real'], 
    datos['probabilidad_aprobacion'], 
    datos['grupo_etnico']
)
``` -->

### 🎪 **Analogía de la calibración:**
> **"Si digo que llueve con 80% probabilidad, debe llover 8 de cada 10 veces que hago esa predicción"**



---

## 🛠️ Estrategias para mitigar sesgos

### 🔧 **3 niveles de intervención:**


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

<!-- #### 1. 📊 **Pre-procesamiento: Arreglar los datos**

```python
# Estrategia 1: Balanceo de datos
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def balancear_dataset(X, y, grupo_protegido):
    """Balancear representación de grupos minoritarios"""
    
    # SMOTE para generar datos sintéticos
    smote = SMOTE(random_state=42)
    X_balanced, y_balanced = smote.fit_resample(X, y)
    
    print(f"📈 Dataset original: {len(X)} muestras")
    print(f"📈 Dataset balanceado: {len(X_balanced)} muestras")
    
    return X_balanced, y_balanced

# Estrategia 2: Re-sampling por grupos
def balanceo_por_grupos(datos, grupo_protegido, target):
    """Asegurar representación equitativa"""
    
    balanced_data = []
    
    # Encontrar el grupo con menos muestras positivas
    min_positivos = float('inf')
    for grupo in datos[grupo_protegido].unique():
        subset = datos[datos[grupo_protegido] == grupo]
        n_positivos = sum(subset[target] == 1)
        min_positivos = min(min_positivos, n_positivos)
    
    # Balancear cada grupo
    for grupo in datos[grupo_protegido].unique():
        subset = datos[datos[grupo_protegido] == grupo]
        
        # Tomar muestra balanceada
        positivos = subset[subset[target] == 1].sample(min_positivos)
        negativos = subset[subset[target] == 0].sample(min_positivos)
        
        balanced_data.append(pd.concat([positivos, negativos]))
    
    return pd.concat(balanced_data, ignore_index=True)
```

#### 2. ⚙️ **In-processing: Entrenar con restricciones de equidad**

```python
# Estrategia 3: Penalización de discriminación
from sklearn.linear_model import LogisticRegression
import numpy as np

class FairLogisticRegression:
    def __init__(self, fairness_penalty=0.1):
        self.fairness_penalty = fairness_penalty
        self.model = LogisticRegression()
    
    def fit(self, X, y, grupo_protegido):
        """Entrenar con penalización por discriminación"""
        
        # Función de pérdida personalizada
        def loss_with_fairness(predictions):
            # Pérdida normal
            loss_normal = self.calcular_loss_normal(y, predictions)
            
            # Penalización por inequidad
            penalty = 0
            for grupo in np.unique(grupo_protegido):
                mask = grupo_protegido == grupo
                tasa_grupo = np.mean(predictions[mask])
                tasa_global = np.mean(predictions)
                penalty += abs(tasa_grupo - tasa_global)
            
            return loss_normal + self.fairness_penalty * penalty
        
        # Entrenar con pérdida modificada
        self.model.fit(X, y)
        return self
    
    def predict(self, X):
        return self.model.predict(X)

# Uso del modelo justo
modelo_justo = FairLogisticRegression(fairness_penalty=0.2)
modelo_justo.fit(X_train, y_train, grupos_train)
```

#### 3. 🔄 **Post-procesamiento: Ajustar resultados**

```python
# Estrategia 4: Threshold optimization
def optimizar_umbrales_justos(y_real, y_proba, grupo_protegido):
    """Encontrar umbrales diferentes por grupo para equidad"""
    
    from sklearn.metrics import roc_curve
    
    umbrales_optimos = {}
    
    for grupo in np.unique(grupo_protegido):
        mask = grupo_protegido == grupo
        y_true_grupo = y_real[mask]
        y_prob_grupo = y_proba[mask]
        
        # Calcular ROC
        fpr, tpr, thresholds = roc_curve(y_true_grupo, y_prob_grupo)
        
        # Encontrar umbral que maximiza TPR - FPR (Youden's index)
        j_scores = tpr - fpr
        optimal_idx = np.argmax(j_scores)
        optimal_threshold = thresholds[optimal_idx]
        
        umbrales_optimos[grupo] = optimal_threshold
        
        print(f"🎯 Umbral óptimo para {grupo}: {optimal_threshold:.3f}")
    
    return umbrales_optimos

# Estrategia 5: Calibración post-hoc
def calibrar_por_grupos(y_real, y_proba, grupo_protegido):
    """Calibrar probabilidades separadamente por grupo"""
    
    from sklearn.calibration import CalibratedClassifierCV
    
    modelos_calibrados = {}
    
    for grupo in np.unique(grupo_protegido):
        mask = grupo_protegido == grupo
        
        # Crear y entrenar calibrador para este grupo
        calibrador = CalibratedClassifierCV(method='platt')
        
        # Pseudo-entrenamiento (en práctica usarías validation set)
        X_dummy = y_proba[mask].reshape(-1, 1)
        calibrador.fit(X_dummy, y_real[mask])
        
        modelos_calibrados[grupo] = calibrador
    
    return modelos_calibrados

def aplicar_calibracion_justa(y_proba, grupo_protegido, calibradores):
    """Aplicar calibración específica por grupo"""
    
    y_proba_calibrada = np.zeros_like(y_proba)
    
    for grupo in np.unique(grupo_protegido):
        mask = grupo_protegido == grupo
        X_grupo = y_proba[mask].reshape(-1, 1)
        
        y_proba_calibrada[mask] = calibradores[grupo].predict_proba(X_grupo)[:, 1]
    
    return y_proba_calibrada
```

### 💭 **¿Cuál de estas estrategias crees que es más efectiva? ¿Por qué?**

---

## 🔄 Pipeline completo de IA justa

### 🛠️ **Implementación práctica:**

```python
class FairMLPipeline:
    def __init__(self):
        self.preprocessor = None
        self.model = None
        self.postprocessor = None
        self.fairness_metrics = {}
    
    def fit(self, X, y, grupo_protegido):
        """Pipeline completo de ML justo"""
        
        print("🔧 Iniciando pipeline de IA justa...")
        
        # 1. Pre-procesamiento
        print("📊 Paso 1: Balanceando datos...")
        X_balanced, y_balanced = self.preprocess_for_fairness(X, y, grupo_protegido)
        
        # 2. Entrenamiento con restricciones
        print("⚙️ Paso 2: Entrenando modelo con restricciones de equidad...")
        self.model = FairLogisticRegression(fairness_penalty=0.15)
        self.model.fit(X_balanced, y_balanced, grupo_protegido)
        
        # 3. Evaluación de equidad
        print("📏 Paso 3: Evaluando métricas de equidad...")
        y_pred = self.model.predict(X)
        self.evaluar_equidad(y, y_pred, grupo_protegido)
        
        # 4. Post-procesamiento si es necesario
        if self.necesita_ajuste_post():
            print("🔄 Paso 4: Ajustando con post-procesamiento...")
            self.aplicar_post_procesamiento(X, y, grupo_protegido)
        
        print("✅ Pipeline completado!")
        return self
    
    def evaluar_equidad(self, y_true, y_pred, grupo_protegido):
        """Evaluar todas las métricas de equidad"""
        
        # Demographic Parity
        dp_score = self.calcular_demographic_parity(y_pred, grupo_protegido)
        
        # Equalized Odds  
        eo_score = self.calcular_equalized_odds(y_true, y_pred, grupo_protegido)
        
        # Overall Accuracy
        accuracy = np.mean(y_true == y_pred)
        
        self.fairness_metrics = {
            'demographic_parity': dp_score,
            'equalized_odds': eo_score,
            'accuracy': accuracy
        }
        
        # Reportar resultados
        print("📊 Métricas de Equidad:")
        print(f"  Demographic Parity: {dp_score}")
        print(f"  Equalized Odds: {eo_score}")
        print(f"  Accuracy General: {accuracy:.2%}")
    
    def necesita_ajuste_post(self):
        """Determinar si necesitamos post-procesamiento"""
        return (self.fairness_metrics['demographic_parity'] != "✅" or 
                self.fairness_metrics['equalized_odds'] != "✅")

# Uso del pipeline
pipeline = FairMLPipeline()
pipeline.fit(X_train, y_train, grupos_train)

# Predicciones justas
y_pred_fair = pipeline.predict(X_test)
```

### 🎯 **¿Cómo implementarías esto en tu próximo proyecto web?** -->

---

## ⚖️ ¿Qué dice la ley?

### 🇪🇺 **GDPR: Tus derechos ante la IA**

#### 📜 **Artículo 22 - El más importante:**
> *"Derecho a no ser objeto de una decisión basada únicamente en tratamiento automatizado"*

---

## 🟢 Los 5 pilares de la IA ética

### 1. ⚖️ **Fairness (Equidad)**
**¿Qué significa?** Tratamiento justo para todos

### 2. 📊 **Transparency (Transparencia)**
**¿Qué hace tu IA?** Explicarlo claramente

### 3. 🎯 **Explainability (Explicabilidad)**
**¿Por qué esta decisión?** Poder explicar cada resultado

### 4. 🛡️ **Accountability (Responsabilidad)**
**¿Quién responde si algo sale mal?** Responsabilidades claras

### 5. 🔒 **Privacy (Privacidad)**
**¿Cómo proteges los datos?** Seguridad y minimización

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

## 🟡 **RIESGO LIMITADO** (Transparencia obligatoria)

### 📱 **Ejemplos que usas diariamente:**
- 🤖 Chatbots y asistentes virtuales
- 📺 Sistemas de recomendación (Netflix, YouTube)
- 🖼️ Deepfakes y contenido generado por IA

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

---

## 🔮 El futuro de la IA ética

### 🌟 **Tendencias emergentes:**

#### 🔍 **IA Explicable (XAI)**
- Algoritmos y técnicas que permiten entender las decisiones tomadas por la IA
- IA Potente + Explicabilidad = Adopción + Confianza + Legalidad

#### 🛡️ **IA Federated Learning**
- Entrenar modelos sin centralizar datos
- Mayor privacidad por diseño
- Colaboración sin comprometer seguridad

---

## ❓ Espacio para preguntas

### 🗣️ **Temas para debatir:**

1. **🤖 vs 👥** ¿Puede la IA ser más justa que los humanos?

2. **🔒 vs 🎯** ¿Privacidad o personalización? ¿Hay que elegir?

3. **⚖️ vs 💰** ¿Ética o beneficios? ¿Son compatibles?

4. **🌍 vs 🏢** ¿Quién debe regular la IA: gobiernos o empresas?


---

## 🎉 Mensaje final

### 💡 **Recuerda:**

> **"Con gran poder (de IA) viene gran responsabilidad"**

**Tu código puede:**
- 🌟 Hacer el mundo más justo y equitativo
- 🚨 O perpetuar y amplificar discriminaciones

### 🎯 **La decisión es tuya como desarrollador**

**¿Qué tipo de futuro digital quieres construir?**
**Piensa en:**
- 👥 Los usuarios que las usarán
- 🌍 El impacto social de tus decisiones
- ⚖️ La equidad y justicia en tus algoritmos
- 🔮 Las consecuencias a largo plazo


---

**🔗 Próxima clase: Fundamentos técnicos de Python para IA**

*¡Gracias por vuestra atención y participación!* 🙌