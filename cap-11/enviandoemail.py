import os
import smtplib
from email.message import EmailMessage
from segredo import senha  # importanto a minha senha de um arquivo segredo.py
# configurando email de envio

EMAIL_ADRESS =  # o email de quem enviara o email
EMAIL_PASSWORD = senha

# criando um email

msg = EmailMessage()
msg['Subject'] = 'Enviando o meu primeiro email via código em python'
msg['From'] =  # o email de quem enviara o email
msg['To'] =  # definindo o destinatario
msg.set_content('Se você recebeu este email, é por que o código funcionou')

# Enviando um email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
