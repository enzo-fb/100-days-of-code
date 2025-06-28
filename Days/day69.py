"""Análise estática"""

import ast
import astor

codigo = """
def soma(a, b):
    return a + b

x = 10
y = 20
resultado = soma(x, y)
"""


def analisar_codigo(codigo: str) -> None:
    """Analisa o código Python estaticamente."""
    try:
        # Analisa o código em uma AST
        arvore = ast.parse(codigo)

        # Imprime a AST em formato legível
        print(astor.to_source(arvore))

        # Exemplo: Verifica definições de funções
        for no in ast.walk(arvore):
            if isinstance(no, ast.FunctionDef):
                print(f"Função encontrada: {no.name} na linha {no.lineno}")
        # Exemplo: Verifica atribuições de variáveis
        for no in ast.walk(arvore):
            if isinstance(no, ast.Assign):
                print(
                    f"Atribuição encontrada na linha {no.lineno}: {astor.to_source(no)}"
                )

    except SyntaxError as e:
        print(f"Erro de sintaxe no código: {e}")


analisar_codigo(codigo)
