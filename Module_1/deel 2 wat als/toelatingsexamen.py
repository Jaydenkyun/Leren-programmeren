leeftijd = 13
heeft_magische_brief = True
magisch_huisdier = "uil" 
kent_spreuk = True
heeft_stok = True
op_zwarte_lijst = False
geslaagd_aanlegtest = True
heeft_strafblad = False

if leeftijd >= 11:
    if heeft_magische_brief:
        if magisch_huisdier in ["uil", "pad", "kat"]:
            if kent_spreuk:
                if heeft_stok:
                    if not op_zwarte_lijst:
                        if geslaagd_aanlegtest:
                            if not heeft_strafblad:
                                print("Toegelaten!")
                            elif heeft_strafblad:
                                print("Afgewezen: Strafblad bij de goblinbank.")
                        else:
                            print("Afgewezen: Je bent niet geslaagd voor de Magische aanlegtest.")
                    elif op_zwarte_lijst:
                        print("Afgewezen: Je staat op de zwarte lijst van het Ministerie.")
                elif not heeft_stok:
                    print("Afgewezen: Je hebt nog geen toverstok.")
            elif not kent_spreuk:
                print("Afgewezen: Je kent nog geen spreuken.")
        elif not magisch_huisdier:
            print("Afgewezen: Ongeldig magisch huisdier.")
    elif not heeft_magische_brief:
        print("Afgewezen: Geen magische uitnodiging ontvangen.")
elif leeftijd <= 11:
    print("Afgewezen: Je bent te jong.")