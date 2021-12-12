import random
Kleuren = ["oranje", "blauw", "groen", "bruin"]
ZakList = []
ZakDictionary = {"oranje" : 0, "blauw" : 0, "groen" : 0, "bruin" : 0}
# --------------------------------------------------------------------

def MnM(aantal):
    global Inhoud
    for x in range(aantal):
        Willekeurig = random.randrange(0,4)
        Inhoud = Kleuren[Willekeurig]
        ZakList.append(Inhoud)
        ZakList.sort()
        if Inhoud == 'oranje':
            ZakDictionary['oranje'] += 1
        if Inhoud == 'blauw':
            ZakDictionary['blauw'] += 1
        if Inhoud == 'groen':
            ZakDictionary['groen'] += 1
        if Inhoud == 'bruin':
            ZakDictionary['bruin'] += 1
    return ZakDictionary, ZakList





Aantal = int(input('Hoeveel M&Ms wilt u? '))

print(MnM(Aantal))

