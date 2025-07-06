'''Exercicio 3: Crie uma função que verifique se uma palavra ou frase é um palindromo
 (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim",
se o resultado for False, responda "Não".'''

import re

def verificar_palindromo(texto):
    #Remove espaços, pontuação e deixa tudo minúsculo
    texto_limpo = re.sub(r'[^a-zA-Z0-9]','',texto.lower())

    #Verifica se o texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    
frase = input("Digite uma palavra ou frase para verificar se é palíndromo: ")

resultado = verificar_palindromo(frase)
print(f"\nÉ Palíndromo: {resultado}")