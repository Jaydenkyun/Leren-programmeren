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
functie = input("kies:").upper()



while True:
    try:
        n1 = float(input("welk getal?"))
        break
    except ValueError: 
        print("voer een getal in")
while True:
    try:   
        n2 = float(input(f"welk getal wil je optellen bij {n1}\n"))
        break
    except ValueError:
        print("voer een getal in")
        
if functie == "I" or "":
    print("einde berekening")
    exit()

elif functie == "A":
    print(f"{functie} getallen optellen")
    print(functions.addition(n1, n2))
   
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