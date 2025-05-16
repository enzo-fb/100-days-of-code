'''
    Função que verifique se duas strings são anagramas
'''

def verificaAnagrama(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        print("São anagramas!")
    else:
        print("Não são anagramas!")

verificaAnagrama("amor", "roma")