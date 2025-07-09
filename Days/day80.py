'''Web Scraping'''

import requests
from bs4 import BeautifulSoup

def extrair_titulos(url):
    resposta = requests.get(url)
    if resposta.status_code != 200:
        print("Erro ao acessar o site.")
        return []
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    # Exemplo: extrair títulos de notícias de um site de notícias
    titulos = [h2.get_text(strip=True) for h2 in sopa.find_all('h2')]
    return titulos

def main():
    url = input("Digite a URL do site para extrair os títulos: ")
    titulos = extrair_titulos(url)
    if titulos:
        print("\nTítulos encontrados:")
        for t in titulos:
            print("-", t)
    else:
        print("Nenhum título encontrado.")

if __name__ == "__main__":
    main()

