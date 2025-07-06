'''Exercicio 2: Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.'''

from datetime import datetime

#Função para calcular a idade em dias
def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade_dias = calcular_idade_em_dias(ano_nascimento)

print(f"\nVocê tem aproximadamente {idade_dias} dias de Vida")

