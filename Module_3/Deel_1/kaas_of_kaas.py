import time
print("kies een van de 8 kazen")
print("Emmenthaler, leerdammer parmigiano regiano, goudse kaas, blue de rochbaron, foume d'ambert, cammembert, mozzarella")
print("beantwoord de vragen door te antwoorden met ja of nee")
print("")
time.sleep(2)

kaaskleurvraag = input("is de kaas geel?")
if kaaskleurvraag == ("ja"):
    gatenvraag = input("zitten er gaten in ?")
    if gatenvraag == ("ja"):
        duurvraag = input("is de kaas belachelijk duur?")
        if duurvraag == ("ja"):
            print("jouw kaas is Emmenthaler")
        elif duurvraag == ("nee"):
            print("jouw kaas is Leerdammer")
    elif gatenvraag == ("nee"):
        hardekaasvraag = input("is de kaas zo hard als steen")
        if hardekaasvraag == ("ja"):
            print("jouw kaas is parmigiano regiano")
        elif hardekaasvraag == ("nee"):
            print("jouw kaas is goudse kaas")

elif kaaskleurvraag == ("nee"):
    blauweschimmelvraag = input("heeft de kaas blauwe schimmel")
    if blauweschimmelvraag == ("ja"):
        korstvraag_1 = input("heeft de kaas een korst")
        if korstvraag_1 == ("ja"):
            print("jouw kaas is blue de rachbaron")
        elif korstvraag_1 == ("nee"):
            print("jouw kaas is foume d'abert")
    elif blauweschimmelvraag == ("nee"):
        korstvraag_2 = input("heeft uw kaas een korst")
        if korstvraag_2 == ("ja"):
            print("je kaas is camembert")
        elif korstvraag_2 == ("nee"):
            print("je kaas is mozzarella")