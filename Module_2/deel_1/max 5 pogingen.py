wachtwoord = "kaasblok"
wachtwoord = False
pogingen = 0


while wachtwoord == False and pogingen <5:
    wachtwoord_vraag = input("wat is het wachtwoord")

    pogingen += 1
    if wachtwoord_vraag == "kaasblok":
        wachtwoord = True
        print("je bent ingelogd")
    else:
        print("klop niet")

print(f"je hebt {pogingen} pogingen gedaan ")