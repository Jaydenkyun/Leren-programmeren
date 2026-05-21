def getal_even(getal: int) -> bool:
    return getal % 2 == 0


def woorden_omdraaien(zin: str) -> str:
    woorden = zin.split()
    omgekeerde_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgekeerde_woorden)
    return omgekeerde_zin


def aantal_unieke_letters(tekst: str) -> int:
    unieke_letters = set(tekst)
    aantal_letters = len(unieke_letters)
    return aantal_letters


def gemiddelde_woordlengte(zin: str) -> float:
    woorden = zin.split()

    if len(woorden) == 0:
        return 0

    totaal_aantal_letters = 0

    for woord in woorden:
        totaal_aantal_letters += len(woord)

    gemiddelde = totaal_aantal_letters / len(woorden)
    return gemiddelde


def tafels_printen(vermenigvuldiger: int, tot_en_met: int = 10) -> None:
    for getal in range(1, tot_en_met + 1):
        uitkomst = getal * vermenigvuldiger
        print(f'{getal} x {vermenigvuldiger} = {uitkomst}')


print(getal_even(4))
print(woorden_omdraaien("hallo wereld"))
print(aantal_unieke_letters("banaan"))
print(gemiddelde_woordlengte("dit is een test"))
tafels_printen(5)