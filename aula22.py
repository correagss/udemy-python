
# A ideia é nas opções, colocar por exemplo: A ou a, tanto faz a forma

entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# foi colocado a linha 12 entre parenteses, para executar primeiro
# como uma operação matemática

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')     
else:
    print('Sair')