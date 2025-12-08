wachtwoord = "kaasblok"
wachtwoord = False
pogingen = 0


while wachtwoord == False and pogingen <5:
    wachtwoord_vraag = input("wat is het wachtwoord")

    if wachtwoord_vraag == "kaasblok":
        wachtwoord = True
        break
    else:
        print("klop niet")
        pogingen += 1