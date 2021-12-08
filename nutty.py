from contextlib import nullcontext
import random


Zakje = []
mnmDictionary = {'oranje': 0, 'blauw': 0, 'groen': 0, 'bruin': 0}
Kleur = ["oranje", "blauw", "groen", "bruin"]

Aantal = int(input('Hoeveel M&Ms moeten er worden gevuld? '))


def nutty(aantal:int):
    global Inhoud
    for x in range(Aantal):
        Inhoud = random.choice(Kleur)
        Zakje.append(Inhoud)
    print(Zakje)

nutty(Aantal)


def nuttyDict(aantal:int):
    global InhoudDict
    for x in range(Aantal):
        InhoudDict = random.choice(Kleur)
        if InhoudDict == 'oranje':
            mnmDictionary['oranje'] += 1
        if InhoudDict == 'blauw':
            mnmDictionary['blauw'] += 1
        if InhoudDict == 'groen':
            mnmDictionary['groen'] += 1
        if InhoudDict == 'bruin':
            mnmDictionary['bruin'] += 1
    print(mnmDictionary)

nuttyDict(Aantal)



