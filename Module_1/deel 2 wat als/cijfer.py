cijfer = float(input("noem een cijfer tussen de 1 en 10\n"))
if cijfer > 10:
    print("dit kan ik niet omzetten")
elif cijfer > 9:
    print(f"gefeliciteerd, uitmuntend je resultaat is {cijfer}")
elif cijfer > 8:
    print(f"gefeliciteerd, zeer goed je resultaat is {cijfer}")
elif cijfer > 7:
    print(f"gefeliciteerd, goed je resultaat is {cijfer}")
elif cijfer > 6:
    print(f"gefeliciteerd, ruim voldoende je resultaat is {cijfer}")
elif cijfer > 5:
    print(f"gefeliciteerd, voldoende je resultaat is {cijfer}")
elif cijfer > 4:
    print(f"jammer, bijna voldoende je resultaat is {cijfer}")
elif cijfer > 3:
    print(f"jammer, onvoldoende je resultaat is {cijfer}")
elif cijfer > 2:
    print(f"jammer, gerig je resultaat is {cijfer}")
elif cijfer > 1:
    print(f"jammer, slecht je resultaat is {cijfer}")
elif cijfer > 0:
    print(f"jammer, zeer slecht je resultaat is {cijfer}")
else:
 print("dit kan ik niet omzetten")