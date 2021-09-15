from email.mime import text
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from os import environ
from dotenv import load_dotenv
load_dotenv()

mensaje = MIMEMultipart()
mensaje['From'] = environ.get('EMAIL')
mensaje['Subject'] = 'Solicitud de restauracion de la contrasenia'
password = environ.get('EMAIL_PASSWORD')

def enviarCorreo(destinatario,cuerpo):
    '''Funcion para enviar correo'''
    mensaje['To'] = destinatario
    texto = mensaje

    # Luego de definir el cuerpo del correo agregamos al mensaje mediante su metodo attach y en formato MIMEText en el cual recibira un texto y luego el format a convertir, si quieres enviar un html entonces pondremos en 'html', si queremos enviar un texto 'plain
    mensaje.attach(MIMEText(cuerpo, 'html'))

    try:

        servidorSMTP = smtplib.SMTP('smtp.gmail.com',587)

        servidorSMTP.starttls()

        servidorSMTP.login(user=mensaje.get('From'), password=password)
        servidorSMTP.sendmail(
            from_addr=mensaje.get('From'),
            to_addrs=mensaje.get('To'),
            msg=mensaje.as_string()
        )
        servidorSMTP.quit()
    except Exception as e:
        print(e)