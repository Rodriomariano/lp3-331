def contar_palavras(frase):
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower()
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem


print("\nCONTAGEM DE PALAVRAS")
frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)
print("Contagem de palavras:", resultado)