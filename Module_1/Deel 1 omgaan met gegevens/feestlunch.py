
from termcolor import colored, cprint, COLORS

prijs_croissantje = float(input ("hoeveel kost een croissant?"))
prijs_stokbroden = float(input ("hoeveel kost een stokbrood?"))
kortingsbon = float(input ("hoeveel korting geeft een kortingbon in euro's."))

aantalcroisant = int(input ("hoeveel croissanten?\n"))
aantalstokbrood = int(input ("hoeveel stokbroden?\n"))
aantalkortingsbonnen = int(input ("hoeveel kortingsbonnen\n"))

kost = (prijs_croissantje * aantalcroisant) + (prijs_stokbroden * aantalstokbrood) - (kortingsbon * aantalkortingsbonnen)

print (f"De feestlunch kost je bij de bakker {colored(kost, 'green')} euro voor de {colored(aantalcroisant, 'red')} croissantjes en de {colored(aantalstokbrood, 'blue')} stokbroden als de {colored(aantalkortingsbonnen, 'yellow')} kortingsbonnen nog geldig zijn!")

