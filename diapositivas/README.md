# Presentación HTML desde Markdown: Modelos supervisados

Proyecto completo para generar una presentación de diapositivas en HTML, orientada a alumnado de DAW, a partir de un único archivo Markdown (`slides.md`) usando **Marp**.

## 1) Descripción del proyecto

Este proyecto incluye:

- Contenido docente en español sobre **clasificación y regresión**.
- Estilo visual personalizado (tema CSS).
- Diagramas y dibujos en SVG inline (sin dependencias frágiles).
- Automatización con **GitHub Actions** para compilar HTML en cada push a `main`.
- Opción de publicación en **GitHub Pages**.

## 2) Estructura de carpetas

```text
proyecto-slides-supervisados/
├─ README.md
├─ slides.md
├─ package.json
├─ marp.config.js
├─ .gitignore
├─ theme/
│  └─ custom.css
├─ assets/
│  ├─ diagrams/
│  │  └─ .gitkeep
│  └─ images/
│     └─ .gitkeep
└─ .github/
   └─ workflows/
      └─ build-slides.yml
```

## 3) Requisitos previos

- Node.js 18+ (recomendado 20 LTS)
- npm 9+
- Git (si vas a usar CI/CD y Pages)

## 4) Instalación

Desde la carpeta del proyecto:

```bash
npm install
```

## 5) Cómo lanzar en local

Modo desarrollo con recarga:

```bash
npm run dev
```

Marp abrirá un servidor local para previsualizar las diapositivas.

## 6) Cómo generar la presentación HTML

Compilación a HTML estático:

```bash
npm run build
```

Salida generada:

- `dist/index.html`

Opcional: exportación a PDF

```bash
npm run build:pdf
```

Salida PDF:

- `dist/slides.pdf`

## 7) Cómo se ejecuta GitHub Actions

El workflow `build-slides.yml` se ejecuta al hacer `push` a `main` (y también manualmente con `workflow_dispatch`).

Pasos automáticos:

1. Checkout del repositorio
2. Instalación de Node
3. `npm install`
4. `npm run build`
5. Publicación del artefacto `slides-html` con el contenido de `dist/`

## 8) Cómo publicar en GitHub Pages

La publicación está preparada como opcional en el workflow mediante una variable de repositorio:

- Variable: `ENABLE_PAGES`
- Valor: `true`

Pasos:

1. En GitHub: **Settings → Pages**
2. En **Build and deployment**, selecciona **GitHub Actions**
3. En **Settings → Secrets and variables → Actions → Variables**, crea:
   - `ENABLE_PAGES = true`
4. Haz push a `main`
5. El job `deploy-pages` publicará `dist/` en Pages

Si no quieres publicar en Pages, deja `ENABLE_PAGES` sin crear o con otro valor.

## 9) Cómo editar el Markdown para modificar contenidos

Archivo principal:

- `slides.md`

Sugerencias:

- Usa separadores `---` para nueva diapositiva.
- Mantén una idea principal por slide.
- Prefiere listas breves, tablas y bloques visuales.
- Para resaltar, usa etiquetas de CSS definidas en `theme/custom.css`.

## 10) Cómo añadir nuevas diapositivas, gráficos o ejemplos

### Nueva diapositiva

Añade al final de `slides.md`:

```markdown
---
# Título de la nueva diapositiva

- Punto clave 1
- Punto clave 2
```

### Nuevo gráfico/dibujo

Opciones recomendadas:

- SVG inline dentro de `slides.md` (más robusto para exportar).
- Imagen local en `assets/images/` y referencia relativa.

### Nuevo ejemplo numérico

Incluye una tabla simple con datos de entrada/salida:

```markdown
| Feature 1 | Feature 2 | y |
|---:|---:|---|
| 10 | 2 | clase A |
| 15 | 5 | clase B |
```

## Comandos útiles

```bash
npm run dev       # previsualización local
npm run build     # exportar a HTML
npm run build:pdf # exportar a PDF
```

---

Material pensado para uso docente en DAW: visual, riguroso y fácil de mantener.
