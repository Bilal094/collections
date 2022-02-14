import random
Kleuren = ['oranje', 'blauw', 'groen', 'bruin']
ZakDictionary = {}
ZakList = []
# --------------------------------------------------------------------
def Dictionary(aantal):
    for x in range(aantal):
        Inhoud = random.choice(Kleuren)
        if Inhoud in ZakDictionary.keys():
            ZakDictionary[Inhoud] += 1
        else:
            ZakDictionary[Inhoud] = 1
    return ZakDictionary

def Lijst(dict,lijst):
    oranjeAantal = dict.get('oranje')
    for a in range(oranjeAantal):
        lijst.append(Kleuren[0])
    blauwAantal = dict.get('blauw')
    for b in range(blauwAantal):
        lijst.append(Kleuren[1])
    groenAantal = dict.get('groen')
    for c in range(groenAantal):
        lijst.append(Kleuren[2])
    bruinAantal = dict.get('bruin')
    for d in range(bruinAantal):
        lijst.append(Kleuren[3])
    return ZakList

def Sorteren(lijst):
    lijst.sort()
    return lijst

Aantal = int(input('Hoeveel M&Ms wil je hebben? '))
Dictionary(Aantal)
Lijst(ZakDictionary, ZakList)
Sorteren(ZakList)
print(ZakList)
print(ZakDictionary)
