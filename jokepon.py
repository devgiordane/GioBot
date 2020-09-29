import random
# 1 - pedra
# 2 - papel
# 3 - tesoura

# ✊
# ✋
# ✌️


def jogar(p, nome):
    r = ""
    b = random.randint(1, 3)
    if b == 1 and p == 1:
        r = f"{nome}: ✊ VS GioBot: ✊\nPoxa empatamos, duas rochas, são duas rochas!"
    if b == 2 and p == 1:
        r = f"{nome}: ✊ VS GioBot: ✊\nAceita uma pedra embrulhada para presente"
    if b == 3 and p == 1:
        r = f"{nome}: ✊ VS GioBot: ✊\nPara que essa agressividade, sou uma tesoura em fase de crcimento."

    if b == 1 and p == 2:
        r = f"{nome}: ✊ VS GioBot: ✊\nAh, não me enrola, você ganhou essa na sorte"
    if b == 2 and p == 2:
        r = f"{nome}: ✊ VS GioBot: ✊\nUma luta de papeis, mas que papelão"
    if b == 3 and p == 2:

        r = f"{nome}: ✊ VS GioBot: ✊\nCorte seco! você foi cortado da competição!"
    if b == 1 and p == 3:
        r = f"{nome}: ✊ VS GioBot: ✊\nJá dizia o ditado, \"a pedra é mais forte que o aço\" - Giob, 2020"
    if b == 2 and p == 3:
        r = f"{nome}: ✊ VS GioBot: ✊\nVocê cortou nossa relação!"
    if b == 3 and p == 3:
        r = f"{nome}: ✊ VS GioBot: ✊\nCuidado, você não quer uma briga assim tão afiada."
    return r
