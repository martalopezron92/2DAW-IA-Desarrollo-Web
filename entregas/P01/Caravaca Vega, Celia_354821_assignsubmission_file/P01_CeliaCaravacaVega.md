# Investigación![](Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.001.png)
![](Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.002.png)

31/10/2025  optativa CURSO:2ºDAW  Celia Caravaca Vega 

![ref1]

**índice ![](Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.004.png)**

[**El futuro de la IA en el desarrollo web  1**](#_page3_x60.00_y56.70) **[Áreas de investigación:  1](#_page3_x60.00_y106.80)** 

1. [Resumen ejecutivo  6](#_page8_x60.00_y56.70) 
1. [Introducción  6](#_page8_x60.00_y555.90) [Contexto  6](#_page8_x60.00_y598.30) [Objetivos específicos  7](#_page10_x60.00_y56.70) [Metodología  7](#_page10_x60.00_y316.30) 
1. [Estado actual de la IA en desarrollo web  7](#_page10_x60.00_y401.10) 
   1. [IA en Frontend  7](#_page10_x60.00_y431.50) 
   1. [IA en Backend  8](#_page11_x60.00_y83.10) 
   1. [Barreras y limitaciones  8](#_page11_x60.00_y386.30) 
1. [Tendencias emergentes  8](#_page11_x60.00_y552.70) 
1. [Impacto en empleo y competencias  9](#_page12_x60.00_y87.50) [Nuevos roles  9](#_page12_x60.00_y127.90) [Competencias híbridas  9](#_page12_x60.00_y232.70) 

   [Herramientas no‑code/low‑code(Herramienta para crear aplicaciones web con interfaces gráficas)  9](#_page12_x60.00_y331.90) 

   [Colaboración humano‑IA  9](#_page12_x60.00_y402.30) 

6. [Casos de estudio  9](#_page12_x60.00_y487.10) **[Caso de éxito Lovable.dev  9](#_page12_x60.00_y523.20)** [Caso de fracaso  Builder.ai  11](#_page15_x60.00_y150.30) 

   7. [Predicciones y escenarios futuros  12](#_page16_x60.00_y231.90) [2‑3 años  12](#_page16_x60.00_y262.30) [5‑10 años  12](#_page16_x60.00_y355.10) 

      [Las IA podrán generar una pag con las especificaciones exactas que le des sin la necesidad de que algún humano introduzca código.  12](#_page16_x60.00_y402.30) 

      [Escenarios alternativos  12](#_page16_x60.00_y508.30) [Recomendaciones para profesionales  12](#_page16_x60.00_y720.30) 

8. [Conclusiones y reflexión personal  13](#_page17_x60.00_y198.30) 
8. [Referencias bibliográficas  13](#_page17_x60.00_y461.50) 

# <a name="_page3_x60.00_y56.70"></a>**El futuro de la IA en el desarrollo web  ![](Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.005.png)**
## <a name="_page3_x60.00_y106.80"></a>*Áreas de investigación:* 
1. IA en Frontend  
- Generación automática de código: GitHub Copilot, CodeT5, etc. 
- Diseño asistido por IA: Figma AI, Adobe Sensei 
- Optimización de UX: Personalización automática, A/B testing inteligente 
- Accesibilidad automatizada: Detección y corrección de problemas 
- ¿Cómo están cambiando estas herramientas el flujo de trabajo frontend?  

  Estas herramientas nos hacen tener más facilidades a la hora de trabajar con el frontend como por ejemplo hacer entregas más rápidas, automatizar tareas repetitivas,mejorar el rendimiento y más mantenibilidad. 

- ¿Qué tareas se están automatizando y cuáles permanecen humanas?  Tareas automatizadas: 
- El linting del código(Es una herramienta de software que analiza código):  Cuando usamos CI (La Integración Continua) nos permite ejecutar linters(analizador estático de código) automáticamente y nos  asegura un código consistente. 
- Construcción y pruebas:  

  La tarea de crear código y probarlo se hace automáticamente a través de CI(Integración continua), por lo que nos facilita la depuración y nos garantiza un entorno parecido al del usuario. 

- Publicación de código: GitLab Pages automatiza la publicación de código, incluso en situaciones con conexiones a internet inestables. 

  **Intervención humana:** 

- Analizar y corregir problemas:  

  Puede que el CI/CD(Despliegue continuo) pueda detectar problemas (como el código que no pasa el linting o pruebas lentas), por lo que la corrección y mantenimiento de estos generados por IA siguen siendo la responsabilidad de los desarrolladores.

- Mejoras en el rendimiento: ![ref1]

  Independientemente de los problemas detectados en el rendimiento, quienes deciden cómo solventarlos son los gerentes de producto y equipo. 

- Creación y mantenimiento de canalización CI/CD: 

  Este CI/CD requiere de conocimiento técnico y ajustes continuos de personas. 

2. IA en Backend: 
- APIs inteligentes: Procesamiento de lenguaje natural, visión por computadora 
- Optimización de bases de datos: Tuning automático, predicción de carga 
- DevOps inteligente: Deployment automático, detección de anomalías 
- Microservicios adaptativos: Auto-scaling basado en IA 
- ¿Cómo mejora la IA la eficiencia y escalabilidad del backend? 

. 

- Con los diseñó para flujos de trabajo asincrónicos(no siguen un orden o línea) y paralelos(acorde a una estructura): Este método evita bloquear las respuestas de las APIs y hace una mejora en el rendimiento al descargar tareas grandes a las colas de tarea. 
- Los docker y orquestación con kubernetes(aplicación que orquesta los dokers):  Permite escalar de forma eficiente muchos modelos de IA como microservicios y a parte nos facilita las actualizaciones. 
- Usar infraestructura optimizada para GPU: Con esto aceleramos el procesamiento de modelos que requieren una GPU, optimizando el uso de recursos y mejorando la capacidad de respuesta. 
- ¿Qué nuevos patrones arquitectónicos están emergiendo? 
- Los tres patrones arquitectónicos: 
- Microservicios con Kubernetes: Desacoplar servicios en microservicios y gestiona y coordina con Kubernetes para mayor modularidad y escalabilidad. 
- Capa de inferencia dedicada con GPU: Crear una capa específica optimizada para modelos que requieren aceleración por GPU. 
- Uso de Model Serving (TorchServe o TF Serving): Utilizar servidores de modelos para gestionar la inferencia de manera más eficiente. 
3. Nuevas profesiones y competencias  ![ref1]
- Roles emergentes: AI Engineer, Prompt Engineer, ML Ops 
- Competencias híbridas: Desarrollador + conocimientos de IA 
- Herramientas no-code/low-code: Democratización del desarrollo 
- Colaboración humano-IA: Mejores prácticas 
- ¿Qué competencias debe desarrollar para ser competitivo? 

  Para ser competitivo con respecto a la amenaza de la IA, debemos desarrollar una combinación de competencias técnicas y blandas.Concretamente: 

  - Técnicas: 
    - Lenguajes de programación: Python, R y SQL. 
    - Matemáticas y estadística: Álgebra lineal, cálculo, probabilidad y estadística. 
    - Frameworks de Machine Learning: TensorFlow, PyTorch y scikit-learn. 
    - Deep Learning: CNNs, RNNs/LSTM y Transformers. 
    - Data Engineering y Big Data: Hadoop, Spark, AWS EMR, Google BigQuery, Azure Databricks, ETL. 
    - Cloud Platforms: AWS, Azure, Google Cloud Platform. 
    - MLOps: Docker, Kubernetes, Mlflow. 
  - Blandas: 
    - Comunicación y Storytelling: Capacidad de comunicar ideas complejas de forma clara. 
    - Colaboración y Trabajo en Equipo: Habilidad para trabajar con equipos multidisciplinarios. 
    - Pensamiento Crítico y Resolución de Problemas: Capacidad para diagnosticar problemas y encontrar soluciones. 
    - Adaptabilidad y Aprendizaje Continuo: Disposición para adaptarse a los cambios y aprender nuevas tecnologías. 
    - Creatividad e Innovación: Capacidad de proponer soluciones nuevas y eficientes. 
- ¿Cómo evolucionará mi rol como desarrollador web? 

Por como van las cosas evolucionaremos de ser un codificador manual a un orquestador, estratega y colaborador de ecosistemas de desarrollo impulsados por IA.  

Tendremos que hacer estás cosas para adaptarnos: 

- proporcionar contexto: Darle a la IA la información necesaria para generar código preciso y útil. 
- Aportar juicio y estrategia: Combinar la eficiencia de la IA y el trabajo en equipo humanos. 
- Aprender continuamente: Adaptarse a las nuevas tecnologías y habilidades a medida que evolucionan. 
4. Casos de éxito y fracasos Casos de éxito sugeridos: ![ref1]
- Netflix: Sistema de recomendaciones personalizado  
- Shopify: Magic - generación automática de tiendas 
- Grammarly: Corrección de texto en tiempo real  
- Canva: Generación automática de diseños  

Casos de fracaso sugeridos: 

- Microsoft Tay: Chatbot que aprendió comportamientos tóxicos 
- IBM Watson for Oncology: Sobre Promesas en diagnóstico médico  
- Quill: Plataforma de generación de contenido que no cumplió expectativas  

Preguntas guía:  

- ¿Qué factores contribuyeron al éxito o fracaso? 

**Factores que contribuyeron al éxito:** 

- Tener claro lo que quieres y cómo lo harás:  

  Los proyectos que tienen objetivos de negocio bien claros y la IA se utilizaba como una herramienta para conseguirlos . 

- Datos de alta calidad:  

  El uso de varios datos, bien curados y relevantes para el dominio específico es crucial. 

- Supervisión de personas: 

  ` `La supervisión de personas y la validación de los resultados de la IA es muy esencial para garantizar precisión, seguridad y la ética del proyecto. 

- Pruebas repetitivas: 

  ` `El desarrollo repetitivo y las pruebas continuas permiten la adaptación y la mejora de los modelos de IA. 

- Integrar la IA con datos existentes de la empresa:  

  La integración de la IA con los sistemas y procesos existentes facilitó la adopción y el impacto. 

**Factores que contribuyeron al fracaso:** 

- Tratar la tecnología como la solución a todo:  

  El error más normal es considerar la IA como una solución mágica que lo resuelve todo, en lugar de una herramienta para mejorar. 

- Datos no filtrados o sesgados: ![ref1]

  ` `El uso de datos sin curación o con sesgos lleva a resultados inexactos, discriminatorios o perjudiciales. 

- Falta de conocimiento en el dominio:  

  La falta de conocimiento en el dominio concreto resulta en modelos de IA ineficaces. 

- Falta de reglas claras:  

  La ausencia de reglas y objetivos claros nos dificulta encontrar el éxito e identificar problemas. 

- Supervisión del personal inadecuada:  

  La falta de supervisión del personal y validación de los resultados de la IA nos lleva a errores y riesgos. 

- ¿Qué lecciones podemos extraer para futuros proyectos? 
- Priorizar la estrategia sobre la herramientas que utilizaremos:  

  Definir primero los objetivos de negocio y luego seleccionar las herramientas de IA adecuadas. 

- Invertir en la calidad de los datos:  

  Asegurarse de que los datos sean precisos, diversos y libres de sesgos para evitar posibles errores y evitar mal informar al usuario. 

- Incorporar la experiencia en el dominio:  

  Involucrar a expertos en el dominio para garantizar que los modelos de IA sean relevantes y efectivos. 

- Establecer métricas claras:  Definir métricas y objetivos claros para medir el éxito y la mejora continua. 
- Mantener la supervisión de personas: 

  ` `Implementar procesos de supervisión de personas y validar para garantizar la precisión, la seguridad y la ética. 

- Adoptar un enfoque repetitivo: 

  ` `Desarrollar y probar los modelos de IA de forma repetitiva, adaptándose a medida que se aprende más sobre el problema. 
1. ## *Resumen<a name="_page8_x60.00_y56.70"></a> ejecutivo ![ref1]*
La inteligencia de la IA ha cambiado mucho el frontend y el backend. 

- En el frontend, herramientas para generar código y diseño personalizado permiten a los equipos crear interfaces mucho más rápido que hacerlo a mano. 
- En el backend, APIs inteligentes, optimización automática de bases de datos y DevOps(Conjunto de prácticas que agrupan el desarrollo de software) con IA están mejorando la escalabilidad, eficiencia y fiabilidad de los sistemas. 
- Este cambio ha modificando los perfiles profesionales: roles 

  como AI Engineer(Desarrollador de inteligencia 

  artificial), Prompt Engineer(Ingeniero de instrucciones de entrada) 

  ` `y ML Ops(prácticas y herramientas para aprendizaje automático) están ganando protagonismo, mientras que la necesidad de que una persona utilice la IA aumenta. 

- Las oportunidades para desarrolladores web son más, automatización de tareas repetitivas, nuevos servicios basados en IA, aceleración de productos… 
- Pero también existen amenazas: necesidad de adquirir nuevas competencias, competencia más intensa, posibles desplazamientos de tareas rutinarias. 
- De cara al futuro (2‑10 años), se espera que la IA pase de ser una herramienta de apoyo a integrarse como componente central del desarrollo web, con agentes autónomos, código generado automáticamente, experiencias ultra‑personalizadas y arquitecturas que se adaptan por sí mismas.  
- Para nuestra rama, la clave será mantenerse actualizados, adoptar un enfoque híbrido (desarrollo + IA) y centrarse en tareas que requieren creatividad, visión humana y empatía(Todo lo que no tiene la IA por ahora). 
- Este informe analiza el estado actual, las tendencias emergentes, el impacto en empleo y competencias, presenta casos reales de éxito, y ofrece predicciones con tres escenarios posibles (positivos, realistas y negativos). 
2. ## Introducción<a name="_page8_x60.00_y555.90"></a> 
### <a name="_page8_x60.00_y598.30"></a>Contexto 
El desarrollo web se ha desarrollado mucho durante el tiempo (nuevos frameworks, prácticas ágeis(adaptabilidad, colaboración y entrega continua de valor al cliente), DevOps,).  

En paralelo, la IA ha evolucionado desde sistemas de soporte hasta convertirse en una tecnología integrada en casi todos los ámbitos del software. 

` `En este contexto, entender cómo la IA nos afecta en el desarrollo web es muy necesario. 

` `![ref1]

<a name="_page10_x60.00_y56.70"></a>Objetivos específicos ![ref1]Objetivos: 

- Investigar aplicaciones actuales y futuras de IA en desarrollo web. 
- Analizar el impacto de la IA en las profesiones del sector tecnológico. 
- Evaluar oportunidades y amenazas para desarrolladores web. 
- Comunicar hallazgos de forma clara y estructurada. 
- Desarrollar criterio sobre la evolución tecnológica del sector. 
- Investigar cómo la IA está siendo aplicada actualmente en el desarrollo web (frontend y backend). 
### <a name="_page10_x60.00_y316.30"></a>Metodología 
La investigación se basa en buscar los datos necesarios de páginas recientes para contestar el los objetivos mencionados anteriormente y saber cómo poder avanzar . También se incluyen casos reales de empresas. 
3. ## Estado<a name="_page10_x60.00_y401.10"></a> actual de la IA en desarrollo web 
1. ### IA<a name="_page10_x60.00_y431.50"></a> en Frontend 
En el ámbito frontend, aparecen herramientas de generación automática de código y diseño asistido.  

Por ejemplo, la herramienta Stitch de Google permite convertir prompts de texto y referencias visuales en diseños UI(Interfaz de usuario) completos y en código frontend funcional. 

Por lo que esto modifica la forma de realizar el trabajo(menos tiempo en maquetación, poder prestarle más atención a la validación de diseño y lógica de negocio).  

Sin embargo, hay muchas tareas que deben de realizar las personas : la definición del producto, la usabilidad, la accesibilidad, la revisión de código, a lo que se refiere el usuario. 

También se observa que la IA puede acelerar prototipos, pero aún depende de supervisión para calidad, coherencia y pensado de UX(Experiencia del usuario)  

La personalización automática de UX y la optimización de accesibilidad están cada vez más utilizados: adaptaciones de interfaz según perfil de usuario, test A/B (Comparar dos elementos de la página)inteligentes, ajustes dinámicos de layout … 

(veremos ejemplo en tendencias más adelante). ![ref1]
2. ### IA<a name="_page11_x60.00_y83.10"></a> en Backend 
En el backend, la IA se incorpora en varios niveles:  

- optimización de bases de datos 
- mejora del rendimiento 
- automatización de DevOps 
- APIs inteligentes. 

` `Encontré en un artículo que “la adopción del desarrollo de backend impulsado por IA” ya está en curso:  

herramientas para optimización de consultas, documentación automática de APIs, detección de anomalías.[ ](https://www.arunangshudas.com/blog/8-trends-in-backend-development-you-cant-ignore-in-2025/?utm_source=chatgpt.com) 

Las arquitecturas modernas (microservicios, serverless(Computación sin servidor)) se integran con IA para escalar automáticamente, ajustar cargas y ofrecer servicios inteligentes.  

Por ejemplo, los sistemas backend van más allá de servir datos y comienzan a “razonar” (predicción de carga, adaptabilidad). 
3. ### Barreras<a name="_page11_x60.00_y386.30"></a> y limitaciones 
A pesar del gran progreso, existen unas limitaciones:  

calidad y seguridad del código generado automáticamente (por ejemplo, un estudio muestra que los LLMs(IA entrenada con cantidad masiva de texto para entender a las personas) aún presentan errores de seguridad en backends generados).[ ](https://arxiv.org/abs/2502.11844?utm_source=chatgpt.com) 

También hay cuestiones éticas, de privacidad, de dependencia tecnológica, y de coste de adopción (infraestructura de IA, entrenamiento de modelos, talento especializado). 
4. ## Tendencias<a name="_page11_x60.00_y552.70"></a> emergentes 
Las principales tendencias que se son: 

- Integración más profunda de IA en interfaces web: personalización en tiempo real, ajustes basados en comportamiento del usuario. 
- Herramientas que generan automáticamente código y no solo sugerencias: ya en frontend y apuntando al backend. 
- Plataformas de desarrollo «IA‑nativas», donde la IA no es solo un añadido, sino parte del flujo por defecto (archivos, despliegue, testeo) 
- Mayor inversión y creación de startups centradas en desarrollar herramientas IA para desarrolladores web. 
- Aumento del uso de arquitecturas adaptativas, microservicios inteligentes, edge computing combinado con IA. ![](Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.006.png)
5. ## Impacto<a name="_page12_x60.00_y87.50"></a> en empleo y competencias 
### <a name="_page12_x60.00_y127.90"></a>Nuevos roles 
Roles como Prompt Engineer, AI Engineer, ML Ops, y “agent operations” aparecen. 

Se demanda talento que mezcle conocimientos de IA, desarrollo de software y entendimiento del negocio. 
### <a name="_page12_x60.00_y232.70"></a>Competencias híbridas 
Ya no basta con saber HTML/CSS/JS, es cada vez más valorado entender IA, saber trabajar con modelos, API inteligentes, generar prompts(instrucciones que se le dan a la IA para guiar su respuesta), implementar personalización, colaborar con IA en el flujo de trabajo. 
### <a name="_page12_x60.00_y331.90"></a>Herramientas no‑code/low‑code(Herramienta para crear aplicaciones web con interfaces gráficas) 
Estas plataformas hacen que  perfiles con menor especialización técnica puedan usarlo fácilmente, lo cual puede cambiar la dinámica del empleo. 
### <a name="_page12_x60.00_y402.30"></a>Colaboración humano‑IA 
Aunque la IA automatiza muchas tareas (por ejemplo prototipado rápido, generación de código), el desarrollador sigue siendo muy necesario en los puntos como supervisión, validación, creatividad, diseño de experiencia, ética y estrategia. 
6. # Casos<a name="_page12_x60.00_y487.10"></a> de estudio 
### <a name="_page12_x60.00_y523.20"></a>Caso de éxito Lovable.dev 
Lovable.dev es una plataforma para crear aplicaciones web utilizando IA sin tener que escribir código. 

Más o menos tienen 70-80% Generado con IA y el resto se supervisa manualmente. ¿Qué problemas resuelve en el desarrollo web a mano? 

Por un lado 

Que cualquier persona que tenga manejo con el internet, comunicación con IA pueda crear una web sin muchos conocimientos. 

Por el otro lado  

Los que están dedicados al frontend y backend se quedan como comprobadores de código y dejan de crear para empezar a supervisar estos códigos y mejorarlos. ![ref1]

Resultados  

Poco después de su lanzamiento este año consiguió 100 millones de dólares poco después de su lanzamiento. 

La empresa tiene más de miles de usuarios que la usan con la IA por texto. 

Su impacto hace que no sea necesario contratar a alguien que te lo haga pagas y te lo hace la IA mucho más rápido(pero sin alma) 

Está empresa ha popularizado su sistema de “vive-coding” que permite crear aplicaciones solo escribiendo y esto llama a los desarrolladores con que pueden crear prototipos muy rápido por que no les hace falta escribir desde cero el código y pueden lanzar aplicaciones en poco tiempo lo que les hace trabajar más rápido y eficientemente.  

Y algunos factores que le hicieron triunfar son: 

Interfaz muy fácil de interpretar: Al utilizar la IA hace que personas como emprendedores,diseñadores o estudiantes puedan crear webs cosa que antes solo los desarrolladores web expertos podían hacer. 

La potencia de la IA: Como la IA maneja frontend y backend, puede desplegar aún si el código está sin terminar. 

Integración : Usa los servicios de Superbase como otros más para tener bases de datos y le facilita crear el backend sin complicarse demasiado. 

Se despliega rápido: La IA utiliza “review & deploy” que primero revisa el proyecto y luego lo despliega, lo que agiliza el ciclo del desarrollo. 

¿Qué debemos de aprender de  Lovable.dev? 

1. Adaptarse a trabajar con la IA en vez de sustituirlos 

   Lavoble nos enseña que la IA no nos remplaza si no nos da más capacidad. 

   Lo suyo sería darle un buen uso y revisar los resultados con nuestras capacidades técnicas. 

2. Especializarse en las tareas que solo podamos hacer nosotros Aunque la IA genera código nosotros debemos: 
- Diseñar la experiencia para el usuario 
- Decidirnos qué arquitectura vamos a utilizar 
- Mantener el enfoque del proyecto 
- Detectar los errores que la IA no es capaz de ver 
3. Aprender a iterar rápido 

   Cómo Lavoble destaca por velocidad, nosotros tenemos que hacer muchos prototipos, comprobar ideas constantemente y realizar estos procedimientos mucho más rápidos que no nos supongan una carga grande.![ref1]

4. Desarrollar habilidades de supervisión técnica ![ref1]

   Debemos de asegurarnos de la calidad del código, corregir errores, evaluar la seguridad. 
### Nuestro rol cambia de crear código a garantizar que todo va a funcionar bien. <a name="_page15_x60.00_y150.30"></a>Caso de fracaso  Builder.ai 
La empresa se publicita como la solución para desarrollar web de manera rápida con IA. 

¿Qué promete? 

Aceleración del desarrollo de aplicaciones y webs. 

Lo que prometía era muy parecido al anterior caso crear webs a través de un asistente de IA llamado “Natasha” por texto, sin tener que codificar manualmente. 

A parte 

Atrajo la atención de muchas personas como empresas, emprendedores, con la promesa de que tenían semi-automatización con la IA. 

Su eslogan era “Tan fácil como pedir una pizza” 

¿Qué problemas empezaron a tener para que llegara al fracaso? 

Detectaron que a falta de recursos mintieron con los ingresos de 2024 que tenían los habían inflado  

Acusaban que la IA Natasha no generaba el código automático, sino que habían 700 ingenieros de la India que realizaban código manualmente. 

A partir de estás cosas se endeudaron y más de 1000 empleados se despidieron a causa de que la empresa colapsó. 

Factores que llevaron la empresa al fracaso 

1. Demasiadas promesas: 

   Prometió una IA que lo iba a realizar absolutamente todo cuando había muchas personas por atrás. 

2. No Transparencia 

   Engañan descaradamente a los clientes e inversores con que la gran parte del desarrollo la generaban ingenieros. 

3. Mala gestión  

   Inflaron los ingresos y eso no es sostenible por lo que les generó el no poder conseguir el suficiente dinero para seguir. ![ref1]

4. Problemas de producto  

   Los clientes se quejaban de que las webs estaban incompletas y tenían bugs, no se escalaban bien y no cumplían lo prometido. 

5. Depender excesivamente del marketing de la IA. 

   Se apoyaron tanto en la idea de “IA mágica” más que en enfocarse en el servicio que daban. 
7. ## Predicciones<a name="_page16_x60.00_y231.90"></a> y escenarios futuros 
### <a name="_page16_x60.00_y262.30"></a>2‑3 años
Más o menos la IA se volverá parte del desarrollo web generando prototipos en minutos, testeando automáticamente, personalizando lo que se le pide de forma rápida y despliegues más rápidos 
### <a name="_page16_x60.00_y355.10"></a> 5‑10 años
### Las IA podrán generar una pag con las especificaciones exactas que le des sin la <a name="_page16_x60.00_y402.30"></a>necesidad de que algún humano introduzca código. 
Las plataformas se reconfiguraron solas analizando el tráfico y el comportamiento de los usuarios(ej el usuario la abre desde un dispositivo móvil se adapta a sus características sin tocar nada). 

En vez de escribir cosas como formularios, encuestas que tardan tiempo se harían por voz. 

Y las IA estarían interconectadas.
### <a name="_page16_x60.00_y508.30"></a>Escenarios alternativos 
- Optimista: Los desarrolladores son capaces de aprender más, la IA los libera de tareas repetitivas y se centrarán en creatividad, experiencia y estrategia. 
- Realista: Aunque la IA sirva mucho no se puede dejar de supervisar, realizará muchas tareas de los programadores y algunos roles cambian o desaparecen y se verá más reclamado supervisar código. 
- Pesimista: Se automatizará lo suficiente como para valerse por sí misma y si los profesionales no se adaptan se quedarán atrás ya que este mismo trabajo de revisar código lo realizará otra IA. 
### <a name="_page16_x60.00_y720.30"></a>Recomendaciones para profesionales 
- Aprender IA básica, herramientas de IA para desarrollo web. ![ref1]
- Mantenerse actualizado en frameworks, arquitectura y en cómo la IA se integra. 
- Desarrollar habilidades de supervisión, diseño de experiencia, ética, pensamiento crítico. 
- Adoptar mentalidad de aprendizaje permanente y adaptabilidad. 
8. ## Conclusiones<a name="_page17_x60.00_y198.30"></a> y reflexión personal 
La IA está avanzando a niveles más rápidos que los de los desarrolladores de páginas web y nos van a cambiar el trabajo y nos vamos a tener que adaptar a ésto. 

La IA desde mi punto de vista la veo como un arma de doble filo muy fuerte ya que si no sabes usarla te puedes hacer mucho daño. 

Ya sabiendo ésto el tema de que las utilicen de manera quitándole el trabajo a los desarrolladores para depender de estás me molesta mucho, pues puede que nos den tantas ventajas perfección etc, pero al fin de alcabo nos están dejando solo con la parte que no nos pueden copiar por ahora la creatividad y maneras de pensar diferentes. 

Lo malo es que la mayoría de las empresas y personas se están acostumbrando a que la IA lo resuelve todo y les da igual la creatividad de las personas que trabajan para ello solo quieren dinero y nos obligan a servir solo de analizadores de código para la IA. 

Estoy generalizando que no todas son así (Pero parece que no muy lejos va a  ser así). 
9. ## Referencias<a name="_page17_x60.00_y461.50"></a> bibliográficas 
- [https://about.gitlab.com/blog/how-devops-and-gitlab-cicd-enhance-a-frontend-workf low/?utm_source=chatgpt.com](https://about.gitlab.com/blog/how-devops-and-gitlab-cicd-enhance-a-frontend-workflow/?utm_source=chatgpt.com) 
- [https://aws.amazon.com/es/blogs/compute/serverless-generative-ai-architectural-p atterns/?utm](https://aws.amazon.com/es/blogs/compute/serverless-generative-ai-architectural-patterns/?utm_source=chatgpt.com)   
- [https://medium.com/@anthony_mccann/building-ai-apis-7-backend-architecture-tip s-for-scalable-ai-solutions-c2fa2d922676](https://medium.com/@anthony_mccann/building-ai-apis-7-backend-architecture-tips-for-scalable-ai-solutions-c2fa2d922676)  
- [https://artificialintelligencejobs.co.uk/career-advice/building-the-ultimate-ai-skill-set-t echnical-and-soft-skills-employers-want-in-2025](https://artificialintelligencejobs.co.uk/career-advice/building-the-ultimate-ai-skill-set-technical-and-soft-skills-employers-want-in-2025)  
- [https://ejfin.com/the-role-of-strategy-in-driving-ai-ml-project-success-and-avoiding-f ailure/](https://ejfin.com/the-role-of-strategy-in-driving-ai-ml-project-success-and-avoiding-failure/)  
- [https://artificialintelligencejobs.co.uk/career-advice/building-the-ultimate-ai-skill-set-t echnical-and-soft-skills-employers-want-in-2025?utm_source=chatgpt.com](https://artificialintelligencejobs.co.uk/career-advice/building-the-ultimate-ai-skill-set-technical-and-soft-skills-employers-want-in-2025?utm_source=chatgpt.com)  
- [https://github.blog/ai-and-ml/the-developer-role-is-evolving-heres-how-to-stay-ahea d/?utm_source](https://github.blog/ai-and-ml/the-developer-role-is-evolving-heres-how-to-stay-ahead/?utm_source=chatgpt.com) 
- [https://www.arunangshudas.com/blog/8-trends-in-backend-development-you-cant-i gnore-in-2025/?](https://www.arunangshudas.com/blog/8-trends-in-backend-development-you-cant-ignore-in-2025/?utm_source=chatgpt.com) 
- [https://arxiv.org/abs/2502.11844?](https://arxiv.org/abs/2502.11844?utm_source=chatgpt.com) 
Página: 14 

[ref1]: Aspose.Words.ca099ab9-6a1f-471a-aca1-349b5f5f34fb.003.png
