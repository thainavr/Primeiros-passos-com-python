"""
1) Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa

2) Criar variável com o ano atual (int)

3) Obter o ano de nascimento da pessoa (baseado na idade e no atual ano)

4) Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)

5) Exibir um texto com todos os valores na tela usando F-Strings
"""

nome = 'Morgana'
idade = 26
altura = 1.81
peso = 60.2
ano = 2021
nascimento = (ano - idade)
imc = ((altura * altura)/peso)

print(f'Seu ano de nascimento é {nascimento} e seu imc é de {imc:.2f}')