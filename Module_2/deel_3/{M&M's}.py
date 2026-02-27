import random

kleuren = ["rood","blauw","groen","geel","bruin"]
zak = {}

hoeveel = int(input("hoeveel m&m's wilt u\n"))

for h in range(hoeveel):
    kleur_keuze = random.choice(kleuren)

    if kleur_keuze in zak:
        zak[kleur_keuze] += 1

    else:
        zak[kleur_keuze] = 1

print(f"de inhoud van de zak is {zak}")