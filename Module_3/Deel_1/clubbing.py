VIP_LIST = ('jeroen', 'jouke', 'rudi')

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30
bandjekleur = None
stempel = False


leeftijd = int(input("hoe oud ben je?"))
if leeftijd < 18:
    print("sorry je mag niet naar binnen")
    proberen = 18 - leeftijd
    print(f"probeer het nog eens in {proberen} jaar")
    exit()

naamvraag = input("wat is je naam?")
if naamvraag in VIP_LIST:
    if leeftijd >= 21:
        bandjekleur = "blauw"
    elif leeftijd <= 21:
        bandjekleur = "rood"
    print(f"je krijgt een {bandjekleur} bandje")
elif naamvraag not in VIP_LIST:
    if leeftijd >= 21:
            print("je krijgt van mij een stempel")
            stempel = True
keuzedrank = input("wat wil je drinken? kies uit: cola, bier, champangne")
if keuzedrank  not in ["cola", "bier", "champagne"]:
     print("sorry geen idee wat je bedoelt hier is een glaasje water")
     exit()
if keuzedrank == "champagne":
    if bandjekleur == "rood":
        print("je mag met een rood bandje geen champange bestellen")
    if bandjekleur != "blauw":
        print("sorry alleen vips mogen champange bestellen")
        exit()

elif keuzedrank == "bier":
    if not stempel and bandjekleur not in ["blauw", "rood"]:
        print("sorry je mag geen alcohol bestellen onder 21")
        exit()
    elif bandjekleur in ["blauw", "rood"]:
        print("alsjeblieft complimenten van het huis")
        exit()


        
elif keuzedrank == "cola":
    if bandjekleur in ["blauw", "rood"]:
        print("alsjeblieft complimenten van het huis")
        exit()

if keuzedrank == "cola":
    print(f"alsjeblieft je {keuzedrank} dat is dan {PRIJS_COLA}0")
    exit()

elif keuzedrank == "bier":
    print(f"alsjeblieft je {keuzedrank} dat is dan {PRIJS_BIER}0")
    exit()

elif keuzedrank == "champagne":
    print(f"alsjeblieft je {keuzedrank} dat is dan {PRIJS_CHAMPAGNE}0")
    exit()

