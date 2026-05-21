import random

naamlijst = []
gekoppeld = {}

# Namen toevoegen
while True:
    naam = input("Voer een naam in: ")

    if naam not in naamlijst:
        naamlijst.append(naam)
        print("Naam toegevoegd.")
    else:
        print("Naam staat al in de lijst.")

    if len(naamlijst) >= 3:
        antwoord = input("Wil je meer namen toevoegen? (ja/nee): ")

        if antwoord.lower() == "nee":
            break

# Namen koppelen
beschikbaar = naamlijst.copy()

for naam in naamlijst:
    keuze = random.choice(beschikbaar)

    while keuze == naam:
        keuze = random.choice(beschikbaar)

    gekoppeld[naam] = keuze
    beschikbaar.remove(keuze)

# Persoon controleren
gelinkedvraag = input("Typ een naam in: ")

if gelinkedvraag in gekoppeld:
    print(gelinkedvraag, "heeft:", gekoppeld[gelinkedvraag])
else:
    print("Naam niet gevonden.")