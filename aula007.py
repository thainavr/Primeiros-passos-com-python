"""
Formatação de strings
"""
nome = 'Nana'
idade = 21
altura = 1.65
e_maior = idade > 18
peso = 63
imc = (altura * altura)/peso

print(nome, 'possui', idade, 'anos de idade. E seu imc é de ', imc)
print(f'{nome} tem {idade} anos de idade. E seu imc é de {imc:.2f}')
"""
Caso eu queria arredondar valor da minha variável (imc) colocasse ":.2f" onde
o 2 significa duas casas decimais
"""
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
#Ordem
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
