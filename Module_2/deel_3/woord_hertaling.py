woorden = {
    "school" : "tafel",
    "vrienden" : "brotatos",
    "fiets" : "boeing 737-800",
    "huiswerk" : "spel",
    "boek" : "papiertje"
}



tekst = """Elke ochtend fietste Milan op zijn fiets naar school
Op school wachtte zijn leraar hem al op bij de deur
Tijdens de les pakte hij zijn boek uit zijn tas.Zijn vrienden zaten naast hem in de klas.Na de pauze moesten ze samen aan hun huiswerk werken.De leraar gaf extra uitleg uit het boek.Na school fietste Milan weer naar huis op zijn fiets.Thuis maakte hij zijn huiswerk verder af. Later belde hij zijn vrienden om te vragen of zij het huiswerk begrepen.
De volgende dag ging hij weer naar school met zijn fiets"""

for oud, nieuw in woorden.items():
    tekst = tekst.replace(oud, nieuw)

print(tekst)