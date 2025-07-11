'''Agendador de tarefas'''

import schedule
import time

def minha_tarefa():
    print("Executando tarefa agendada!")

def main():
    # Agenda a tarefa para rodar a cada 5 segundos
    schedule.every(5).seconds.do(minha_tarefa)

    print("Agendador iniciado. Pressione Ctrl+C para sair.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

