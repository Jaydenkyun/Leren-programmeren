wachtwoord = "kaasblok"


for poging in range(1, 6):
    wachtwoord_vraag = input("wat is het wachtwoord")

    if wachtwoord_vraag == wachtwoord:
        print("het klopt")
        break
    else:
        print("dit klopt niet")


