import random
Kleuren = ["oranje", "blauw", "groen", "bruin"]
ZakList = []
ZakDictionary = {}
# --------------------------------------------------------------------

def List(aantal):
    for x in range(aantal):
        Inhoud = random.choice(Kleuren)
        ZakList.append(Inhoud)
        
    return ZakList

def Dictionary(aantal):
    for x in range(aantal):
        Inhoud = random.choice(Kleuren)
        if Inhoud in ZakDictionary.keys():
            ZakDictionary[Inhoud] += 1
        else:
            ZakDictionary[Inhoud] = 1
    return ZakDictionary

def Sorteren(lijst):
    lijst.sort()
    return lijst



Aantal = int(input('Hoeveel M&Ms wil je hebben? '))
List(Aantal)
print(Sorteren(ZakList))
print(Dictionary(Aantal))
