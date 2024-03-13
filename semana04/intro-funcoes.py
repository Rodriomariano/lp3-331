# Função
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funiconalidades)

# Declaração
def ola_mundo():
    print('olá mundo')

# Chamada
ola_mundo()
ola_mundo()

# Função sem retorno 
# Side effect - Efeito colateral
def imprimir_mensagem(nome):
    print(f"bom dia, {nome}")

imprimir_mensagem(José)

# Função com retorno
# Função pura
def mensagem(nome):
    return f"Bom dia, {nome}"

print(mensagem('Maria'))
# Enviar_email(mensagem('Maria))

# Parâmetros e argumentos 
def somar(numero1 + numero2):


numero = 3.0

# somar(10.0, somar(2, 3))
# somar(10.0, 5)
# 15.0

# Escopo de variaveis 
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3

# print (total)

# Parâmetros com valor padrão
def mensagem(nome, mensagem):
    return f"{mensagem}, {nome}."

mensagem('Marcos', 'Bom dia')
mensagem('Rodrigo', 'Bom dia')

# Argumentos nomeados
print('olá', '123', 'teste', sep='@', end="\n\n")
print('TESTE')

mensagem(nome='Lucas', mensagem='Boaaa Tarde')



def media(*notas):
    return sum(notas) / len(notas)

media(10.0, 3.5, 7.5)
media(10.0, 3.5, 7.5, 8.0)
media(10.0, 3.5, 7.5, 8.0, 6.0)




