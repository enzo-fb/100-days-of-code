"""Módulos da biblioteca padrão do Python"""

import datetime
import itertools
import functools
import time
import os


def hora_atual():
    return datetime.datetime.now().strftime("%H:%M:%S")


def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("Tempo esgotado!")


def junta_lista(lt1, lt2):
    return itertools.chain(lt1, lt2)


def soma_lista(lt):
    return functools.reduce(lambda y, z: y + z, lt)


print(soma_lista([1, 2, 3, 4, 5]))
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(hora_atual())
    time.sleep(1)
