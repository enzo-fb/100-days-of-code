'''
verificar se uma determinada string é um palíndromo.
'''

def verificaPalindromo(palavra):
    x = str(palavra[::-1]) #inverte a palavra
    if x == palavra:
        return True
    return False
   
    
x = str(input("Digite uma palavra: "))    
print(verificaPalindromo(x))