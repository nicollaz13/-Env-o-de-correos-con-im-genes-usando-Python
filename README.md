# -Env-o-de-correos-con-im-genes-usando-Python
Script en Python para enviar correos electrónicos de forma segura usando SMTP. Permite envío masivo, contenido HTML y adjuntar imágenes. Las credenciales se gestionan con variables de entorno, evitando datos sensibles en el código. Ideal como ejemplo educativo o base para automatizar notificaciones por email en proyectos reales simples!!

## Configuración

Este proyecto utiliza variables de entorno para proteger credenciales.

Ejemplo en Linux / macOS:
export EMAIL_USER="correo@gmail.com"
export EMAIL_PASSWORD="app_password"

En Windows (PowerShell):
setx EMAIL_USER "correo@gmail.com"
setx EMAIL_PASSWORD "app_password"
