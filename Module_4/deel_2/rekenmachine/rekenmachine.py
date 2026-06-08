import functions 
first_round = True
while True:
    print("wat wilt u doen?")
    print("A) optellen")
    print("B) aftrekken")
    print("C) vermenigvuldigen")
    print("D) delen")
    print("E) ophogen")
    print("F) verlagen")
    print("G) verdubbelen")
    print("H) halveren")
    print("I) niets")
    while True:
        functie = input("kies:").upper()
        if functie in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
            break
        else:
            print("voer een van de voorgestelde letters in")

    if functie == "I" or functie == "":
        print("einde berekening")
        exit()

    if first_round:
        while True:
            try:
                n1 = float(input("welk getal?"))
                break
            except ValueError: 
                print("voer getal 1 in in")
        first_round = False
    else:
        n1 = answer

    while True:
        try:   
            n2 = float(input("voer getal 2 in"))
            break
        except ValueError:
            print("voer een getal in")

    if functie == "A":
        print(f"{functie} getallen optellen")
        answer = functions.addition(n1, n2)
    
    elif functie == "B":
        print(f"{functie} getallen aftrekken")
        print(functions.subtraction(n1, n2))

    elif functie == "C":
        print(f"{functie} getallen vermenigvuldigen")
        print(functions.multiplication(n1, n2))

    elif functie == "D":
        print(f"{functie} getallen delen")
        print(functions.devision(n1, n2))

    elif functie == "E":
        print(f"{functie} getal ophogen")
        if n2 == "":
            n2 = "1"
        print(functions.addition(n1, n2))

    elif functie == "F":
        print(f"{functie} getal verlagen")
        if n2 == "":
            n2 = "1"
        print(functions.subtraction(n1, n2))

    elif functie == "G":
        n2 = 2
        print(functions.devision(n1, n2))
        
    elif functie == "H":
        print(functions.devision(n1, n2))

    print(f"uikomst = {answer}")