listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def addAndDisplayLists(list1,list2):
    for x in range(10):
        Antwoord = list1[x] + list2[x]
        print(str(list1[x]) +' + '+ str(list2[x]) + ' = '+ str(Antwoord))

def substractAndDisplayLists(list1,list2):
    for x in range(10):
        Antwoord = list1[x] - list2[x]
        print(str(list1[x]) +' - '+ str(list2[x]) + ' = '+ str(Antwoord))

def multiplyAndDisplayLists(list1,list2):
    for x in range(10):
        Antwoord = list1[x] * list2[x]
        print(str(list1[x]) +' * '+ str(list2[x]) + ' = '+ str(Antwoord))

def divideAndDisplayLists(list1,list2):
    for x in range(10):
        Antwoord = list1[x] / list2[x]
        print(str(list1[x]) +' / '+ str(list2[x]) + ' = '+ str(Antwoord))


addAndDisplayLists(listOne,listTwo)
print()
substractAndDisplayLists(listOne,listTwo)
print()
multiplyAndDisplayLists(listOne,listTwo)
print()
divideAndDisplayLists(listOne,listTwo)