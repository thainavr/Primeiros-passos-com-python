"""
Variáveis
"""
"""
Salvas na memória RAM do computador
Iniciar com letra, pode conter números, separar_, letras minúsculas
"""

nome = 'Nana'
idade = """21"""
altura = 1.65
e_maior = idade > 18
peso = 63
imc = (altura * altura)/peso

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior de idade?', e_maior)
print(idade * altura)

print(nome, 'possui', idade, 'anos de idade. E seu imc é de ', imc)

#print(nome, type(nome))