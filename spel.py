import random
spelList = ["Monopoly", "Yathzee", "Bridge", "Poker", "Pesten", "Mens Erger Je Niet", "Cluedo"]

def spelProgramma(Lijst,min,max):
    MaxEnMin = random.randrange(3,11)
    for x in range(MaxEnMin):
        Spel = random.randrange(0,7)
        print(Lijst[Spel])
    print('Minimum = '+ str(min))
    print('Maximum = '+ str(MaxEnMin))

spelProgramma(spelList,3,10)

