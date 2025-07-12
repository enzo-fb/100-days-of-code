'''Ferramenta de linha de comando '''

import argparse

def main():
    parser = argparse.ArgumentParser(description="Exemplo de ferramenta de linha de comando")
    parser.add_argument('--opcao', choices=['a', 'b', 'c'], help='Escolha uma opção: a, b ou c')
    args = parser.parse_args()

    if args.opcao == 'a':
        print("Você escolheu a opção A")
    elif args.opcao == 'b':
        print("Você escolheu a opção B")
    elif args.opcao == 'c':
        print("Você escolheu a opção C")
    else:
        print("Nenhuma opção escolhida.")

if __name__ == "__main__":
    main()
