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
if functie == "I":
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
    print(function.addition(n1, n2))

    
#elif functie == "C":
    
#elif functie == "D":
    
#elif functie == "E":
    
#elif functie == "F":
    
#elif functie == "G":
    
#elif functie == "H":