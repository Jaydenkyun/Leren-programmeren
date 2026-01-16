aantal = int(input("Hoeveel lijstjes wil je? "))

alles = []
tekst = ""

for i in range(aantal):
    invoer = int(input(f"Geef waarden voor lijstje {i+1} (gescheiden door komma): "))
    for j in (range(invoer)):
        tekst += str(j) + ","

    lijstje = invoer
    alles.append(tekst)
    tekst = ""
print(alles)
