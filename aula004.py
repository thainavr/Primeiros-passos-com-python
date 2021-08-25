"""
Tipos de dados
"""
# str - string: textos 'Assim' ou "Assim" vale para números tbm
# int - inteiro: 12340 ou -1 -2 -3 NÃO PODE TER PONTO
# float - real/ponto flutuante(casas decimais): negativo ou positivo que tenha ponto. No python não se utiliza , -10.10, 0.0
# bool - booleano/lógico: só tem dois valores, true ou false

print('Luiz', type('Luiz'))
print(10, type(10))
print(25.6, type(25.6))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
print('l' == 'L', type('L' == 'L'))

"""
type: retorna o tipo de dado
dois sinais de igual: 10 é igual a 10? Tom de pergunta
"""

#Converter um tipo para outro

#print('Nana', type('Nana'), bool('Luiz'))
#print('10', type('10'), type(int('10')))
#print('Nana', float('10.5'))
#print('Nana', float('10'))

#Nome
print('Nana', type('Nana'))
#Idade
print(21, type(21))
#Peso
print(1.65, type(1.65))
#É maior de idade
print(21 > 18, type(21 > 18))