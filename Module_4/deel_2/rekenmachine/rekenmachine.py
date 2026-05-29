import functions 

print("wat wilt u doen?")
print("A) getallen optellen")
print("B)  getallen aftrekken")
print("C) getallen vermenigvuldigen")
print("D) getallen delen")
print("E) getallen ophogen")
print("F) getallen verlagen")
print("G) getallen verdubbelen")
print("H) getallen halveren")
print("I) niets")
functie = input("kies:")
if functie == "I" or "":
    print("einde berekening")
    exit()
elif functie == "A":
    print(f"{functie} getallen optellen")
    n1 = input("welk getal?")
    n2 = input(f"welk getal wil je optellen bij {n1}\n")
    print(functions.addition(n1, n2))
   
elif functie == "B":
    print(f"{functie} getallen aftrekken")
    n1 = input("welk getal?")
    n2 = input(f"welk getal wil je aftrekken van {n1}\n")
    print(functions.subtraction(n1, n2))

elif functie == "C":
    print(f"{functie} getallen vermenigvuldigen")
    n1 = input("welk getal?")
    n2 = input(f"welk getal wil je vermenigvuldigen met {n1}\n")
    print(functions.multiplication(n1, n2))

elif functie == "D":
    print(f"{functie} getallen delen")
    n1 = input("welk getal?")
    n2 = input(f"welk getal wil je delen van {n1}\n")
    print(functions.devision(n1, n2))

elif functie == "E":
    print(f"{functie} getal ophogen")
    n1 = input("welk getal?")
    n2 = input(f"met hoeveel wil je het getal {n1} ophogen\n")
    if n2 == "":
        n2 = "1"
    print(functions.addition(n1, n2))

elif functie == "F":
    print(f"{functie} getal verlagen")
    n1 = input("welk getal?")
    n2 = input(f"met hoeveel wil je het getal {n1} verlagen\n")
    if n2 == "":
        n2 = "1"
    print(functions.subtraction(n1, n2))

elif functie == "G":
    print(f"{functie} getallen verdubbelen")
    n1 = input("welk getal?")
    n2 = 2
    print(functions.devision(n1, n2))
    
elif functie == "H":
    print(f"{functie} getallen halveren")
    n1 = input("welk getal?")
    n2 = 2
    print(functions.devision(n1, n2))