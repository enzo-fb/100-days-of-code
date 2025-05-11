'''
Sequência de Fibonacci
'''

def sequenciaFibo(limit):
    if limit == 0:
        return None
    aux = 0
    fibo = [1]
    while aux != limit-1:
        if aux == 0:
            fibo.append(1)
        else:
            fibo.append(fibo[aux]+fibo[aux-1])
        aux += 1
    return fibo
        
limite = int(input("Digite a quantidade de elementos da sequência de Fibonacci: "))
print(sequenciaFibo(limite))