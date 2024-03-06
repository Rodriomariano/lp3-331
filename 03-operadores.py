# Operadores
# aritimetcos 
# +, -, /, *, %

nota1 = 10
nota2 = 3
media = (nota1 + nota2) / 2

# potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado 


# logicos
# and, or, not
# acesso liberado = nao bloqueado, idade >= 18, horario comercial
bloqueado = False
idade = 21
hora_atual = 10

horario_comercial = hora_atual >= 8 and hora_atual <= 18
maior_idade = idade >= 18

if not bloqueado and maior_idade and hora_atual >= 8 and hora_atual <= 18:
    print('liberado')
else:
    print('nao liberado')

# operadores de comparacao
# >, <, >=, <=, ==, =!
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) #True

# operador is
print(numeros is numeros2) #False

numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) #True
print(numeros3 is not numeros4) #False


# in (bool)
print('a' is 'python') #False

prontuarios = ['SP001', 'SP002', 'SP003']
prontuario = 'SP002'
print(prontuario in prontuarios) #True

# sim, nao, talvez
opcao = ''

if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opcao valida')
else:
    print('opcao invalida')

opcoes = ('sim')



verdade = True and False
