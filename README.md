# Portafolio de Jesús Carreño

Portafolio personal construido con Django. La página sirve la plantilla desde Django, y WhiteNoise publica el currículum y los demás archivos estáticos en producción.

## Ejecutar localmente en Windows

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:DEBUG = "True"
.\.venv\Scripts\python.exe manage.py runserver
```

Abre `http://127.0.0.1:8000/`. Para ejecutar las pruebas:

```powershell
$env:DEBUG = "True"
.\.venv\Scripts\python.exe manage.py test
```

## Publicar en Render

El archivo `render.yaml` define el servicio web, la compilación de archivos estáticos y la ruta de comprobación de salud. Sube el repositorio a GitHub, crea un Blueprint en Render conectado al repositorio y confirma el servicio descrito por `render.yaml`. Render genera `SECRET_KEY` automáticamente; `DEBUG` queda desactivado en producción.

La ruta `/health/` debe responder `ok` cuando la publicación esté lista. El servicio no requiere base de datos.

## Contacto

Los botones de WhatsApp abren una conversación con el número público configurado en la plantilla. El CV se encuentra en `assets/sintesis_curricular.pdf`.
