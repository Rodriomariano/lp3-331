# Ex01

numero = int(input('digite um numero:'))

sucessor = numero + 1
antecessor = numero - 1

print('antecessor', antecessor)
print('sucessor', sucessor)

# Ex02

numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o seg Solicita ao usuário seu peso (Kg) e sua altura (m)undo numero:'))
numero3 = int(input('digite o terceiro numero:'))

media = (numero1 + numero2 + numero3) / 3

print('media', media)

# Ex03

def calcular_desconto(valor):
    if 0.01 <= valor < 10:
        desconto = 0
    elif 10 <= valor < 100:
        desconto = 0.05
    elif 100 <= valor < 500:
        desconto = 0.10
    else:
        desconto = 0.15
    
    valor_com_desconto = valor * (1 - desconto)
    
    return valor_com_desconto, desconto

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_final, desconto = calcular_desconto(valor_compra)
print(f"Valor final com desconto: R$ {valor_final:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")

# Ex04
def verificar_codigo(codigo):
    if len(codigo) != 7:
        return False
    
    if codigo[:2] != 'BR':
        return False

    if not codigo[2:6].isdigit():
        return False
    
    numero = int(codigo[2:6])
    if numero < 1 or numero > 9999:
        return False
    
    if codigo[6] != 'X':
        return False
    
    return True

print(verificar_codigo("BR0001X"))   
print(verificar_codigo("BR1236X"))   
print(verificar_codigo("BR9999X"))   
print(verificar_codigo("br0001X"))   
print(verificar_codigo("BR126X"))   
print(verificar_codigo("BR99999X"))  
print(verificar_codigo("BR9999Y"))   



# Ex05

def verificar_codigo(codigo):
    if len(codigo) != 7:
        return False
    
    if codigo[:2] != 'BR':
        return False
    
    if not codigo[2:6].isdigit():
        return False
    
    numero = int(codigo[2:6])
    if numero < 1 or numero > 9999:
        return False
    
    if codigo[6] != 'X':
        return False
    
    return True

identificador = input("Digite o identificador: ")

if verificar_codigo(identificador):
    print("O identificador é válido.")
else:
    print("O identificador é inválido.")

# Ex06

def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem_por_hora(volume):
    return volume * 2

comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temperatura_desejada = float(input("Digite a temperatura desejada (°C): "))
temperatura_ambiente = float(input("Digite a temperatura ambiente (°C): "))

volume = calcular_volume(comprimento, altura, largura)

potencia_termostato = calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)

filtragem_por_hora = calcular_filtragem_por_hora(volume)

print(f"O volume do aquário é de {volume} litros.")
print(f"A potência do termostato necessária é de {potencia_termostato} watts.")
print(f"A quantidade de filtragem por hora necessária é de {filtragem_por_hora} litros por hora.")

#Ex07

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Excesso de peso"
    elif 30 <= imc < 35:
        return "Obesidade de Classe 1"
    elif 35 <= imc < 40:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)

classificacao = classificar_imc(imc)

peso_normal = 24.9 * (altura ** 2)
diferenca_peso = peso_normal - peso

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
if imc != 24.9:
    if diferenca_peso > 0:
        print(f"Você precisa ganhar {diferenca_peso:.2f} Kg para atingir o peso normal.")
    else:
        print(f"Você precisa perder {abs(diferenca_peso):.2f} Kg para atingir o peso normal.")
else:
    print("Seu peso está dentro da faixa considerada normal.")




    

