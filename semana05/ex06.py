def conversor():
    nota = int(input("Digite sua nota: "))
    equivalencia = ""

    if nota <= 20:
        equivalencia = "F" 
    elif nota <= 40:
        equivalencia = "D"
    elif nota <= 60:
        equivalencia = "C"
    elif nota <= 80:
        equivalencia = "B"
    elif nota == 100:
        equivalencia = "A"

    return f"Sua nota equivale a: '{equivalencia}'"


print(conversor())