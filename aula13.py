nome = 'Gabriel Corrêa'
altura = 1.75
peso = 82
imc = peso / altura ** 2

 # f-strings = f de formatação
linha_1 = f'{nome} tem {altura:.2f} de altura,' 
linha_2 = f'pesa {peso} quilos e seu imc é,'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)