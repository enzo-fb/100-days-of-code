"""Rastreador da Web"""

import requests
from bs4 import BeautifulSoup


def rastrear_links(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code != 200:
            print("Erro ao acessar o site.")
            return []
        sopa = BeautifulSoup(resposta.text, "html.parser")
        links = [a["href"] for a in sopa.find_all("a", href=True)]
        return links
    except Exception as e:
        print(f"Erro: {e}")
        return []


def main():
    url = input("Digite a URL para rastrear os links: ")
    links = rastrear_links(url)
    if links:
        print("\nLinks encontrados:")
        for link in links:
            print(link)
    else:
        print("Nenhum link encontrado.")


if __name__ == "__main__":
    main()
