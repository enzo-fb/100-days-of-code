'''Script de Automação'''
import os

def renomear_arquivos(diretorio, padrao_novo_nome):
    """
    Renomeia todos os arquivos no diretório especificado seguindo o padrão informado.
    O padrão pode conter {i} para o índice do arquivo.
    """
    arquivos = sorted(os.listdir(diretorio))
    for i, nome_antigo in enumerate(arquivos, 1):
        caminho_antigo = os.path.join(diretorio, nome_antigo)
        if os.path.isfile(caminho_antigo):
            extensao = os.path.splitext(nome_antigo)[1]
            novo_nome = padrao_novo_nome.format(i=i) + extensao
            caminho_novo = os.path.join(diretorio, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {nome_antigo} -> {novo_nome}')

if __name__ == "__main__":
    diretorio = input("Informe o diretório dos arquivos: ").strip()
    padrao = input("Informe o padrão do novo nome (use {i} para o número sequencial): ").strip()
    renomear_arquivos(diretorio, padrao)
