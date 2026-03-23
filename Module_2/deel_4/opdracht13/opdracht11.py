from fruitmand import fruitmand

kleuren = [fruit["color"] for fruit in fruitmand]

while True:
    kleur = input("Kies een kleur: ")
    if kleur in kleuren:
        break
    else:
        print(f"De kleur {kleur} kan niet")

rond = 0
niet_rond = 0

for fruit in fruitmand:
    if fruit["color"] == kleur:
        if fruit["round"]:
            rond += 1
        else:
            niet_rond +=1

if rond >= niet_rond:
    print(f"er zijn meer ronde fruitstukken dan nietronde van de kleur {kleur}")
if rond <= niet_rond:
    print(f"er zijn minder ronde fruitstukken dan nietronde van de kleur {kleur}")
if rond == niet_rond:
    print(f"er zijn evenveel ronde en niet ronde fruitstukken van de kleur {kleur}")

