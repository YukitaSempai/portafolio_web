# Portafolio de Jesús Carreño

Portafolio personal estático, creado con HTML, CSS y JavaScript. Se publica en GitHub Pages desde la rama `main`; no necesita servidor, base de datos ni dependencias de Python.

## Desarrollo local

Abre `index.html` en un navegador o inicia un servidor estático local:

```powershell
py -m http.server 8000
```

Visita `http://localhost:8000`. El currículum está en `assets/sintesis_curricular.pdf`.

## Publicación

1. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** como fuente de publicación.
2. Cada cambio enviado a `main` ejecutará el flujo de [publicación](./.github/workflows/pages.yml).
3. Al finalizar el flujo, el portafolio estará disponible en <https://yukitasempai.github.io/portafolio_web/>.

Para una versión nueva, modifica `index.html` o los archivos de `assets/`, revisa el resultado localmente y envía los cambios a `main`. El flujo publicará automáticamente la versión actualizada.

## Proyectos destacados

El carrusel vive en la sección `#projects` de `index.html`. Cada tarjeta contiene una demo, una descripción, funcionalidades, tecnologías y enlaces al código fuente. Para añadir un proyecto, duplica un elemento `.project-card`, actualiza su demo y enlaces, y añade su indicador `.project-dot`. Mantén `projectStatus` y `aria-label` de las diapositivas sincronizados con el número de proyectos.

Las demos se cargan de forma diferida en iframes aislados. Usa solo sitios autorizados para publicación e inserción; si una demo deja de estar disponible, actualiza su enlace o sustitúyela por una vista estática claramente identificada, sin presentarla como funcional.

- [Nanas Design — código](https://github.com/YukitaSempai/nanas-design) · [demo](https://nanas-design.pages.dev/)
- [MYGV — código](https://github.com/YukitaSempai/mygv) · [demo](https://yukitasempai.github.io/mygv/)

## Contacto

Los enlaces de WhatsApp abren una conversación con el número público configurado en la página. Actualiza ese número en `index.html` si cambia.
