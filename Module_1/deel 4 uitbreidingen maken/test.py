producten =[
    {"naam":"Appel","prijs":2},
    {"naam":"boek","prijs":15},
    {"naam":"laptop","prijs":999},
]

duurdere_producten = []

for product in producten:
    if product["prijs"] > 10:
        print(product["naam"])
        duurdere_producten.append(product["naam"])
print(duurdere_producten)

aantal_duurdere_producten = len(duurdere_producten)
print(aantal_duurdere_producten)
