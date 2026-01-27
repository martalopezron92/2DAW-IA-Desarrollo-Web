# Introducción al Machine Learning
---

## 1. ¿Qué es el Machine Learning?

### 1.1. Definición conceptual

El **Machine Learning** (Aprendizaje Automático) es una disciplina que permite a los ordenadores **aprender patrones a partir de datos** sin ser programados explícitamente para cada situación específica.

En lugar de escribir reglas concretas para resolver un problema, **el ordenador encuentra las reglas por sí mismo** observando ejemplos.

**Ejemplo sencillo:**
- **Programación tradicional:** Programas que un profesor apruebe a un alumno si su nota ≥ 5.
- **Machine Learning:** El ordenador observa miles de casos de alumnos (notas, asistencia, participación) y aprende qué patrón suelen tener los que aprueban, sin que nadie le diga explícitamente las reglas.

### 1.2. Diferencia entre programación tradicional y Machine Learning

| **Programación Tradicional** | **Machine Learning** |
|-------------------------------|----------------------|
| El programador escribe todas las reglas explícitamente | El sistema aprende las reglas a partir de ejemplos |
| Si cambia el problema, hay que reescribir el código | Si cambian los datos, el modelo se puede reentrenar |
| Funciona bien con reglas claras y simples | Funciona bien con problemas complejos o con muchas variables |
| Ejemplo: calcular el IVA de un producto | Ejemplo: detectar si un correo es spam |

**Idea clave:** En programación tradicional, tú defines la lógica. En Machine Learning, **los datos definen la lógica**.

### 1.3. ¿Por qué surge el Machine Learning?

El Machine Learning surge por la necesidad de resolver problemas donde:

- Hay **demasiadas variables** para programar todas las reglas manualmente.
- Las reglas **cambian con el tiempo** (por ejemplo, qué hace que un producto se venda bien).
- Las reglas son **difíciles de expresar** con código (por ejemplo, reconocer una cara humana).
- Hay **grandes cantidades de datos** disponibles que contienen información valiosa.

**Ejemplos de la vida real:**
- Recomendar películas en Netflix según tus gustos.
- Detectar transacciones fraudulentas en una tarjeta de crédito.
- Predecir qué clientes dejarán de usar un servicio web.
- Reconocer texto manuscrito o voz.

### 1.4. Qué NO es Machine Learning (ideas erróneas)

❌ **No es inteligencia artificial como en las películas.** El Machine Learning no piensa, no razona, no tiene conciencia. Solo encuentra patrones estadísticos en datos.

❌ **No es magia.** Es una herramienta matemática y estadística basada en datos.

❌ **No puede resolver cualquier problema.** Solo funciona bien en problemas donde existen patrones en los datos.

❌ **No sustituye al programador.** El programador sigue siendo necesario para preparar datos, elegir modelos, interpretar resultados y aplicarlos en aplicaciones reales.

❌ **No es infalible.** Los modelos pueden equivocarse, especialmente si los datos son malos o incompletos.

---

## 2. Relación entre datos y Machine Learning

### 2.1. El dato como materia prima

Los **datos son el combustible del Machine Learning**. Sin datos, no hay aprendizaje posible.

Un modelo de Machine Learning aprende observando ejemplos (datos). Cuantos más ejemplos de calidad tenga, mejor aprenderá.

**Analogía:** 
- Aprender a cocinar leyendo 5 recetas → conocimiento limitado.
- Aprender a cocinar con 5.000 recetas bien explicadas → conocimiento amplio.

Los datos alimentan al modelo igual que las recetas alimentan al cocinero.

### 2.2. Importancia de la calidad del dato

**No todos los datos son útiles.** La calidad del dato es fundamental:

- **Datos erróneos:** Si los datos contienen errores, el modelo aprenderá patrones incorrectos.
- **Datos incompletos:** Si faltan valores importantes, el modelo no podrá aprender correctamente.
- **Datos desactualizados:** Si los datos son antiguos, el modelo aprenderá patrones que ya no son válidos.
- **Datos sesgados:** Si los datos representan solo una parte de la realidad, el modelo no funcionará bien en situaciones reales.

**Ejemplo:**  
Si quieres crear un modelo para predecir el rendimiento académico de estudiantes, pero solo tienes datos de estudiantes que aprobaron, el modelo no sabrá reconocer a los estudiantes que podrían suspender.

### 2.3. Relación directa con el análisis y tratamiento de datos

El **análisis y tratamiento de datos** que ya habéis estudiado es la base del Machine Learning:

- **Limpieza de datos:** Eliminar errores, duplicados, valores faltantes.
- **Transformación de datos:** Normalizar, categorizar, estructurar.
- **Exploración de datos:** Entender qué información contienen.
- **Visualización de datos:** Detectar patrones, tendencias y anomalías.

**Machine Learning es el paso siguiente:** una vez que los datos están preparados y analizados, se usan para entrenar modelos que aprenden de ellos.

### 2.4. Consecuencias de trabajar con datos incorrectos o sesgados

Si los datos son de mala calidad, **el modelo aprenderá cosas incorrectas**. Esto se conoce como el principio **"basura entra, basura sale"** (*garbage in, garbage out*).

**Consecuencias reales:**

- **Discriminación:** Un modelo para filtrar candidatos a empleo entrenado con datos sesgados puede discriminar por género, edad o procedencia.
- **Errores médicos:** Un modelo de diagnóstico entrenado solo con datos de un tipo de paciente puede fallar con otros.
- **Malas decisiones empresariales:** Predecir mal las ventas puede causar pérdidas económicas.
- **Pérdida de confianza:** Los usuarios dejarán de confiar en un sistema que comete errores frecuentes.

**Idea clave:** La calidad de los datos determina la calidad del modelo. Sin buenos datos, no hay buen Machine Learning.

---

## 3. Tipos de problemas que puede resolver el Machine Learning

El Machine Learning puede resolver diferentes tipos de problemas. Los cuatro más importantes son:

### 3.1. Clasificación

**¿Qué problema resuelve?**  
Asignar una **etiqueta o categoría** a un elemento.

**¿Qué tipo de resultado produce?**  
Una categoría discreta (por ejemplo: "sí" o "no", "A", "B" o "C").

**Ejemplos claros:**
- Determinar si un correo electrónico es **spam o no spam**.
- Clasificar a un cliente como de **riesgo alto, medio o bajo** de impago.
- Predecir si un estudiante va a **aprobar o suspender** un examen.
- Identificar si una imagen contiene un **perro o un gato**.
- Detectar si una opinión en redes sociales es **positiva, negativa o neutra**.

**Característica principal:** La respuesta es siempre una **categoría predefinida**.

### 3.2. Regresión

**¿Qué problema resuelve?**  
Predecir un **valor numérico continuo**.

**¿Qué tipo de resultado produce?**  
Un número (por ejemplo: 23.5, 1.200, 87%).

**Ejemplos claros:**
- Predecir el **precio de una vivienda** según sus características (metros, ubicación, habitaciones).
- Estimar el **número de ventas** que tendrá un producto el próximo mes.
- Calcular la **nota esperada** de un alumno en el próximo examen.
- Predecir cuántos **visitantes** tendrá una página web mañana.
- Estimar el **tiempo de entrega** de un pedido.

**Característica principal:** La respuesta es un **número que puede tener decimales** y no pertenece a categorías fijas.

### 3.3. Agrupamiento (Clustering)

**¿Qué problema resuelve?**  
Encontrar **grupos naturales** dentro de un conjunto de datos, sin saber previamente cuáles son esos grupos.

**¿Qué tipo de resultado produce?**  
Grupos o segmentos de elementos similares entre sí.

**Ejemplos claros:**
- Agrupar **clientes** de una tienda online según su comportamiento de compra (compradores frecuentes, ocasionales, etc.).
- Segmentar **estudiantes** según su forma de estudiar (visuales, prácticos, teóricos).
- Identificar **tipos de usuarios** en una red social según sus intereses.
- Agrupar **artículos** de un periódico por temática sin etiquetar.
- Detectar **comunidades** en una red de contactos.

**Característica principal:** No sabemos de antemano cuántos grupos hay ni qué características tienen. El modelo los **descubre automáticamente**.

### 3.4. Detección de anomalías

**¿Qué problema resuelve?**  
Identificar elementos que **se comportan de forma diferente** al resto, que son raros o inusuales.

**¿Qué tipo de resultado produce?**  
Señalar qué elementos son normales y cuáles son anómalos.

**Ejemplos claros:**
- Detectar **transacciones fraudulentas** en una tarjeta de crédito (gastos inusuales).
- Identificar **fallos en un servidor** antes de que se caiga (comportamiento anormal en el sistema).
- Encontrar **estudiantes con patrones de estudio extraños** (posible trampa o problema).
- Detectar **productos defectuosos** en una cadena de producción.
- Identificar **accesos sospechosos** a un sistema informático.

**Característica principal:** Se busca lo que es **diferente o extraño**, no lo que es normal.

---

## 4. Tipos de aprendizaje en Machine Learning

Los modelos de Machine Learning pueden aprender de diferentes formas. Las tres principales son:

### 4.1. Aprendizaje supervisado

**¿Cómo funciona?**  
El modelo aprende a partir de **ejemplos etiquetados**, es decir, datos donde ya se conoce la respuesta correcta.

Es como aprender con un profesor que te dice si tu respuesta es correcta o no.

**Proceso:**
1. Se le muestran al modelo ejemplos con sus respuestas correctas.
2. El modelo aprende la relación entre las características de los ejemplos y las respuestas.
3. Una vez entrenado, puede predecir respuestas para nuevos ejemplos.

**Ejemplos:**
- Entrenar un modelo con miles de correos etiquetados como "spam" o "no spam" para que aprenda a detectar spam.
- Mostrar al modelo casas con su precio de venta conocido para que aprenda a predecir precios.
- Enseñar al modelo imágenes de perros y gatos (etiquetadas) para que aprenda a distinguirlos.

**Casos de uso:**  
Clasificación y regresión.

**Idea clave:** Siempre hay un "profesor" (las etiquetas) que indica cuál es la respuesta correcta.

### 4.2. Aprendizaje no supervisado

**¿Cómo funciona?**  
El modelo aprende a partir de **datos sin etiquetar**, es decir, sin conocer respuestas correctas previamente.

Es como explorar y descubrir patrones por ti mismo, sin que nadie te diga qué buscar.

**Proceso:**
1. Se le muestran al modelo datos sin respuestas.
2. El modelo busca patrones, similitudes o estructuras ocultas en los datos.
3. Agrupa o identifica información relevante por sí mismo.

**Ejemplos:**
- Agrupar clientes según su comportamiento sin saber de antemano qué tipos de clientes existen.
- Descubrir qué artículos se suelen comprar juntos en un supermercado.
- Identificar temas comunes en una colección de documentos sin etiquetar.

**Casos de uso:**  
Agrupamiento (clustering) y detección de anomalías.

**Idea clave:** No hay "profesor". El modelo explora los datos y encuentra patrones por sí mismo.

### 4.3. Aprendizaje por refuerzo (nivel conceptual)

**¿Cómo funciona?**  
El modelo aprende mediante **prueba y error**, recibiendo recompensas o castigos según sus acciones.

Es como aprender a jugar a un videojuego: si haces algo bien, ganas puntos; si lo haces mal, pierdes.

**Proceso:**
1. El modelo realiza una acción.
2. Recibe una recompensa (si la acción fue buena) o un castigo (si fue mala).
3. Con el tiempo, aprende qué acciones maximizan las recompensas.

**Ejemplos:**
- Entrenar un robot para caminar: recibe recompensa al avanzar y castigo al caerse.
- Enseñar a un sistema a jugar al ajedrez: gana puntos si gana partidas.
- Optimizar rutas de entrega: recompensa por entregar rápido y con bajo coste.

**Casos de uso:**  
Robótica, videojuegos, optimización de procesos.

**Idea clave:** El modelo aprende **experimentando** y mejorando con la práctica.

### 4.4. Comparación clara entre los tipos de aprendizaje

| **Tipo de aprendizaje** | **¿Hay respuestas correctas?** | **¿Cómo aprende?** | **Ejemplo típico** |
|-------------------------|--------------------------------|--------------------|-------------------|
| **Supervisado** | Sí, las respuestas están etiquetadas | Observando ejemplos con sus soluciones | Predecir si un alumno aprueba |
| **No supervisado** | No, no hay respuestas previas | Buscando patrones ocultos en los datos | Agrupar clientes por comportamiento |
| **Por refuerzo** | No directamente, hay recompensas | Probando acciones y viendo sus resultados | Entrenar un robot para moverse |

**Resumen:** El más usado es el **supervisado**, que es el que estudiaremos en temas siguientes.

---

## 5. Ciclo de vida de un proyecto de Machine Learning

Crear un modelo de Machine Learning **no es solo entrenar un algoritmo**. Es un proceso completo que forma parte de un proyecto real de software. Las fases principales son:

### 5.1. Fase 1: Definición del problema

**¿Qué queremos resolver?**  
Se define claramente qué problema de negocio o necesidad queremos abordar.

**Ejemplo:** "Queremos reducir el número de clientes que abandonan nuestra plataforma web."

**Preguntas clave:**
- ¿Es un problema que el Machine Learning puede resolver?
- ¿Qué resultado necesitamos obtener?
- ¿Cómo se medirá el éxito?

### 5.2. Fase 2: Recopilación y preparación de datos

**Obtener y preparar la materia prima.**

- Recopilar datos de bases de datos, APIs, archivos, logs, etc.
- Limpiar datos: eliminar errores, duplicados, valores faltantes.
- Transformar datos: normalizar, codificar variables categóricas, crear nuevas características.
- Dividir datos: separar en conjuntos de entrenamiento y prueba.

**Importante:** Esta fase suele ser la más larga del proyecto (60-80% del tiempo).

### 5.3. Fase 3: Entrenamiento del modelo

**Entrenar el algoritmo con los datos preparados.**

- Elegir el tipo de modelo adecuado (clasificación, regresión, etc.).
- Configurar parámetros del modelo.
- Entrenar el modelo con los datos de entrenamiento.
- Ajustar y mejorar el modelo iterativamente.

**Resultado:** Un modelo entrenado que ha aprendido patrones de los datos.

### 5.4. Fase 4: Evaluación del modelo

**Comprobar si el modelo funciona bien.**

- Probar el modelo con datos que no ha visto durante el entrenamiento.
- Medir su rendimiento: ¿acierta correctamente? ¿comete errores aceptables?
- Comparar con otros modelos.
- Decidir si está listo para usar o necesita mejoras.

**Pregunta clave:** ¿Es lo suficientemente bueno para nuestro problema?

### 5.5. Fase 5: Despliegue e integración

**Poner el modelo en producción, en una aplicación real.**

- Integrar el modelo en una aplicación web, móvil o sistema.
- Hacer que el modelo esté disponible para hacer predicciones en tiempo real.
- Configurar APIs o servicios para que otras aplicaciones lo usen.

**Ejemplo:** Publicar el modelo en un servidor para que la web pueda consultar si un correo es spam.

### 5.6. Fase 6: Monitorización y mantenimiento

**Vigilar el rendimiento del modelo en el tiempo.**

- Comprobar que el modelo sigue funcionando bien.
- Detectar si el rendimiento se degrada (los datos reales pueden cambiar).
- Reentrenar el modelo periódicamente con datos nuevos.
- Actualizar si las necesidades del negocio cambian.

**Idea clave:** El Machine Learning no termina cuando entrenas el modelo. Es un proceso continuo que requiere mantenimiento.

### 5.7. Relación con proyectos reales y aplicaciones web

En el desarrollo de aplicaciones web (como las que habéis estudiado):

- El **modelo de Machine Learning** es un componente más del sistema.
- Se consume como un **servicio o API** desde el backend.
- Los datos entran y salen como en cualquier otra funcionalidad web.
- Requiere **integración con bases de datos, interfaces de usuario y lógica de negocio**.

**Ejemplo práctico:**  
Una tienda online que recomienda productos:
1. El usuario navega por la web (frontend).
2. La aplicación envía información del usuario al backend.
3. El backend consulta el modelo de Machine Learning.
4. El modelo devuelve productos recomendados.
5. La web los muestra al usuario.

**El modelo es una pieza más en el engranaje completo de la aplicación.**

---

## 6. Entrenamiento vs predicción

Dos conceptos fundamentales que **NO debemos confundir**:

### 6.1. Entrenamiento (Training)

**¿Qué es?**  
Es el proceso mediante el cual el modelo **aprende** a partir de los datos.

**¿Cuándo ocurre?**  
Durante el desarrollo del proyecto, antes de poner el modelo en producción.

**¿Qué hace el modelo?**  
Observa miles o millones de ejemplos y ajusta sus parámetros internos para aprender patrones.

**¿Es rápido o lento?**  
Puede ser lento (minutos, horas o incluso días, dependiendo del tamaño de los datos y del modelo).

**¿Con qué frecuencia se hace?**  
Se hace una vez inicialmente, y se repite periódicamente para actualizar el modelo.

**Analogía:**  
Como un estudiante que estudia durante semanas para un examen.

**Ejemplo:**  
Entrenar un modelo con 10.000 correos electrónicos etiquetados como spam o no spam para que aprenda a reconocer spam.

### 6.2. Predicción (Prediction / Inference)

**¿Qué es?**  
Es el proceso en el que el modelo **usa lo que ha aprendido** para hacer predicciones sobre datos nuevos.

**¿Cuándo ocurre?**  
En producción, cuando el modelo ya está entrenado y se utiliza en una aplicación real.

**¿Qué hace el modelo?**  
Recibe un dato nuevo (que no ha visto antes) y devuelve una predicción basada en lo que aprendió.

**¿Es rápido o lento?**  
Es muy rápido (milisegundos o segundos).

**¿Con qué frecuencia se hace?**  
Continuamente, cada vez que un usuario o sistema consulta el modelo.

**Analogía:**  
Como un estudiante que responde preguntas en el examen usando lo que estudió.

**Ejemplo:**  
Un nuevo correo llega a tu bandeja de entrada. El modelo entrenado analiza el correo y predice en milésimas de segundo: "Este es spam".

### 6.3. Comparación clara

| **Aspecto** | **Entrenamiento** | **Predicción** |
|-------------|------------------|---------------|
| **Propósito** | Aprender patrones de los datos | Usar lo aprendido para nuevos datos |
| **Frecuencia** | Ocasional (una vez o periódicamente) | Continua (miles de veces al día) |
| **Velocidad** | Lento (puede tardar horas) | Rápido (milisegundos) |
| **Usa datos** | Datos históricos etiquetados | Datos nuevos sin etiquetar |
| **Resultado** | Un modelo entrenado | Una predicción específica |
| **Fase del proyecto** | Desarrollo | Producción |

### 6.4. Ejemplos sencillos

**Ejemplo 1: Sistema de recomendación de películas**
- **Entrenamiento:** El sistema analiza durante días las películas que han visto millones de usuarios y sus valoraciones. Aprende qué tipo de películas le gustan a cada perfil de usuario.
- **Predicción:** Cuando tú entras en la plataforma, el modelo te recomienda películas instantáneamente según tu perfil y lo que ha aprendido.

**Ejemplo 2: Filtro de spam**
- **Entrenamiento:** El modelo estudia 100.000 correos (50.000 spam, 50.000 legítimos) durante horas hasta aprender qué características tiene cada tipo.
- **Predicción:** Cada vez que recibes un correo nuevo, el modelo lo analiza en 0.01 segundos y decide si es spam o no.

### 6.5. Importancia de distinguir ambos conceptos

**¿Por qué es importante?**

- **Recursos:** El entrenamiento requiere más potencia de cálculo y tiempo. La predicción debe ser rápida para que la aplicación funcione bien.
- **Costes:** Entrenar puede ser costoso (requiere servidores potentes). Predecir es barato.
- **Arquitectura:** En producción, el modelo ya está entrenado y solo se usa para predecir. No se reentrena continuamente.
- **Separación de responsabilidades:** El equipo de desarrollo entrena el modelo; la aplicación en producción solo lo consulta.

**Idea clave:** Entrenamiento = aprender (fase de desarrollo). Predicción = usar lo aprendido (fase de producción).

---

## 7. Evaluación de modelos (nivel conceptual)

Una vez entrenado un modelo, debemos saber si **funciona bien** o no. La evaluación nos permite decidir si está listo para usarse.

### 7.1. ¿Qué significa que un modelo sea "bueno"?

Un modelo es "bueno" cuando:

- **Acierta con frecuencia:** Predice correctamente la mayoría de las veces.
- **Generaliza bien:** Funciona bien no solo con los datos de entrenamiento, sino también con datos nuevos que no ha visto.
- **Es útil para el problema:** Aporta valor real al negocio o aplicación.
- **Comete errores aceptables:** Los errores que comete no son graves para el contexto del problema.

**Importante:** La definición de "bueno" depende del problema. No todos los modelos necesitan ser perfectos.

### 7.2. Idea de acierto/error

Todo modelo comete **aciertos** y **errores**:

- **Acierto:** El modelo predice correctamente (ejemplo: dice que un correo es spam y realmente lo es).
- **Error:** El modelo predice incorrectamente (ejemplo: dice que un correo es legítimo pero era spam).

**Objetivo:** Maximizar los aciertos y minimizar los errores.

**Pregunta clave al evaluar:** ¿Cuántas predicciones correctas hace el modelo del total de predicciones?

### 7.3. Generalización

**¿Qué es la generalización?**  
Es la capacidad del modelo para **funcionar bien con datos nuevos**, no solo con los datos que vio durante el entrenamiento.

**¿Por qué es importante?**  
Un modelo que solo funciona con datos de entrenamiento no sirve en la realidad. Necesitamos que funcione en producción con datos nuevos y diferentes.

**Analogía:**  
Un estudiante que memoriza las respuestas de un examen de años anteriores puede sacarlo perfecto si le ponen ese mismo examen. Pero si le cambian las preguntas, suspende. Ese estudiante no ha "generalizado" el conocimiento; solo ha memorizado.

**Lo que queremos:** Un modelo que entienda los patrones generales, no que memorice los ejemplos concretos.

### 7.4. Sobreajuste (Overfitting)

**¿Qué es el sobreajuste?**  
Ocurre cuando el modelo aprende **demasiado bien** los datos de entrenamiento, incluyendo ruido y detalles irrelevantes, y por eso **no generaliza bien** a datos nuevos.

**Síntomas:**
- El modelo funciona perfectamente con los datos de entrenamiento.
- Pero funciona mal con datos nuevos.

**Analogía:**  
Un estudiante que memoriza palabra por palabra los ejercicios del libro. Saca 10 si le preguntan exactamente esos ejercicios, pero suspende si le cambian ligeramente el enunciado.

**Ejemplo:**  
Un modelo de predicción de notas que aprende que "todos los alumnos llamados Pedro aprueban" porque en los datos de entrenamiento había 3 alumnos llamados Pedro y los 3 aprobaron. Cuando llega un nuevo Pedro, predice que aprobará aunque no estudie. El modelo memorizó algo irrelevante (el nombre) en lugar de aprender lo importante (horas de estudio, asistencia, etc.).

**Causas del sobreajuste:**
- Modelos demasiado complejos.
- Pocos datos de entrenamiento.
- Entrenar durante demasiado tiempo.

**Soluciones (conceptual):**
- Usar más datos.
- Simplificar el modelo.
- Detener el entrenamiento antes de que memorice.

### 7.5. Subajuste (Underfitting)

**¿Qué es el subajuste?**  
Ocurre cuando el modelo es **demasiado simple** y no consigue aprender los patrones importantes de los datos.

**Síntomas:**
- El modelo funciona mal tanto con datos de entrenamiento como con datos nuevos.

**Analogía:**  
Un estudiante que estudia muy poco y solo lee el título del tema. No entiende ni lo básico.

**Ejemplo:**  
Un modelo de predicción de precios de vivienda que solo considera el número de habitaciones, ignorando la ubicación, el estado, el tamaño, etc. Es demasiado simple y no aprende bien.

**Causas del subajuste:**
- Modelos demasiado simples.
- Pocos datos o datos de mala calidad.
- No entrenar suficientemente.

**Soluciones (conceptual):**
- Usar modelos más complejos.
- Entrenar más tiempo.
- Añadir más características relevantes.

### 7.6. El equilibrio ideal

El objetivo es encontrar el **equilibrio perfecto** entre sobreajuste y subajuste:

- **No demasiado simple:** Que aprenda los patrones importantes.
- **No demasiado complejo:** Que no memorice detalles irrelevantes.
- **Generaliza bien:** Funciona tanto con datos de entrenamiento como con datos nuevos.

**Representación visual conceptual:**

```
Subajuste          Equilibrio          Sobreajuste
   ↓                   ↓                     ↓
Muy simple    →  Complejidad  →         Muy complejo
Aprende poco    Aprende bien      Memoriza todo
```

**Idea clave:** Un buen modelo aprende lo esencial sin memorizar los detalles.

---

## 8. Límites, riesgos y consideraciones éticas

El Machine Learning es una herramienta poderosa, pero tiene **limitaciones importantes** y puede causar **problemas serios** si no se usa de forma responsable.

### 8.1. El modelo no piensa ni razona

**Realidad fundamental:**  
Un modelo de Machine Learning **no entiende** lo que hace. No tiene conciencia, no razona, no comprende conceptos.

Solo encuentra **correlaciones estadísticas** en los datos. Ve patrones numéricos, no significados.

**Ejemplo:**  
Un modelo puede aprender que "los correos con la palabra 'gratis' suelen ser spam", pero no entiende qué significa "gratis" ni por qué los humanos consideramos algo spam. Solo ve que esa palabra aparece con frecuencia en correos etiquetados como spam.

**Consecuencia:**  
El modelo puede hacer cosas que parecen inteligentes, pero en realidad solo está siguiendo patrones. Si los datos cambian, el modelo puede fallar sin "darse cuenta".

### 8.2. Dependencia total de los datos

**Realidad:**  
El modelo **solo puede aprender lo que hay en los datos**. Si algo no está representado en los datos de entrenamiento, el modelo no lo sabrá.

**Ejemplo:**  
Si entrenas un modelo de reconocimiento de frutas solo con imágenes de manzanas y plátanos, no podrá reconocer una naranja aunque sea obvio para un humano.

**Problemas derivados:**
- Si los datos están desactualizados, el modelo dará respuestas anticuadas.
- Si los datos no representan todos los casos posibles, el modelo fallará en situaciones no vistas.
- Si los datos son escasos, el modelo no aprenderá bien.

### 8.3. Sesgos y errores

**¿Qué son los sesgos?**  
Son **distorsiones en los datos** que hacen que el modelo aprenda patrones injustos, incorrectos o discriminatorios.

**Origen de los sesgos:**
- **Sesgos históricos:** Los datos reflejan prejuicios pasados de la sociedad.
- **Sesgos de recopilación:** Los datos no representan equitativamente todos los grupos.
- **Sesgos de etiquetado:** Los humanos que etiquetaron los datos tenían prejuicios.

**Ejemplos reales de sesgos:**

1. **Sesgo de género:**  
   Un modelo de selección de personal entrenado con datos históricos de una empresa donde solo contrataban hombres para puestos técnicos. El modelo aprende a descartar automáticamente candidatas mujeres.

2. **Sesgo racial:**  
   Un modelo de reconocimiento facial entrenado principalmente con imágenes de personas de piel clara. Funciona mal con personas de piel oscura.

3. **Sesgo socioeconómico:**  
   Un modelo de concesión de créditos entrenado con datos de una zona rica. Rechaza automáticamente solicitudes de personas de zonas pobres.

4. **Sesgo de edad:**  
   Un modelo de recomendación de empleo que solo sugiere puestos de baja responsabilidad a personas mayores porque en los datos históricos así era.

**¿Puede un modelo ser racista, sexista o discriminatorio?**  
El modelo en sí no tiene intenciones, pero **reproduce los sesgos que hay en los datos**. Si los datos contienen discriminación, el modelo la aprenderá y la aplicará.

**Gravedad del problema:**  
Los sesgos no son solo errores técnicos. Pueden causar **daño real a personas**: impedir que alguien consiga un trabajo, acceda a un crédito, reciba un tratamiento médico, o sea tratado injustamente por su género, raza o edad.

### 8.4. Errores de predicción y sus consecuencias

Todo modelo comete errores. Pero **no todos los errores son igual de graves**.

**Tipos de consecuencias según el contexto:**

**Errores leves (bajo impacto):**
- Recomendar una película que no te gusta.
- Mostrar un anuncio irrelevante.
- Predecir mal el tiempo mañana.

**Errores graves (alto impacto):**
- Diagnosticar incorrectamente una enfermedad.
- Rechazar una solicitud de empleo a una persona cualificada.
- Identificar erróneamente a alguien como sospechoso de un crimen.
- Aprobar un préstamo a alguien que no podrá pagarlo.

**Principio fundamental:**  
Cuanto mayor sea el impacto en las personas, mayor debe ser el cuidado al usar Machine Learning.

### 8.5. Importancia del criterio humano

**El Machine Learning no debe tomar decisiones críticas de forma autónoma.**

**Buenas prácticas:**

- **Supervisión humana:** Las decisiones importantes deben ser revisadas por personas.
- **Transparencia:** Explicar cómo y por qué el modelo toma decisiones.
- **Responsabilidad:** Siempre debe haber un responsable humano de las consecuencias.
- **Revisión continua:** Monitorizar el modelo para detectar errores o sesgos.
- **Posibilidad de apelación:** Las personas afectadas deben poder cuestionar las decisiones del modelo.

**Ejemplo:**  
Un modelo puede sugerir candidatos para un puesto de trabajo, pero **el responsable de recursos humanos debe tomar la decisión final** tras revisar manualmente los casos.

**Idea clave:** El Machine Learning es una herramienta de apoyo a la decisión humana, **no un sustituto del juicio humano**.

### 8.6. Responsabilidad ética del desarrollador

**Como futuros desarrolladores, tenéis una responsabilidad importante:**

- **Conocer los límites:** Saber qué puede y qué no puede hacer el Machine Learning.
- **Cuestionar los datos:** ¿Son representativos? ¿Contienen sesgos?
- **Evaluar el impacto:** ¿A quién puede perjudicar este modelo?
- **Diseñar con ética:** Priorizar la justicia y el bienestar de las personas.
- **Comunicar claramente:** Explicar las limitaciones del modelo a los usuarios y clientes.
- **Decir "no":** Rechazar proyectos que puedan causar daño o discriminación.

**Pregunta esencial antes de desplegar un modelo:**  
¿Estaría dispuesto a aceptar las consecuencias si este modelo se equivoca con alguien de mi familia?

### 8.7. Casos reales de problemas éticos

**Algunos casos reales que han ocurrido:**

1. **Amazon (2018):** Canceló un sistema de selección de personal porque discriminaba a mujeres. El modelo había aprendido de datos históricos donde se contrataban principalmente hombres.

2. **Sistemas de reconocimiento facial:** Han sido prohibidos en algunas ciudades porque presentaban tasas de error mucho mayores en personas de piel oscura.

3. **Modelos de predicción de reincidencia criminal:** Han mostrado sesgos raciales, prediciendo mayor riesgo de reincidencia en personas de minorías étnicas.

4. **Sistemas de publicidad:** Han mostrado anuncios de empleos bien pagados principalmente a hombres y anuncios de empleos de baja cualificación a mujeres.

**Lección:** La tecnología no es neutra. Refleja los valores y sesgos de quien la crea y de los datos con los que se entrena.

---

## 9. Resumen final del tema

### 9.1. Ideas clave que el alumnado debe recordar

#### Sobre el Machine Learning en general:

1. **Machine Learning es aprendizaje automático a partir de datos**, no programación manual de reglas.

2. **Los datos son el combustible**: sin datos de calidad, no hay buen modelo.

3. **El modelo encuentra patrones estadísticos**, no piensa ni razona.

4. **Hay diferentes tipos de problemas**: clasificación, regresión, agrupamiento y detección de anomalías.

5. **Existen diferentes formas de aprender**: supervisado (con respuestas), no supervisado (sin respuestas) y por refuerzo (prueba y error).

#### Sobre el proceso:

6. **Entrenar ≠ Predecir**: entrenar es aprender (desarrollo), predecir es usar lo aprendido (producción).

7. **El ciclo de vida de un proyecto de ML tiene múltiples fases**: desde definir el problema hasta mantener el modelo en producción.

8. **Un buen modelo generaliza**: funciona bien con datos nuevos, no solo con los de entrenamiento.

9. **Sobreajuste = memorizar detalles irrelevantes** y no generalizar bien.

10. **Subajuste = ser demasiado simple** y no aprender los patrones importantes.

#### Sobre límites y ética:

11. **El modelo solo aprende lo que hay en los datos**. Si los datos son sesgados, el modelo será sesgado.

12. **Machine Learning puede discriminar y cometer errores graves** si no se usa responsablemente.

13. **Siempre debe haber criterio humano** supervisando y tomando decisiones finales.

14. **Los desarrolladores tienen responsabilidad ética** sobre los sistemas que crean.

---

### 9.2. Lista de conceptos fundamentales

**Conceptos que debes dominar para el examen:**

#### Definiciones básicas:
- Machine Learning
- Programación tradicional vs Machine Learning
- Dato como materia prima
- Calidad del dato
- Sesgo en los datos

#### Tipos de problemas:
- Clasificación
- Regresión
- Agrupamiento (clustering)
- Detección de anomalías

#### Tipos de aprendizaje:
- Aprendizaje supervisado
- Aprendizaje no supervisado
- Aprendizaje por refuerzo

#### Fases y procesos:
- Ciclo de vida de un proyecto de ML
- Entrenamiento
- Predicción (inferencia)
- Evaluación de modelos
- Despliegue
- Monitorización

#### Evaluación:
- Generalización
- Sobreajuste (overfitting)
- Subajuste (underfitting)
- Acierto y error

#### Ética y límites:
- Sesgo algorítmico
- Discriminación algorítmica
- Responsabilidad ética
- Supervisión humana
- Transparencia

