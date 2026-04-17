boodschappenlijstje = {}
while True:
    print(" de artikelen zijn: (bier, hagelslag, brood, beleg, bananen, chips)")
    product = input("welk product wilt u toevoegen?")
    aantal = input(f"hoeveel {product} stuks wilt u?")
    if product not in boodschappenlijstje:
        boodschappenlijstje[product] = (f" x {aantal}")
        print(boodschappenlijstje)
    elif product in boodschappenlijstje:
        boodschappenlijstje[product]
        boodschappenlijstje.update({
        product: (f"{aantal}")
        })
    doorgaan_vraag = input("wilt u nog meer boodschappen toevoegen? ja of nee ")
    if doorgaan_vraag == ("nee"):
        break
print("***BOODSCHAPPEN LIJST***")
print("")
print(f"  {boodschappenlijstje}")
print("")
print("--------------------------")




