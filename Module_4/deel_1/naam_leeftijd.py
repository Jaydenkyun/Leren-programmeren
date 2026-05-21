def maak_dictionary():
    dictionary = {}

    naam = input("Geef een naam: ")

    if naam == "stop":
        return None

    leeftijd = input("Geef een leeftijd: ")

    if leeftijd == "stop":
        return None

    dictionary[naam] = leeftijd

    return dictionary


doorgaan = True
lijst = []

while doorgaan:

    resultaat = maak_dictionary()

    if resultaat is None:
        doorgaan = False
    else:
        lijst.append(resultaat)

print(lijst)