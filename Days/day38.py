"""Exceção personalizada"""


class MensagemInvalida(Exception):
    def __init__(self, mensagem="Mensagem inserida inválida!") -> None:
        super().__init__(mensagem)


def enviar_mensagem(msg):
    if not msg or len(msg.strip()) == 0:
        raise MensagemInvalida()
    if len(msg) > 200:
        raise MensagemInvalida("Mensagem muito longa! Máximo de 200 caracteres.")
    print("Mensagem enviada:", msg)


#
try:
    enviar_mensagem("   ")
except MensagemInvalida as e:
    print(e)
