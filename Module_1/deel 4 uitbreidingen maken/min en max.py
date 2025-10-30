nr1 = float(input("Geef het eerste gehele getal (nr1): "))
nr2 = float(input("Geef het tweede gehele getal (nr2): "))

minimum = nr1
maximum = nr2
verschil = maximum - minimum
try:
    if nr1 == nr2:
        print(f'Beide getallen zijn even groot (nr1: {nr1}, nr2: {nr2})')
    elif nr1 > nr2:
        print(f'nr1 ({nr1}) is groter dan nr2 ({nr2})')
        minimum = nr2
        maximum = nr1
    else:
        print(f'nr2 ({nr2}) is groter dan nr1 ({nr1})')
        minimum = nr1
        maximum = nr2
    print(f"Het minimum is: {minimum} en het maximimum is: {maximum}")
except:
    print("dit kan niet")