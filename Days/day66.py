"""Chamada de API externa"""

import requests


def buscar_dados_api(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx
        return resposta.json()
    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return {"erro": str(e)}


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    dados = buscar_dados_api(url)
    print(dados)

    # Exemplo de uso com uma API que retorna dados de usuários
    url_usuarios = "https://jsonplaceholder.typicode.com/users"
    usuarios = buscar_dados_api(url_usuarios)
    print(usuarios)
