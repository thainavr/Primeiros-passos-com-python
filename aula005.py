"""
Operadores aritméticos
"""

"""
+ = adição
- = subtração
* = multiplicação
/ = divisão (valor real)
// = divisão inteira (o resultado da divisão é arredondado)
** = exponenciação
% = resto da divisão (retorna o módulo)
() = parenteses (usados para alterar a precedência)
"""

print(10 * 10)
print(10 + 10)
print(17 - 4)
print(40 / 5)
print(40 // 3)

print('Multiplicação', 10 *'10')
"""
O operador * também serve como operador de repetição, precisando de um número inteiro e uma string
exemplo:
Quero repetir 10 vezes a letra 'A'
print('Multiplicação', 10 * 'A')
"""

print('Concatenação +', '5' + '5')
"""
Não funciona com número inteiro + string
"""
print('Nana' + ' ' + 'Vieira tem ' + str(21) + ' anos') #Raro
print(2 ** 10)
print(10 % 5)
print(10 % 3)

#Desafio
print(2 + (5 * (3 ** 2)) - (23.5 + 23.5))