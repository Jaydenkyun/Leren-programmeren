import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_rupee_amount = 0
sleutel = False
# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print("je loopt een nieuwe kamer in.")
print("je kijkt de kamer rond en ziet een rupee op de grond liggen")
print("je pakt de ruppee op")
player_rupee_amount += 1
print("verderop zie je een deur en er is een deur rechts van je ")
print("pak je de deur recht voor je of de deur rechts van je")
deur_keuze1 = input("kies je de deur voor je typ(1) kies je de deur rechts van je typ(2)")

if deur_keuze1 == "1":

    # === [kamer 2] === #

    som_getal_1 = random.randint(10, 25)
    som_getal_2 = random.randint(-5, 75)
    operator_list = ["+", "-", "*"]
    operator = random.choice(operator_list)

    print ('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print ('Het standbeeld heeft een sleutel vast.')
    print ('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print (f'Daarboven zie je een som staan {som_getal_1}{operator}{som_getal_2}=?')
    antwoord = int(input('Wat toets je in?'))

    if antwoord == eval(f"{som_getal_1}{operator}{som_getal_2}"):
        print('Het stadbeeld laat de sleutel vallen en je pakt het op')
        sleutel = True
    else:
        print('Er gebeurt niets....')

    print('Je zie een 2 deuren achter het standbeeld.')
    print('deur 1 lijd naar de kamer achter het standbeeld en deur 2 lijd naar de kamer rechts van jouw')
    deur_keuze2 = input('welke deur kies je?')
    print('')
    time.sleep(1)

    if deur_keuze2 == "1":
    # === [kamer 6] === #
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2
        print('Je duwt hem open en stap een donkere kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        else:
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            player_health -= zombie_attack * player_attack_amount
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            print('')
            time.sleep(1)




        # === [kamer 3] === #


    print('Je stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
    print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
    print("je krijgt de kans om wat te komen van jouw ene rupee en toevallig kost het zwaard een rupee en het schild een rupee dus je krijgt de keus: koop jij het zwaard? koop jij het schild? of koop je helemaal niets en loop je door?")
    shop_items_keuze = input("typ: (schild) of (zwaard) of (geen) als je geen wapen wilt kopen ")
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

    if shop_items_keuze == "schild":
        player_rupee_amount -= 1
        player_defense += 1
    elif shop_items_keuze == "zwaard":
        player_rupee_amount -= 1
        player_attack += 2
    else:
        player_attack += 0
        print("je bent nu officieël een jood")
else:
    print('Je stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
    print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
    print("je krijgt de kans om wat te komen van jouw ene rupee en toevallig kost het zwaard een rupee en het schild een rupee dus je krijgt de keus: koop jij het zwaard? koop jij het schild? of koop je helemaal niets en loop je door?")
    shop_items_keuze = input("typ: (schild) of (zwaard) of (geen) als je geen wapen wilt kopen ")
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

    if shop_items_keuze == "schild":
        player_rupee_amount -= 1
        player_defense += 1
    elif shop_items_keuze == "zwaard":
        player_rupee_amount -= 1
        player_attack += 2
    else:
        player_attack += 0
        print("je bent nu officieël een jood")

# === [kamer 4] === #

boss_attack = 2
boss_defense = 0
boss_health = 3
print(f'Dapper loop je de kamer binnen met je nieuwe {shop_items_keuze}.')
print('Je ziet de dungeon boss staan.')

boss_hit_damage = (boss_attack - player_defense)
if boss_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de boss, hij kan je geen schade doen.')
else:
    boss_attack_amount = math.ceil(player_health / boss_hit_damage)
    
    player_hit_damage = (player_attack - boss_defense)
    player_attack_amount = math.ceil(boss_health / player_hit_damage)

    if player_attack_amount < boss_attack_amount:
        player_health -= boss_attack * player_attack_amount
        print(f'In {player_attack_amount} rondes versla je de boss.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de boss te sterk voor je.')
        print('Game over.')
        print("titel einde")
        exit()
print('')
time.sleep(1)


# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel == True:
    print ("je opent de kist en je hebt gewonnen!!!")
else:
    print ("je hebt geen sleutel dus je kan de kist niet openen en ook niet winnen")