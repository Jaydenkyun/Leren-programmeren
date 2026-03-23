from fruitmand import fruitmand

def gewicht(fruit): #functie voor gewicht teruggeven
    return fruit["weight"]
#fruit sorteren
for fruit in sorted(fruitmand, key=gewicht, reverse=True):
    # printen in kilogrammen
    print(fruit["name"], fruit["weight"] / 1000, "kg")