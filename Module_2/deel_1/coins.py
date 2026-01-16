coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  #lijst met de waarde van de muntne

toPay = int(float(input('Amount to pay: ')) * 100) #de bedragen invullen en omzetten naar centen
paid = int(float(input('Paid amount: ')) * 100)  #de bedragen invullen en omzetten naar centen
change = paid - toPay

returnedCoins = {} # Dictionary voor overzicht van teruggegeven munten, want die worden hier dan zo toegevoegd


#While-loop om wisselgeld stap voor stap terug te geven
while change > 0 and len(coinValues) > 0: #len geeft aan hoeveel verschillende dingen in de lijst staan
    coinValue = coinValues.pop(0) #pop verwijderd het eerste ding uit de lijst zodat hij niet nog een keer langs hoeft te komen
    nrCoins = change // coinValue
    if nrCoins > 0:
        print('Return maximal', nrCoins, 'coins of', coinValue, 'cents!') # printje om voor de gebruiker duidelijk te maken hoeveel jij van deze euro of centen terug kan geven
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? ')) # input voor hoeveel geld jij van deze soort heb je

        # Opslaan in overzicht
        returnedCoins[coinValue] = nrCoinsReturned

        change -= nrCoinsReturned * coinValue # wisselgeld minder maken

print("\nteruggeven van de munten overzicht")
for coin, amount in returnedCoins.items():        # Overzicht printen na de loop
    print(f"{coin} cent: {amount} munt(en) teruggegeven")

# Melding als het wisselgeld niet helemaal of goed is teruggegeven
if change > 0: 
    print("\n Niet al het wisselgeld is teruggegeven")
    print("Nog te geven:", change, "cent")
else:
    print("\nAlles is goed teruggegeven")