import smtplib
from email.mime.text import MIMEText
import imaplib
import ssl

def setup_smtp_server(smtp_port=465): ## se usa este puerto cuando vamos a enviar correos
    try:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="certificado.pem", keyfile="clave.pem")
        server = smtplib.SMTP_SSL('smtp.gmail.com', smtp_port, context=context)
        server.login('user@example.com', 'password') # ingresa el correo yc contraseña desde donde enviarias un e-mail
        return server
    except Exception as e:
        print("Error en la conexión SMTP:", e)
        return None

def send_email(server):
    try:
        msg = MIMEText("Este es un correo electrónico automático de prueba.")
        msg['Subject'] = "Correo electrónico automático"
        msg['From'] = 'user@example.com' # ingresa el correo desde donde enviarias un e-mail
        msg['To'] = 'recipient@example.com' # ingresa el correo de destino
        server.send_message(msg)
        print("Correo electrónico enviado")
    except Exception as e:
        print("Error al enviar el correo:", e)
    finally:
        if server:
            server.quit()

def setup_imap_server(imap_port=993):
    try:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="certificado.pem", keyfile="clave.pem")
        mail = imaplib.IMAP4_SSL('imap.gmail.com', imap_port, context=context)
        mail.login('user@example.com', 'password') # ingresa el correo yc contraseña desde donde enviarias un e-mail
        return mail
    except Exception as e:
        print("Error en la conexión IMAP:", e)
        return None

def fetch_emails(mail, folder='inbox'):
    try:
        mail.select(folder)
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        print(raw_email.decode('utf-8'))
    except Exception as e:
        print("Error al recuperar correos electrónicos:", e)
    finally:
        if mail:
            mail.logout()

smtp_server = setup_smtp_server()
if smtp_server:
    send_email(smtp_server)
    smtp_server.quit()
    print("Correo electrónico automático enviado")
