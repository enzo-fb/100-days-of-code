"""Concorrência e Paralelismo"""

import threading
import multiprocessing
import time


def tarefa(nome, n):
    for i in range(n):
        print(f"{nome}: {i+1}")
        time.sleep(0.5)


def exemplo_threading():
    print("\n--- Exemplo com threading (concorrência) ---")
    t1 = threading.Thread(target=tarefa, args=("Thread 1", 5))
    t2 = threading.Thread(target=tarefa, args=("Thread 2", 5))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def exemplo_multiprocessing():
    print("\n--- Exemplo com multiprocessing (paralelismo) ---")
    p1 = multiprocessing.Process(target=tarefa, args=("Processo 1", 5))
    p2 = multiprocessing.Process(target=tarefa, args=("Processo 2", 5))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def main():
    exemplo_threading()
    exemplo_multiprocessing()


if __name__ == "__main__":
    main()
