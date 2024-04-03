def palindromo():
    frase = str(input('Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    # Outra forma seria declarar inverso = junto[::-1], o código ficaria bem menor
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]  # Mesmo que inverso = inverso + junto[letra]
    # Declarando como a frase é do contrário
    print(f'{junto} do contrário, é {inverso}')
    # Verificando se é ou não um palíndromo
    if inverso == junto:
        print('Temos um palíndromo! ')
    else:
        print('Não é um palíndromo')


palindromo()