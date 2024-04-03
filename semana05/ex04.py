def eleicao():
    candidatos = {
            "candidato 1": 0,
            "candidato 2": 0,
            "candidato 3": 0
    }
    
    while True:
        voto = int(input("Vote em um candidato: "))
        if voto == 1:
            candidatos["candidato 1"] += 1
        elif voto == 2:
            candidatos["candidato 2"] += 1
        elif voto == 3:
            candidatos["candidato 3"] += 1

        resposta = str(input("Quer continuar [S/N]: "))
        if resposta in "Nn":
            break
    
    keys = list(candidatos.keys())
    if candidatos["candidato 1"] > candidatos["candidato 2"] and candidatos["candidato 1"] > candidatos["candidato 3"]:
        vencedor = keys[0]
    elif candidatos["candidato 2"] > candidatos["candidato 1"] and candidatos["candidato 2"] > candidatos["candidato 3"]:
        vencedor = keys[1]
    elif candidatos["candidato 3"] > candidatos["candidato 1"] and candidatos["candidato 3"] > candidatos["candidato 2"]:
        vencedor = keys[2]

    conclusao = f"""
    {keys[0]}: {candidatos["candidato 1"]}
    {keys[1]}: {candidatos["candidato 2"]}
    {keys[2]}: {candidatos["candidato 3"]}

    O vencedor é o {vencedor}
    """
    return conclusao


print(eleicao())