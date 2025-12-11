# name of student: 
# number of student:
# purpose of program: 
# structure of program: 
coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # lijst van muntwaardes in centen)

toPay = int(float(input('Amount to pay: ')) * 100)  # veranderen naar centen
paid = int(float(input('Paid amount: ')) * 100)     # hetzelfde voor het betaalde bedrag, ook in centen
change = paid - toPay                               # bereken hoeveel wisselgeld terug moet worden gegeven

returnedCoins = {}  # dictionary voor de verschillende muntensoorten

while change > 0 and len(coinValues) > 0:  # while loopt zolang er wisselgeld nodig is en er nog muntsoorten in de lijst zitten

    coinValue = coinValues.pop(0)         # pop(0) verwijdert en retourneert het eerste element uit de lijst (grootste munt eerst)
    nrCoins = change // coinValue         # // is floor division; geeft hoeveel van deze munt in het resterende change past

    if nrCoins > 0:  # alleen relevante munten tonen (waar er minimaal 1 van teruggegeven kán worden)

        print('Return maximal', nrCoins, 'coins of', coinValue, 'cents!')  
        
        nrCoinsReturned = int(input('How many coins of ' 
                                    + str(coinValue) +
                                    ' cents did you return? '))  # gebruiker vult echt aantal teruggegeven munten in

        change -= nrCoinsReturned * coinValue   # aftrekken van het resterende wisselgeld

        returnedCoins[coinValue] = nrCoinsReturned  # opslaan in dictionary voor later overzicht