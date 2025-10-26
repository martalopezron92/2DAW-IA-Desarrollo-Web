# Guía de Contribución

¡Gracias por tu interés en contribuir al curso "Inteligencia Artificial aplicada al Desarrollo Web"! 

## 🎯 Tipos de contribuciones bienvenidas

### 📚 Contenido educativo
- Mejoras en explicaciones teóricas
- Ejercicios adicionales
- Ejemplos prácticos
- Correcciones de errores
- Traducciones

### 💻 Código y datasets
- Optimización de scripts Python
- Nuevos datasets de ejemplo
- Mejoras en notebooks Jupyter
- Scripts de automatización

### 📖 Documentación
- Correcciones ortográficas y gramaticales
- Mejoras en la estructura
- Añadir enlaces útiles
- Aclaraciones en las instrucciones

## 🔄 Proceso de contribución

### 1. Preparación
1. Haz un **fork** del repositorio
2. Clona tu fork localmente:
   ```bash
   git clone https://github.com/tu-usuario/2daw-ia-desarrollo-web.git
   ```
3. Crea una rama para tu contribución:
   ```bash
   git checkout -b feature/descripcion-mejora
   ```

### 2. Desarrollo
1. Realiza los cambios siguiendo las **convenciones establecidas**
2. Asegúrate de que el contenido es **pedagógicamente coherente**
3. Verifica que todos los **enlaces relativos funcionen**
4. Ejecuta las pruebas si aplica

### 3. Documentación
- Si añades nuevas unidades, incluye su rúbrica correspondiente
- Si modificas prácticas, actualiza las soluciones del profesor
- Mantén actualizada la documentación relacionada

### 4. Envío
1. Confirma tus cambios:
   ```bash
   git add .
   git commit -m "feat: descripción clara de los cambios"
   ```
2. Sube los cambios a tu fork:
   ```bash
   git push origin feature/descripcion-mejora
   ```
3. Crea un **Pull Request** explicando:
   - Qué cambios realizas
   - Por qué son necesarios
   - Cómo benefician al curso

## 📋 Estándares de calidad

### Contenido educativo
- **Claridad**: Explicaciones comprensibles para estudiantes de 2º DAW
- **Progresión**: Respeta la secuencia de aprendizaje establecida
- **Practicidad**: Enfoque hacia aplicaciones reales
- **Inclusividad**: Considera diferentes estilos de aprendizaje

### Código
- **Python**: Sigue PEP 8
- **Comentarios**: En español, claros y útiles
- **Documentación**: Docstrings descriptivos
- **Funcionalidad**: Código probado y funcional

### Markdown
- **Estructura**: Usa encabezados jerárquicos correctos
- **Enlaces**: Verifica que todos los enlaces internos funcionen
- **Formato**: Mantén consistencia con el estilo existente
- **Imágenes**: Usa rutas relativas y texto alternativo

## 🎨 Convenciones de estilo

### Nombres de archivos
- **Unidades**: `U##_Nombre_Descriptivo.md`
- **Prácticas**: `P##_nombre_descriptivo.md`
- **Rúbricas**: `R##_B#_U##.md`
- **Soluciones**: `S##_nombre_descriptivo.md`

### Estructura de contenido

#### Unidades didácticas
```markdown
# U## - Título de la Unidad

## 🎯 Objetivos de aprendizaje
## ⏱️ Duración estimada
## 📚 Contenidos
## 🔍 Ejemplos prácticos
## 💡 Mini-ejercicios
## 📝 Quiz de autoevaluación
## 🔗 Recursos adicionales
## ➡️ Siguiente unidad
```

#### Prácticas
```markdown
# P## - Título de la Práctica

## 🎯 Objetivos
## ⏱️ Duración estimada
## 📋 Prerrequisitos
## 🛠️ Materiales necesarios
## 📝 Enunciado
## 🔍 Pasos detallados
## 📤 Entregables
## 📊 Evaluación
## 💡 Pistas y ayuda
```

### Convenciones de commits
Usa el formato [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nueva funcionalidad o contenido
- `fix:` Corrección de errores
- `docs:` Cambios en documentación
- `style:` Formato, espacios, etc.
- `refactor:` Reestructuración de código
- `test:` Añadir o modificar tests
- `chore:` Tareas de mantenimiento

Ejemplos:
```
feat: añadir ejercicios prácticos a U4b Siuba
fix: corregir enlaces rotos en README
docs: mejorar explicación de redes neuronales
style: formatear código Python en P07
```

## 🧪 Testing y validación

Antes de enviar tu PR:

1. **Markdown lint**: Verifica que pasa el workflow de validación
2. **Enlaces**: Comprueba que todos los enlaces internos funcionan
3. **Código**: Ejecuta y verifica que el código Python funciona
4. **Coherencia**: Revisa que el contenido encaja con el resto del curso

## 🤝 Código de conducta

### Comportamiento esperado
- Ser respetuoso y constructivo
- Aceptar críticas constructivas
- Colaborar de forma positiva
- Centrarse en el beneficio educativo

### Comportamiento inaceptable
- Comentarios despectivos o discriminatorios
- Spam o contenido irrelevante
- Violación de derechos de autor
- Promoción comercial no autorizada

## 📞 Comunicación

### Issues
- Usa las plantillas proporcionadas
- Sé específico en las descripciones
- Añade etiquetas apropiadas
- Proporciona pasos para reproducir errores

### Pull Requests
- Describe claramente los cambios
- Referencia issues relacionados
- Mantén el PR enfocado en un tema
- Responde a comentarios de revisión

### Discusiones
- Usa GitHub Discussions para:
  - Propuestas de mejora
  - Dudas sobre el curso
  - Compartir recursos adicionales
  - Feedback general

## 🏆 Reconocimiento

Los contribuidores serán reconocidos en:
- Lista de colaboradores en README
- Sección "Agradecimientos" en la documentación
- Issues y PRs como referencia

## 📋 Checklist para contribuidores

Antes de enviar tu PR, verifica:

- [ ] El contenido sigue las convenciones establecidas
- [ ] Los enlaces internos funcionan correctamente
- [ ] El código Python ejecuta sin errores
- [ ] La documentación está actualizada
- [ ] Los commits siguen el formato convencional
- [ ] El PR tiene una descripción clara
- [ ] Se han ejecutado las pruebas pertinentes

## 🆘 ¿Necesitas ayuda?

- 📧 **Email**: profesor@ejemplo.edu
- 💬 **Discussions**: Usa GitHub Discussions
- 📝 **Issues**: Para reportar problemas específicos
- 📚 **Wiki**: Consulta la documentación adicional

¡Gracias por ayudar a mejorar este curso! 🚀