# komma werkt niet tussen de euros en de centen in gebruik: .
bedrag = float(input("wat is het bedrag? "))

def afgerond(bedrag: float) -> float:
    return round(bedrag * 20) / 20

print(afgerond(bedrag))
