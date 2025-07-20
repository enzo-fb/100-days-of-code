"""Ciência de Dados - Limpeza e Engenharia de Dados"""

import pandas as pd
import numpy as np


def main():
    # Exemplo: Criar um DataFrame com dados faltantes e duplicados
    dados = {
        "nome": ["Ana", "Bruno", "Carlos", "Ana", np.nan],
        "idade": [23, 35, np.nan, 23, 40],
        "cidade": ["SP", "RJ", "BH", "SP", "RJ"],
    }
    df = pd.DataFrame(dados)
    print("Dados originais:\n", df)

    # Limpeza de dados
    df = df.drop_duplicates()  # Remove duplicatas
    df = df.dropna()  # Remove linhas com valores faltantes
    print("\nApós limpeza:\n", df)

    # Engenharia de recursos: criar nova coluna
    df["faixa_etaria"] = pd.cut(
        df["idade"], bins=[0, 18, 30, 50], labels=["jovem", "adulto", "maduro"]
    )
    print("\nCom nova coluna (faixa_etaria):\n", df)


if __name__ == "__main__":
    main()
