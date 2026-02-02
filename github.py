import smtplib
import os
from email.message import EmailMessage

# ==============================
# CONFIGURACIÓN (Variables de entorno)
# ==============================
# Antes de ejecutar:
# export EMAIL_USER="tu_correo@gmail.com"
# export EMAIL_PASSWORD="tu_contraseña_o_app_password"

my_email = os.environ.get("EMAIL_USER")
my_password = os.environ.get("EMAIL_PASSWORD")

if not my_email or not my_password:
    raise ValueError("Faltan las variables de entorno EMAIL_USER o EMAIL_PASSWORD")

# ==============================
# PRUEBA DE CONEXIÓN
# ==============================
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(my_email, my_password)
    print("Conexión exitosa con el servidor SMTP")
    server.quit()
except Exception as error:
    print("Error de conexión:", error)

# ==============================
# ENVÍO MASIVO DE CORREOS
# ==============================
email_masivo = [
    "usuario1@example.com",
    "usuario2@example.com",
    "usuario3@example.com"
]

imagenes = [
    "imagen1.jpg",
    "imagen2.jpg"
]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(my_email, my_password)

for destinatario in email_masivo:
    print(f"Enviando correo a: {destinatario}")

    msg = EmailMessage()
    msg['Subject'] = "Prueba de envío de imágenes con Python"
    msg['From'] = my_email
    msg['To'] = destinatario

    mensaje_html = """
    <html>
        <body>
            <h2 style="color: red;">Hola 👋</h2>
            <p>Este es un correo de prueba enviado desde Python.</p>
            <p>Se adjuntan algunas imágenes.</p>
        </body>
    </html>
    """
    msg.add_alternative(mensaje_html, subtype='html')

    for imagen in imagenes:
        try:
            with open(imagen, 'rb') as archivo:
                data = archivo.read()
                msg.add_attachment(
                    data,
                    maintype='image',
                    subtype='jpeg',
                    filename=imagen
                )
        except FileNotFoundError:
            print(f"Archivo no encontrado: {imagen}")

    try:
        server.send_message(msg)
        print("Correo enviado correctamente")
    except Exception as error:
        print("Error al enviar correo:", error)

server.quit()
print("Proceso de envío finalizado.")
