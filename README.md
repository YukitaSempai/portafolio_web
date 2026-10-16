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

## Contacto

Los enlaces de WhatsApp abren una conversación con el número público configurado en la página. Actualiza ese número en `index.html` si cambia.
