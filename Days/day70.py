'''Computação Numérica '''
import numpy as np

lista = [1, -2, -3, 4, 5]
array = np.array(lista)

x = np.linspace(0, 10, 100)
y = np.sin(x)
dy_dx = np.gradient(y, x)  # Derivada numérica de y em relação a x

print(dy_dx)
print(array)
print(np.abs(array))  
print(dy_dx)