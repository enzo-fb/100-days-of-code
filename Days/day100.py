"""Portfólio"""

# Portfólio de Projetos Python

projetos = [
    {
        "nome": "Pomodoro",
        "descricao": "Aplicativo de gerenciamento de tempo baseado na técnica Pomodoro, desenvolvido com Python e Tkinter.",
        "link": "https://github.com/enzo-fb/Pomodoro",
    },
    {
        "nome": "Frequência de Palavras",
        "descricao": "Contador de palavras em um texto.",
        "link": "https://github.com/enzo-fb/Frequencia-de-Palavras",
    },
    {
        "nome": "App de Controle de Estoque",
        "descricao": "Gerenciador de estoque simples com interface gráfica, permitindo adicionar, remover e listar produtos. Usa SQLite para persistência de dados.",
        "link": "https://github.com/enzo-fb/gerenciador-estoque",
    },
]

for projeto in projetos:
    print(f"Projeto: {projeto['nome']}")
    print(f"Descrição: {projeto['descricao']}")
    print(f"Repositório: {projeto['link']}")
    print()
