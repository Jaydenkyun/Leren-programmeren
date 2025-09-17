from termcolor import colored, cprint, COLORS
toegangsticket = 7.45
mensen = 5
vr5minuten = 0.37
totaalvrminuten = 45
minuten5 = totaalvrminuten/5
totaalvrminuten = 45
vriendendelen = 2
kosten = (toegangsticket * mensen) + (vr5minuten * minuten5) / vriendendelen


print(f"Dit geweldige dagje-uit met {colored(mensen, 'green')} mensen in de Speelhal met {colored(totaalvrminuten, 'blue')} minuten VR kost je maar {colored(kosten, 'red')} euro per persoon voor {colored(vriendendelen, 'yellow')}  mensen")