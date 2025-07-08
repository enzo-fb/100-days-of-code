"""Automatizar e-mails"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_email(destinatario, assunto, mensagem):
    remetente = "meu_email@gmail.com"  # Substitua pelo seu e-mail do Gmail
    senha = "1234567890"  # Substitua pela sua senha de aplicativo do Gmail

    # Configurar o servidor SMTP
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(remetente, senha)

    # Criar a mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(mensagem, "plain"))

    # Enviar o e-mail
    servidor.send_message(msg)
    servidor.quit()


def main():
    destinatario = input("Digite o e-mail do destinatário: ")
    assunto = input("Digite o assunto do e-mail: ")
    mensagem = input("Digite a mensagem do e-mail: ")

    enviar_email(destinatario, assunto, mensagem)
    print("E-mail enviado com sucesso!")


if __name__ == "__main__":
    main()
