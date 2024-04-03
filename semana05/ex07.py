import random

def jogo_da_forca(palavra):
    tentativas = 6
    letras_corretas = set()
    palavra_oculta = ['_'] * len(palavra)

    while tentativas > 0:
        print("\nPalavra: ", " ".join(palavra_oculta))
        print("Tentativas restantes:", tentativas)
        
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente novamente.")
            continue

        if letra in palavra:
            print("Letra correta!")
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
            letras_corretas.add(letra)
            if '_' not in palavra_oculta:
                print("\nParabéns! Você adivinhou a palavra:", palavra)
                return
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas -= 1

    print("\nSuas tentativas acabaram. A palavra era:", palavra)


print("JOGO DA FORCA")
palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo"]
palavra_secreta = random.choice(palavras)
jogo_da_forca(palavra_secreta)

