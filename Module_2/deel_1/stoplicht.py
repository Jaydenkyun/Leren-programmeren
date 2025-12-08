import time
stoplicht = True
kleur = "rood"
tijd_rood = 1
lengte = 30
tijd_groen = 1

while stoplicht == True:
    print (kleur)
    if kleur == "rood":
        tijd_rood +=1
        time.sleep(1)

    elif tijd_rood == 30:
        tijd_rood = 1
        kleur = "groen"
        print(kleur)
        tijd_groen +=1

    elif tijd_groen == 30:
        tijd_groen = 1
        kleur = "oranje"
        print(kleur)
        tijd_oranje +=1

    