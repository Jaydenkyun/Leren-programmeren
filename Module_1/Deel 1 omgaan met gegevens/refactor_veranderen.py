naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
fav_kleur = input("Wat is je favoriete kleur? ")
fav_getal = int(input("Wat is je favoriete getal? "))
verschil_leeftijd = abs(leeftijd-fav_getal)
pronoun = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{pronoun.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", fav_kleur)
print(f"Het verschil tussen {pronoun} leeftijd en {fav_getal} is:", verschil_leeftijd)
