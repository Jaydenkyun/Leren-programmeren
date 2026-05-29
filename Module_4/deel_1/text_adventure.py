import time

print("je bent een soldaat in een middeleeuwse oorlog en je bent uitgekozen om te vechten voor jouw staat")
print("je hebt gekregen een zwaard en harnas")
time.sleep(1)

print("vannacht slaap jij in een kamp vlakbij het front")
time.sleep(1)

print("je hoort soldaten praten over hoeveel mensen morgen dood gaan")
time.sleep(1)

print("iemand naast jouw zegt dat hij liever een arm kwijt raakt dan naar het front gaat")
time.sleep(1)

print("morgen mag je vertrekken voor je eerste gevecht (en laatste als je het niet overleeft)")
time.sleep(1)

print("het is de volgende dag en je staat tegenover de oppositie je maakt je klaar in positie")
print("jouw commander schreeuwt CHARGE en jij rent het front")
time.sleep(2)

print("terwijl jij naar het front aan het rennen bent realiseer jij charge? dat is Engels")
time.sleep(1)

print("het blijkt dus dat in jouw tocht naar het front jij en een andere soldaat in het verkeerde leger zijn gekomen")
time.sleep(1)

print("wat ga je nu doen? je oud Engels is redelijk")
print("ga je: vechten voor de Engelsen, snel van kant switchen, of van binnenuit het leger waar je nu in staat slopen?")

vrg1 = input("kies uit: engelsen, switchen, binnenuit: ")


if vrg1 == "binnenuit":
    print("je doet alsof je gewoon mee aan het vechten bent en zwaait een beetje met jouw zwaard")
    time.sleep(1)

    print("zodra bijna iedereen druk bezig is steek jij ineens een soldaat neer")
    time.sleep(1)

    print("het was alles behalve fataal")
    time.sleep(1)

    print("de soldaat draait zich om en schreeuwt TRAITOR")
    time.sleep(1)

    print("meer soldaten kijken meteen jouw kant op")
    time.sleep(1)

    print("wat doe je nu?")
    print("rennen of liegen")

    actie2 = input("kies uit: rennen, liegen: ")

    if actie2 == "rennen":
        print("je probeert snel weg te rennen")
        time.sleep(1)

        print("maar iemand gooit een speer recht in jouw rug")
        time.sleep(1)

        print("je valt face first in de modder")
        time.sleep(1)

        print("vervolgens word je van 6 kanten gestoken")
        time.sleep(1)

        print("EINDE naam: jij wel Tarzan")

    else:
        print("je zegt dat die soldaat een spion was")
        time.sleep(1)

        print("een commander kijkt jouw raar aan")
        time.sleep(1)

        print("wat doe je nu?")
        print("meer liegen of commander aanvallen")

        actie3 = input("kies uit: liegen, aanvallen: ")

        if actie3 == "liegen":
            print("je verzint een heel verhaal over geheime berichten")
            time.sleep(1)

            print("tot jouw geluk gelooft de commander het")
            time.sleep(1)

            print("jij krijgt zelfs respect van andere soldaten")
            time.sleep(1)

            print("GOED EINDE naam: goed met woorden")

        else:
            print("je probeert de commander neer te steken")
            time.sleep(1)

            print("2 soldaten pakken direct jouw armen vast")
            time.sleep(1)

            print("iemand slaat met een hamer op jouw hoofd")
            time.sleep(1)

            print("EINDE naam: extreme chiropractor sessie")


elif vrg1 == "engelsen":
    print("je besluit gewoon mee te vechten voor de Engelsen")
    time.sleep(1)

    print("je ziet twee soldaten voor jouw staan")
    time.sleep(1)

    print("de soldaat links zit onder bloed en lacht alsof hij gek is(dat is hij)")
    print("de soldaat rechts zit naast een gewonde vriend")

    vrg1_en = input("welke wordt het links of rechts: ")

    if vrg1_en == "links":
        print("de soldaat rent schreeuwend op jouw af")
        time.sleep(1)

        print("wat doe je?")
        print("aanvallen of blokken")

        actie4 = input("kies uit: aanvallen, blokken: ")

        if actie4 == "aanvallen":
            print("je rent ook naar voren en zwaait wild met jouw zwaard")
            time.sleep(1)

            print("na veel gehak weet je hem neer te krijgen")
            time.sleep(1)

            print("Engelse soldaten beginnen jouw naam te schreeuwen")
            time.sleep(1)

            print("GOED EINDE naam: the butcher")

        else:
            print("je blijft alleen maar blokken")
            time.sleep(1)

            print("uiteindelijk breekt jouw arm door een harde klap")
            time.sleep(1)

            print("daarna word jouw keel opengesneden")
            time.sleep(1)

            print("EINDE naam: keelontsteking")

    else:
        print("de soldaat vraagt of jij zijn vriend kan helpen")
        time.sleep(1)

        print("help je hem of loop je weg?")

        actie5 = input("kies uit: helpen, weglopen: ")

        if actie5 == "helpen":
            print("je helpt de gewonde soldaat overeind")
            time.sleep(1)

            print("later blijkt hij familie van een belangrijke commander")
            time.sleep(1)

            print("jij krijgt goud en beter eten")
            time.sleep(1)

            print("GOED EINDE naam: mooi gedaan")

        else:
            print("je loopt gewoon weg")
            time.sleep(1)

            print("plotseling krijg je een pijl in jouw schouder")
            time.sleep(1)

            print("nog 2 pijlen volgen")
            time.sleep(1)

            print("EINDE naam: dart bord")


elif vrg1 == "switchen":
    print("je probeert terug te rennen naar jouw echte leger")
    time.sleep(1)

    print("overal vliegen pijlen en mensen schreeuwen")
    time.sleep(1)

    print("onderweg zie jij een paard zonder ruiter")

    actie6 = input("pak je het paard? ja of nee: ")

    if actie6 == "ja":
        print("je springt op het paard")
        time.sleep(1)

        print("maar het paard raakt compleet in paniek")
        time.sleep(1)

        print("wat doe je?")
        print("springen of blijven zitten")

        actie7 = input("kies uit: springen, blijven: ")

        if actie7 == "springen":
            print("je springt er net op tijd af")
            time.sleep(1)

            print("het paard rent recht een groep soldaten in")
            time.sleep(1)

            print("jij weet veilig jouw leger te bereiken")
            time.sleep(1)

            print("GOED EINDE naam: lucky bastard")

        else:
            print("je blijft zitten terwijl het paard full speed het gevecht in rent")
            time.sleep(1)

            print("een speer gaat dwars door jouw borst")
            time.sleep(1)

            print("EINDE naam: kip sate")

    else:
        print("je rent verder zonder paard")
        time.sleep(1)

        print("een soldaat van jouw eigen leger ziet jouw Engelse outfit")
        time.sleep(1)

        print("hij denkt dat jij een vijand bent")

        actie8 = input("roep je STOP of aanval: ")

        if actie8 == "STOP":
            print("je schreeuwt dat je bij hun hoort")
            time.sleep(1)

            print("de soldaat herkent jouw stem")
            time.sleep(1)

            print("jij overleeft de oorlog")
            time.sleep(1)

            print("GOED EINDE naam: friendly fire ontweken")

        else:
            print("je valt hem direct aan")
            time.sleep(1)

            print("meer soldaten zien het en springen op jouw")
            time.sleep(1)

            print("EINDE naam: friendly fire")