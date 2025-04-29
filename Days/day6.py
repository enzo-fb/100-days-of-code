VALOR_X = 15

def greet_user(nome = 'Convidado'):
    return print(f"Olá, {nome}")

def area_triangulo(comp, larg):
    return comp*larg


def set_valor_x_local(x):
        VALOR_X= x
        print(f"Local VALOR_X: {VALOR_X}")

def set_valor_x_global(x):
        global VALOR_X
        VALOR_X = x
        print(f"Global VALOR_X: {VALOR_X}")
