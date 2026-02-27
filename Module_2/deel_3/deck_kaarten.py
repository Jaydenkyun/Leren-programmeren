import random

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
waarden = ["2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas"]

deck = []
for kleur in kleuren:
    for waarde in waarden:
        deck.append(kleur + " " + waarde)

deck.append("joker")
deck.append("joker")

random.shuffle(deck)

for i in range(1, 8):
    kaart = deck.pop()
    print("kaart", i, ":", kaart)

print("\ndeck (" + str(len(deck)) + " kaarten):", deck)