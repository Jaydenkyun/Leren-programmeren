from naam_leeftijd_input import maak_dictionary

doorgaan = True
lijst = []

while doorgaan:

    resultaat = maak_dictionary()

    if resultaat is None:
        doorgaan = False
    else:
        lijst.append(resultaat)

print(lijst)