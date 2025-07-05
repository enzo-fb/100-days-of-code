import nltk
import random

# Baixar recursos necessários do NLTK
nltk.download("punkt", quiet=True)

# Lista de pares de perguntas e respostas simples
pairs = {
    "oi": ["Olá!", "Oi, tudo bem?", "Oi! Como posso ajudar?"],
    "olá": ["Olá!", "Oi, tudo bem?", "Oi! Como posso ajudar?"],
    "tudo bem": ["Estou bem, obrigado!", "Tudo ótimo! E você?", "Sim, tudo bem!"],
    "qual seu nome": ["Eu sou um chatbot.", "Me chamo Chatbot!", "Sou apenas um bot."],
    "o que você faz": [
        "Respondo perguntas simples.",
        "Converso com você!",
        "Posso te ajudar com dúvidas simples.",
    ],
    "adeus": ["Tchau!", "Até logo!", "Foi bom conversar com você!"],
}


def responder(mensagem):
    mensagem = mensagem.lower()
    for chave in pairs:
        if chave in mensagem:
            return random.choice(pairs[chave])
    return "Desculpe, não entendi. Pode reformular?"


def main():
    print("Chatbot: Olá! Digite 'adeus' para sair.")
    while True:
        user_input = input("Você: ")
        resposta = responder(user_input)
        print("Chatbot:", resposta)
        if "adeus" in user_input.lower():
            break


if __name__ == "__main__":
    main()
