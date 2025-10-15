print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
keuze = input('? ')
weer_type = ("niets")

if (keuze == 'a' or 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif (keuze == 'b'):
    weer_type = 'warm'
elif(keuze) == 'd':
    weer_type = 'koud'

if (weer_type) != 'niets':
    print(f'Dus jij houd van {weer_type} weer!')
if keuze not in ('a','b','c','d'):
    print('Dit is geen te kiezen optie!')
