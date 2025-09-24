from termcolor import colored, cprint, COLORS
trui = input('welke kleur is de trui? \n ')

if trui == "grijs":
    print (f"de trui is {colored(trui, 'dark_grey',)}")

elif trui == "groen":
    print (f"de trui is {colored(trui, 'green')}")

elif trui == "blauw":
    print (f"de trui is {colored(trui, 'blue')}")

elif trui == "roze":
    print (colored( "je bent een","light_magenta"), colored("twink", "light_magenta", attrs=["bold"]))

else:
    print ('je bent naakt')