from functions import *

# De flow van je programma
def main():
    print("Rekenprogramma")

    a = get_input("Geef het eerste getal: ")
    b = get_input("Geef het tweede getal: ")

    keuze = input("Kies operatie (+, -, *, /): ")

    if keuze == "+":
        result = add(a, b)
    elif keuze == "-":
        result = subtract(a, b)
    elif keuze == "*":
        result = multiply(a, b)
    elif keuze == "/":
        result = divide(a, b)
    else:
        print("Ongeldige keuze")
        return

    show_result(result)

# voer de flow uit
if __name__ == "__main__":
    main()