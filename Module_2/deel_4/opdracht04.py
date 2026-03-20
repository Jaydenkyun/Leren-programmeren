from fruitmand import fruitmand
import random
vraag = False
while vraag == False:
    aantal = int(input("hoeveel fruitstukken wil je?"))
    for fruit in range(aantal):
        fruit = random.choice(fruitmand)
        print(fruit["name"])