"""Aplicativo de bate-papo"""

import socket
import threading


def receber_mensagens(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print("\nRecebido:", msg)
        except:
            break


def cliente():
    host = input("Digite o IP do servidor (ex: 127.0.0.1): ")
    porta = int(input("Digite a porta do servidor (ex: 5000): "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, porta))
    print("Conectado ao servidor de bate-papo!")
    threading.Thread(target=receber_mensagens, args=(sock,), daemon=True).start()
    try:
        while True:
            msg = input()
            if msg.lower() == "sair":
                break
            sock.send(msg.encode())
    finally:
        sock.close()


def servidor():
    host = "0.0.0.0"
    porta = int(input("Digite a porta para escutar (ex: 5000): "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, porta))
    sock.listen(1)
    print("Aguardando conexão...")
    conn, addr = sock.accept()
    print(f"Cliente conectado: {addr}")
    threading.Thread(target=receber_mensagens, args=(conn,), daemon=True).start()
    try:
        while True:
            msg = input()
            if msg.lower() == "sair":
                break
            conn.send(msg.encode())
    finally:
        conn.close()
        sock.close()


def main():
    modo = input("Digite 's' para servidor ou 'c' para cliente: ").strip().lower()
    if modo == "s":
        servidor()
    elif modo == "c":
        cliente()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
