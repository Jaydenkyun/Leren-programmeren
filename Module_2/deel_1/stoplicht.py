import time
stoplicht = True
kleur = "rood"
tijd = 1
while stoplicht == True:
    if tijd > 20:
        kleur = "groen"
    if tijd > 50:
        kleur = "oranje"
    if tijd == 60:
        tijd = 0
    print(kleur)
    time.sleep(1)
    tijd += 1