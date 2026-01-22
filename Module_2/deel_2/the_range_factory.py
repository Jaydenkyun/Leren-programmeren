aantal = int(input("Hoeveel lijstjes wil je? "))

alles = []
tekst = ""
begin = 1

for i in range(aantal):
    invoer = int(input(f"Geef waarden voor lijstje {i+1} "))
    for j in (range(invoer)):
        tekst += str(begin+j) + ","

    alles.append(tekst)
    tekst = ""
    begin += invoer
print(alles)