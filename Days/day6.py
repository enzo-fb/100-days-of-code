VALOR_X = 15

def greet_user(nome = 'Convidado'):
    return print(f"Olá, {nome}")

def area_triangulo(comp, larg):
    return comp*larg

def novo_valor(x):
    VALOR_X = x
    print(VALOR_X)

def new_value():
    global VALOR_X
    VALOR_X = 5
print(VALOR_X)
print(novo_valor(10))
print(VALOR_X)
new_value()
print(VALOR_X)
