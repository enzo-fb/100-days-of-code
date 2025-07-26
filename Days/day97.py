"""Gerenciamento de Memória e Coleta de Lixo"""

import gc


class Objeto:
    def __del__(self):
        print("Objeto destruído!")


def cria_ciclo():
    a = Objeto()
    b = Objeto()
    a.ref = b
    b.ref = a


cria_ciclo()

print("Coletando lixo...")
coletados = gc.collect()
print(f"Objetos coletados: {coletados}")
