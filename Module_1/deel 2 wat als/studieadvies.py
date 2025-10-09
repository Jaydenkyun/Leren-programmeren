STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
print(STUDIEDOKTER_TITEL)
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = int(input('Hoeveel weken ben je al bezig met de opleiding?\n'))
print (OPTIES)
COMPETENTIE_STELLING_1 = input('Ik voel stress of blokkades bij het maken van programmeeropdrachten.\n')
print (OPTIES)
COMPETENTIE_STELLING_2 = input('Ik sel programmeeropdrachten en -uitdagingen uit.\n')
print (OPTIES)
COMPETENTIE_STELLING_3 = input('Ik denk dat ik geen talent heb voor de opleiding.\n')
print (OPTIES)
COMPETENTIE_STELLING_4 = input('Ik vermijd assessments (CJV) en feedback van kritische docenten. \n')
print (OPTIES)
COMPETENTIE_STELLING_5 = input('Ik vergelijk mezelf met anderen die beter lijken te zijn.\n')

if AANTAL_WEKEN_VRAAG >= 10:
    print (OPTIES)
    COMPETENTIE_STELLING_6 = input('Ik voel geen interesse in nieuwe programmeertechnieken.\n')
    print (OPTIES)
    COMPETENTIE_STELLING_7 = input('Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.\n')

if AANTAL_WEKEN_VRAAG >=10:
    GEMIDDELDE_SCORE = int(COMPETENTIE_STELLING_1 + COMPETENTIE_STELLING_2 + COMPETENTIE_STELLING_3 + COMPETENTIE_STELLING_4 + COMPETENTIE_STELLING_5 + COMPETENTIE_STELLING_6 + COMPETENTIE_STELLING_7) /7
else:
    GEMIDDELDE_SCORE = int(COMPETENTIE_STELLING_1 + COMPETENTIE_STELLING_2 + COMPETENTIE_STELLING_3 + COMPETENTIE_STELLING_4 + COMPETENTIE_STELLING_5)/5


COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

if GEMIDDELDE_SCORE <= 2:
    print (COMPETENTIE_ADVIES_TITEL)
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif GEMIDDELDE_SCORE <= 3:
    print (COMPETENTIE_ADVIES_TITEL)
    print (COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_TITEL)
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)