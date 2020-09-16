import random
# 1 - pedra
# 2 - papel
# 3 - tesoura

def jogar(p):
    r = ""
    b = random.randint(1, 3)
    if b == 1 and p == 1:
        r = "Poxa empatamos, duas rochas, são duas rochas!"
    if b == 2 and p == 1:
        r = "Aceita uma pedra embrulhada para presente"
    if b == 3 and p == 1:
        r = "Para que essa agressividade, sou uma tesoura em fase de crcimento."

    if b == 1 and p == 2:
        r = "Ah, não me enrola, você ganhou essa na sorte"
    if b == 2 and p == 2:
        r = "Uma luta de papeis, mas que papelão"
    if b == 3 and p == 2:

        r = "Corte seco! você foi cortado da competição!"
    if b == 1 and p == 3:
        r = "Já dizia o ditado, \"a pedra é mais forte que o aço\" - Giob, 2020"
    if b == 2 and p == 3:
        r = "Você cortou nossa relação!"
    if b == 3 and p == 3:
        r = "Cuidado, você não quer uma briga assim tão afiada."
    return r