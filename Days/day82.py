'''Jogo da Velha'''

import random
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    # Verifica linhas, colunas e diagonais
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            row, col = map(int, input(f"Jogador {current_player}, escolha sua jogada (linha e coluna): ").split())
        else:
            row, col = random.randint(0, 2), random.randint(0, 2)
            while board[row][col] != " ":
                row, col = random.randint(0, 2), random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Jogador {current_player} venceu!")
                break
            if is_board_full(board):
                print_board(board)
                print("Empate!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Jogada inválida. Tente novamente.")
            
def main():
    print("Bem-vindo ao Jogo da Velha!")
    play_game()
    
if __name__ == "__main__":
    main()