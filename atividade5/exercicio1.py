'''Exercicio 1: Crie uma  função que calcule a gorjeta a ser deixada em um restaurante,
 baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.
'''

def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem/100)
    return gorjeta


valor_conta = float(input("Digite o valor da conta (ex: 100.00): "))
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)

print("\nPreço Final: ")
print(f"Valor da gorjeta: {valor_gorjeta:.2f}")
print(f"Valor total a pagar (valor_conta + gorjeta): R$ {valor_conta + valor_gorjeta:.2f}")