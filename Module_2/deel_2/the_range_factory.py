aantal = int(input("Hoeveel lijstjes wil je? "))

alles = []
tekst = ""
begin = 1 # hij start bij een

for i in range(aantal): #voor elk lijstje dat jij wilt doet hij dit opnieuw in een loop
    invoer = int(input(f"Geef waarden voor lijstje {i+1} ")) #hier vraagt hij welke waarden jij het lijstje wil geven +1 is er om niet bij lijstje 0 te kunnen beginnen
    for j in (range(invoer)):
        tekst += str(begin+j) + ","

    alles.append(tekst)
    tekst = ""
    begin += invoer #hier onthoud hij waar het ene lijstje is beïndigd om het volgende lijtje te beginnen
print(alles)