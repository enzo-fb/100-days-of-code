'''
    Lidar com exceções
'''

def dividir(a,b):
    try:
        c = a/b
        return print(F"Divisão de {a} por {b} é {c}.")
    except ZeroDivisionError as erro:
        print(f"Não é possível fazer divisão por zero!\n{erro}")
        
dividir(4,0)