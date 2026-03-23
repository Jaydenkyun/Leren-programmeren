from fruitmand import fruitmand
namen_vertaald = {"yellow" : "gele",
                "green" : "groene",
                "orange" : "oranje",
                "red": "rode",
                "brown": "bruine" }
langste = ""
for fruit in fruitmand:
    if len(fruit["name"]) > len(langste):
        langste = fruit
kleur = namen_vertaald[langste["color"]]
print(f"de {langste["name"]}({len(langste["name"])} letters) heeft een {kleur} kleur en een gewicht van {langste["weight"]}gram")