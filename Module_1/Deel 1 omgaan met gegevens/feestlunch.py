
from termcolor import colored, cprint, COLORS

croissantje = 0.39
stokbroden = 2.78
kortingsbonnen = -0.50
aantalcroisant = 17
aantalstokbrood = 2
aantalkortingsbonnen = 3
kost = (croissantje * aantalcroisant) + (stokbroden * aantalstokbrood) + (kortingsbonnen * aantalkortingsbonnen)

print (f"De feestlunch kost je bij de bakker {colored(kost, 'green')} euro voor de {colored(aantalcroisant, 'red')} croissantjes en de {colored(aantalstokbrood, 'blue')} stokbroden als de {colored(aantalkortingsbonnen, 'yellow')} kortingsbonnen nog geldig zijn!")

