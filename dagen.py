Dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print('Alle dagen')
for x in range(0,7):
    print(Dagen[x])
print()

print('Werkdagen')
for x in range(0,5):
    print(Dagen[x])
print()

print('Weekenddagen')
for x in range(5,7):
    print(Dagen[x])
print()

print('Alle dagen omgekeerd')
for x in reversed(range(0,7)):
    print(Dagen[x])
print()

print('Werkdagen omgekeerd')
for x in reversed(range(0,5)):
    print(Dagen[x])
print()

print('Weekenddagen omgekeerd')
for x in reversed(range(5,7)):
    print(Dagen[x])
print()