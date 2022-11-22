# cuvant = ' o n o m a t o p e e'
"""
cuvantul de inceput si litera de sfarsit se gasesc in interiorul cuvantului, litara trebuie sa fie vizibila
cuvant = ' o _ o _ _ _ o _ e e '
7 incercari
"""
import random
from cuvinte_spanzuratoarea import cuvinte_de_ghicit as lista_cuvinte
cuvant_de_ghicit = random.choice(lista_cuvinte)
cuvant = list(cuvant_de_ghicit)

def parcurgere_cuvant(word: str, simbol_de_inlocuit: str, cuvant_ascuns: list) -> str:
    """
    :param word: reprezinta cuvantul care trebuie ghicit
    :param simbol_de_inlocuit: simbolul cu care se inlocuieste
    :param cuvant_ascuns: cuvantul ascuns si modificat dupa fiecare introducere de caracter
    :return: cuvantul modificat
    """
    for index, valoare in enumerate(word):
        if simbol_de_inlocuit == '_' and word[0] != valoare and word[-1] != valoare:
            cuvant_ascuns[index] = simbol_de_inlocuit
        elif word[0] != valoare and word[-1] != valoare and valoare == simbol_de_inlocuit:
            cuvant_ascuns[index] = simbol_de_inlocuit
    return cuvant_ascuns


def info(check_character) -> str:
    if check_character.isalpha() is False:
        return "Te rugam sa adaugi o litera"
    if len(check_character) > 1:
        return "Ai adaugat mai multe caractere. Te rugam sa adaugi o singura litera"
    if check_character in ["", " "]:
        return "Ai adaugat un spatiu. Te rugam sa introduci un caracter"

cuvant_de_afisat = ' '.join(parcurgere_cuvant(cuvant_de_ghicit, ' ', cuvant))
print(f"Cuvantul de ghicit este: {cuvant_de_afisat}")
"""
sa nu fie cifra -> string.isdigit()
sa nu introduca mai mult de un caracter -> len(string) > 1
sa nu fie spatiu
"""
litere_incercate = set()
numar_incercari = 0
while numar_incercari < 7:
    if len(list(litere_incercate)) > 0:
            print(f'Literele incercate sunt: {",".join(litere_incercate)}')
    litera_de_incercat = input("Adauga o litera: ").lower()
    while litera_de_incercat.isalpha() is False or len(litera_de_incercat) > 1 or litera_de_incercat in ["", " "]:
        print(info(litera_de_incercat))
        litera_de_incercat = input("Adauga o litera: ").lower()
    if litera_de_incercat not in cuvant_de_ghicit:
        numar_incercari += 1
        litere_incercate.add(litera_de_incercat)
    elif litera_de_incercat in cuvant_de_ghicit and (cuvant_de_ghicit[0] != litera_de_incercat
                                                     and cuvant_de_ghicit[-1] != litera_de_incercat):
        cuvant = parcurgere_cuvant(cuvant_de_ghicit,litera_de_incercat, cuvant)

    if '_' not in cuvant:
        print("Ai castigat")
        break
    elif numar_incercari == 7:
        print(f"Ai pierdut. Cuvantul initial era: {cuvant_de_ghicit}")
        break
    if (numar_incercari_ramase := 7 -numar_incercari) and numar_incercari_ramase > 0:
        print(f"Mai ai {numar_incercari_ramase} incercari")
        print(" ".join(cuvant))