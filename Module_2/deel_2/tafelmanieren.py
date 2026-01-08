tafel = int(input("typ het getal van de tafel\n"))
vermenigvuldiger = 0
hoeveel = 0
for hoeveel in range (1,11):
    if vermenigvuldiger <= 10:
        vermenigvuldiger += 1
        antwoord = vermenigvuldiger * tafel
        print(f"{vermenigvuldiger} x {tafel} = {antwoord}")