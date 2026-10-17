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

El carrusel vive en la sección `#projects` de `index.html`. Cada tarjeta contiene una vista previa, una descripción, funcionalidades, tecnologías y, cuando el código está publicado, un enlace al repositorio. Para añadir un proyecto, duplica un elemento `.project-card`, actualiza su demo y enlaces, y añade su indicador `.project-dot`. Mantén el nombre accesible de cada diapositiva y los indicadores sincronizados.

Las vistas locales se cargan de forma diferida en iframes aislados. SAGEM y SIPROT son prototipos autónomos que solo usan registros ficticios en memoria, sin conexión a servicios ni almacenamiento. MYGV cuenta con una demo en línea y una miniatura local ilustrativa para mantener el aislamiento del iframe; el enlace de la tarjeta abre la aplicación publicada. No copies datos reales, capturas, documentos ni credenciales de repositorios privados a las demos. Si una demo deja de estar disponible, actualiza su enlace o sustitúyela por una vista estática claramente identificada, sin presentarla como funcional.

- [Nanas Design — código](https://github.com/YukitaSempai/nanas-design) · [demo](https://nanas-design.pages.dev/)
- [MYGV — código](https://github.com/YukitaSempai/mygv) · [demo](https://yukitasempai.github.io/mygv/) · [vista previa local](./demos/mygv-preview.html)
- SAGEM — [demo visual local](./demos/sagem-preview.html); el repositorio permanece privado.
- SIPROT — [demo visual local](./demos/siprot-preview.html); el repositorio permanece privado.

## Contacto

Los enlaces de WhatsApp abren una conversación con el número público configurado en la página. Actualiza ese número en `index.html` si cambia.
