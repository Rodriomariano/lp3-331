def tabuada():
    numero = int(input('Digite um número: '))
    for x in range(0, 11):
        print(f"{numero} x {x} = {numero * x}")
        
tabuada()
