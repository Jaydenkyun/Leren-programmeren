from termcolor import colored, cprint, COLORS
toegangsticket = float(input ("hoeveel kost een toegangsticket?"))
mensen = int(input ("hoeveel mensen doen er mee?"))
vr5minuten = float(input ("hoeveel kost het per 5 minuten?"))
totaalvrminuten = int(input ("hoelang duurt het?"))
minuten5 = totaalvrminuten/5
vriendendelen = int(input ("met hoeveel vrienden wil je de kosten delen"))
kosten = (toegangsticket * mensen) + (vr5minuten * minuten5) / vriendendelen


print(f"Dit geweldige dagje-uit met {colored(mensen, 'green')} mensen in de Speelhal met {colored(totaalvrminuten, 'blue')} minuten VR kost je maar {colored(kosten, 'red')} euro per persoon voor {colored(vriendendelen, 'yellow')}  mensen")