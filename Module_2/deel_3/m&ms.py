import random
kleuren = ("oranje", "blauw","groen","bruin")
hoeveel = int(input("hoeveel m&m's wil je\n"))
zak = []
for i in range(hoeveel):
    zak.append(random.choice(kleuren))

print(zak)