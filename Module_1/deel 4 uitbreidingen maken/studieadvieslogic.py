from studieadviestext import *


print(STUDIEDOKTER_TITEL)
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
input_AANTAL_WEKEN_VRAAG = int(input(f'{AANTAL_WEKEN_VRAAG}\n'))
print (OPTIES)
input_COMPETENTIE_STELLING_1 = int(input(f'{COMPETENTIE_STELLING_1}\n'))
print (OPTIES)
input_COMPETENTIE_STELLING_2 = int(input(f'{COMPETENTIE_STELLING_2}\n'))
print (OPTIES)
input_COMPETENTIE_STELLING_3 = int(input(f'{COMPETENTIE_STELLING_3}\n'))
print (OPTIES)
input_COMPETENTIE_STELLING_4 = int(input(f'{COMPETENTIE_STELLING_4}\n'))
print (OPTIES)
input_COMPETENTIE_STELLING_5 = int(input(f'{COMPETENTIE_STELLING_5}\n'))

if input_AANTAL_WEKEN_VRAAG >= 10:
    print (OPTIES)
    input_COMPETENTIE_STELLING_6 = int(input(f'{COMPETENTIE_STELLING_6}\n'))
    print (OPTIES)
    input_COMPETENTIE_STELLING_7 = int(input(f'{COMPETENTIE_STELLING_7}\n'))


zorgelijk_punten = 0
twijfelachtig_punten = 0

if input_COMPETENTIE_STELLING_1 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_2 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_3 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_4 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_5 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_6 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_7 <= 1:
    zorgelijk_punten =+1
    twijfelachtig_punten =+1

if input_COMPETENTIE_STELLING_1 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_2 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_3 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_4 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_5 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_6 == 2:
    twijfelachtig_punten =+1
if input_COMPETENTIE_STELLING_7 == 2:
    twijfelachtig_punten =+1


if input_AANTAL_WEKEN_VRAAG >=10:
    GEMIDDELDE_SCORE = int(input_COMPETENTIE_STELLING_1 + input_COMPETENTIE_STELLING_2 + input_COMPETENTIE_STELLING_3 + input_COMPETENTIE_STELLING_4 + input_COMPETENTIE_STELLING_5 + input_COMPETENTIE_STELLING_6 + input_COMPETENTIE_STELLING_7) /7
else:
    GEMIDDELDE_SCORE = int(input_COMPETENTIE_STELLING_1 + input_COMPETENTIE_STELLING_2 + input_COMPETENTIE_STELLING_3 + input_COMPETENTIE_STELLING_4 + input_COMPETENTIE_STELLING_5)/5

print (COMPETENTIE_ADVIES_TITEL)

if GEMIDDELDE_SCORE <= 2 or zorgelijk_punten >= 4:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif GEMIDDELDE_SCORE <= 3 or twijfelachtig_punten >=4:
    print (COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)


