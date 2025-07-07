'''Baixar arquivos'''

import os
import requests

def baixar_arquivos(urls, diretorio):

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    for url in urls:
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
            nome_arquivo = os.path.join(diretorio, url.split('/')[-1])
            with open(nome_arquivo, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print(f'Arquivo baixado: {nome_arquivo}')
        except requests.RequestException as e:
            print(f'Erro ao baixar {url}: {e}')