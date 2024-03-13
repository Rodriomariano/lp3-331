#if, if/else, if/elif/else, tenario, match

#if
#if condicao:
#    codigo do if
#    codigo do if
#codigo

idade = 20
if idade >= 18:
    print('maior')

print('fora do if')

#if/else
idade = 20
if idade >= 18:
    print('maior')
else:
    print('menor')

#elif 
#crianca 0 12, adolescente 13 17, adulto 18 59, idoso 60+

idade = 30
if idade <= 12:
    print()
elif idade <= 17:
    print()
elif idade <= 59:
    print()
else:
    print()

# evitar alinhamento de ifs
email = ''
senha = ''

if email == 'admin123@gmail.com':
    if senha == '123admin':
        print('liberado')
    else:
        print('email ou senha incorretos')

# entrada numero 1, 2, 3 ...7
# saida dia: Domingo, Segunda, Terca... Sabado

dia = 4

if dia == 1:
    print('domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('terca')
else:
    print('outro')


dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terca',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sabado',
}

if dia in dias:
    print(dias[dia])
else:
    print('dia invalido')

# ternalo
media = 6.0

if media >= 6.0:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

situacao = 'aprovado' if media >= 6.0 else 'reprovado'

# match

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terca')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabado')
    case _:
        print('invalido')

# dia util 2, 3, 4, 5, 6
# fds 7,1 
match dia:
    case 1 | 7:
        print('fds')
    case 2 | 3 | 4 | 5 | 6:
        print('dia util')
    case _: 
        print('ivalido')
        





