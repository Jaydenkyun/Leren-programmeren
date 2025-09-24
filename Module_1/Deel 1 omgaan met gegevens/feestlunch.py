
from termcolor import colored, cprint, COLORS

prijs_croissantje = 0.39
prijs_stokbroden = 2.78
kortingsbon = -0.50
aantalcroisant = 17
aantalstokbrood = 2
aantalkortingsbonnen = 3
kost = (prijs_croissantje * aantalcroisant) + (prijs_stokbroden * aantalstokbrood) + (kortingsbon * aantalkortingsbonnen)

print (f"De feestlunch kost je bij de bakker {colored(kost, 'green')} euro voor de {colored(aantalcroisant, 'red')} croissantjes en de {colored(aantalstokbrood, 'blue')} stokbroden als de {colored(aantalkortingsbonnen, 'yellow')} kortingsbonnen nog geldig zijn!")

