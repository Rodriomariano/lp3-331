import random
def game():
    return random.randint(1, 100)

def adivinhe():
    resposta = game()
    tentativa = 0
    print ('número gerado')
    
    chute = 0
    while chute is not resposta:
        tentativa +=1
        chute = int(input('qual é o seu chute: '))
        if chute > resposta:
            print('Errou, chute um numero menor que', chute)
        elif chute < resposta:
            print('Errou, chute um numero maior que', chute)
        else:
            print('Parabéns, o número gerado foi', chute, \
                'você acertou em', tentativa, 'tentativas')

while True:
    adivinhe()
    




            

        
