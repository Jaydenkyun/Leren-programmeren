svr = input ("is het dranke rood?\n")

if svr == ("ja"):
    vr1 = input ("zit er citrus in het drankje?\n")
else:
    vr1 = ("no awnser")

if svr == ("nee"):
    vr2 = input ("is het drankje geel?\n")
else:
    vr2 = ("no awnser")



if vr1 == ("ja"):
    vr1s1 = input ("zit er bruisend water in het drankje?\n")
else:
    vr1s1 = ("no awnser")

if vr1 == ("nee"):
    vr1s2 = input ("zitten er druiven bij het drankje?\n")
else:
    vr1s2 = ("no awnser")

if vr2 == ("ja"):
    vr2s1 = input ("heeft het glas van het drinkje een steel?\n")
else:
    vr2s1 = ("no awnser")
if vr2 == ("nee"):
    vr2s2 = input ("zit er limoen in het drankje?\n")
else:
    vr2s2 = ("no awnser")



if vr1s1 == ("ja"):
    print ("je dranke is een cocktail spritz")
elif vr1s1 == ("nee"):
    print ("je drankje is een cocktail negroni")
elif vr1s2 == ("ja"):
    print ("je drankje is een cocktail kiv")
elif vr1s2 == ("nee"):
    print ("je drankje is een cocktail french martini")
elif vr2s1 == ("ja"):
    print ("je dranke is een cocktail white lady")
elif vr2s1 == ("nee"):
    print ("je drankje is een cocktail fizz")
elif vr2s2 == ("ja"):
    print ("je drankje is een cocktail mojito")
elif vr2s2 == ("nee"):
    print ("je drankje is een cocktail french connection")