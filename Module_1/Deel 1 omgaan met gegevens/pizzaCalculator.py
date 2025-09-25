#Jayden van der Pennen, opdracht: pizza calculator

small_pizza_prijs = 6.50
medium_pizza_prijs = 9.30
large_pizza_prijs = 11.10



pizza_aantal_small = float(input("hoeveel small pizza's wilt u\n"))
pizza_aantal_medium = float(input("hoeveel medium pizza's wilt u\n"))
pizza_aantal_large = float(input("hoeveel large pizza's wilt u\n"))

pizza_small_kosten = (small_pizza_prijs) * (pizza_aantal_small)
pizza_medium_kosten = (medium_pizza_prijs) * (pizza_aantal_medium)
pizza_large_kosten = (large_pizza_prijs) * (pizza_aantal_large)

(pizza_kosten_totaal) = (pizza_small_kosten) + (pizza_medium_kosten) + (pizza_large_kosten)

print("***************** KASSA BON *****************")
print(f"pizza's small       {pizza_aantal_small} x {small_pizza_prijs:.2f} = {pizza_small_kosten:.2f} ") 
print(f"pizza's medium      {pizza_aantal_medium} x {medium_pizza_prijs:.2f} = {pizza_medium_kosten:.2f}")
print(f"pizza's large     {pizza_aantal_large} x {large_pizza_prijs:.2f} = {pizza_large_kosten:.2f}")
print("----------------------------------------------")
print(f"te betalen                      {pizza_kosten_totaal:.2f}")
# ik had chat gpt moeten inschakelen om de uitkomst in twee tekens achter de komma te krijgen