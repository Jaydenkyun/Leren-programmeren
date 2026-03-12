from fruitmand import fruitmand
import random

aantal = int(input("hoeveel fruitstukken wil je?"))
for verschil in range(aantal):
    fruit = random.choice(fruitmand)
    print(fruit["name"])