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