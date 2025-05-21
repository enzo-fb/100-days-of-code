'''
    Mesclar dois dicionários
'''

def mesclaDicionario(dicion1, dicion2):
    dicionario = dict()
    dicionario = dicion1 | dicion2
    return dicionario
    
d1 = {"teste": 2, "teste2": 3}
d2 = {"testando1": "oi", "testando2": "hello"}

d3 = mesclaDicionario(d1,d2)
print(d3)