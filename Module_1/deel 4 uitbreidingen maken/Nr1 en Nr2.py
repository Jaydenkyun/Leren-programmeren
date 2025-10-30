nr1 = (input("Geef het eerste gehele getal (nr1): "))
nr2 = (input("Geef het tweede gehele getal (nr2): "))

if nr1 == nr2:
    print(f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})')
elif nr1 > nr2:
    print(f'nr1 ({nr1}) is groter dan nr2 ({nr2})')
else:
    print(f'nr2 ({nr2}) is groter dan nr1 ({nr1})')