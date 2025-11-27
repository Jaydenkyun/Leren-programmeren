import time, math, random

player_attack = 1
player_defense = 0
player_health = 5
player_rupee_amount = 0
sleutel = False

# ========================================
# KAMER 1
# ===========================================
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
input("Typ enter om door te gaan...")

# ===========================================
# KAMER 7
# ========================================
ruppee_kans = random.randint(1,10)
print("Je loopt een nieuwe kamer in (kamer 7).")

if ruppee_kans == 2:
    print("Verderop zie je een deur links van je en een deur rechts van je.")
else:
    print("Je ziet een rupee op de grond liggen en pakt hem op.")
    player_rupee_amount += 1
    print("Verderop zie je een deur links van je en een deur rechts van je.")

print("Typ (1) om naar kamer 2 te gaan")
print("Typ (2) om naar kamer 8 te gaan")
deur_keuze1 = input("Keuze: ")
if deur_keuze1 == "1":
    # ==========================================
    # KAMER 2
    # ===========================================

    som_getal_1 = random.randint(10, 25)
    som_getal_2 = random.randint(-5, 75)
    operator_list = ["+", "-", "*"]
    operator = random.choice(operator_list)

    print ('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print ('Het standbeeld heeft een rupee vast.')
    print ('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    print (f'Daarboven zie je een som staan: {som_getal_1}{operator}{som_getal_2} = ?')
    antwoord = int(input('Wat toets je in? '))

    if antwoord == eval(f"{som_getal_1}{operator}{som_getal_2}"):
        print('Het standbeeld laat een rupee vallen en je pakt het op.')
        player_rupee_amount += 1
    else:
        print('Er gebeurt niets...')

    print('Je ziet twee deuren een achter het standbeeld en de andere rechts van je.')
    print('Typ (1) om naar de kamer te gaan achter het standbeeld.')
    print('Typ (2) om naar kamer te gaan rechts van je.')
    deur_keuze2 = input('Keuze: ')
    if deur_keuze2 == "1":
    # ===========================================
    # KAMER 6
    # =========================================
   
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2

        print('Je duwt de deur open en stapt een donkere kamer binnen.')
        print('Je loopt tegen een zombie aan!')

        zombie_hit_damage = max(0, zombie_attack - player_defense)
        player_hit_damage = max(1, player_attack - zombie_defense)

        if zombie_hit_damage == 0:
            print('De zombie kan je geen schade doen.')
            zombie_attack_amount = 9999
        else:
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            player_health -= zombie_hit_damage * player_attack_amount
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print("De zombie dropt een rupee.")
            player_rupee_amount += 1
        else:
            print("Helaas is de zombie te sterk voor je.")
            print("Game over.")
            exit()
        print('Je ziet twee deuren een voor je en de andere rechts van je.')
        print('Typ (1) om naar de kamer te gaan voor je.')
        print('Typ (2) om naar kamer te gaan rechts van je.')
        deur_keuze6 = input('Keuze: ')
        if deur_keuze6 == "1":
            kamer = 3
if deur_keuze1 == "2" or deur_keuze6 != "1" or deur_keuze2 != "1":

    # ===========================================
    # KAMER 8
    # ===========================================
    dobbelsteen_uitkomst = random.randint(2,12)

    print("In deze kamer zit een grijnzende goblin.")
    print("Hij noemt zichzelf de Gamble Goblin.")
    print("hij pakt twee zeszijdige dobbelstenen uit zijn zakken")
    print("Je moet dobbelen zegt hij als jij hoger gooit dan 7 dan krijg jij een ruppee")
    print("gooi jij lager dan een 7 dan...")
    time.sleep(1)
    if dobbelsteen_uitkomst == 7:
        print("Je rolt een 7! De goblin tweaked en valt je aan.")
        print("Je ontwijkt en slaat hem neer. Hij laat een rupee vallen en een health potion.")
        player_rupee_amount += 1
        player_health += 4
    elif dobbelsteen_uitkomst > 7:
        print(f"Je rolt een {dobbelsteen_uitkomst}. en  Je krijgt een rupee.")
        player_rupee_amount += 1
    else:
        print(f"Je rolt een {dobbelsteen_uitkomst}. De goblin steekt je!")
    player_health -= 1
    print("je loopt verder")
    print("Je ziet twee deuren:")
    print("Typ (1) voor kamer 9.")
    print("Typ (2) voor kamer 3.")
    deur_keuze8 = input("Keuze: ")
    if deur_keuze8 == "1":
        if deur_keuze8 == "1":
        # ===========================================
        # KAMER 9
        # ===========================================
            altaar_lijst = ["schild", "hart"]
            altaar_kans = random.choice(altaar_lijst)
            print("Je stapt een donkere kamer binnen met een lichtgevend altaar.")
            print(f"Het licht dat van het altaar afkomt vormt een {altaar_kans}.")
            time.sleep(2)
            if altaar_kans == "schild":
                print("Je wordt betoverd: je defense stijgt.")
                player_defense += 1
            else:
                print("Je wordt betoverd: je gezondheid stijgt.")
                player_health += 1
            kamer = 3
        else:
            kamer = 3

    


    # ===========================================
    # KAMER 3 (MERCHANT ROOM)
    # ===========================================
    print('Je stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
    print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
    time.sleep(1)
    if player_rupee_amount == 0:
        print("Je hebt geen rupees, dus je kunt niks kopen.")
        shop_items_keuze = "geen"
    elif player_rupee_amount == 1:
        shop_items_keuze = input("Typ: (schild), (zwaard), of (geen): ").lower()
    elif player_rupee_amount == 2:
        shop_items_keuze = input("Typ: (schild), (zwaard), (zwaard en schild), (sleutel), of (geen): ").lower()
    elif player_rupee_amount == 3:
        shop_items_keuze = input("Typ: (schild), (zwaard), (zwaard en schild), (sleutel), of (geen): ").lower()
    elif player_rupee_amount == 4:
        shop_items_keuze = input("Typ: (schild), (zwaard), (zwaard en schild), (sleutel), (alles), of (geen): ").lower()

    print("Op naar de volgende deur.")
    time.sleep(1)

    if shop_items_keuze == "schild":
        player_rupee_amount -= 1
        player_defense += 1
    elif shop_items_keuze == "zwaard":
        player_rupee_amount -= 1
        player_attack += 2
    elif shop_items_keuze == "zwaard en schild":
        player_rupee_amount -= 2
        player_defense += 1
        player_attack += 2
    elif shop_items_keuze == "sleutel"and player_rupee_amount >=2:
        player_rupee_amount -= 2
        sleutel = True
    elif shop_items_keuze == "alles" and player_rupee_amount >=4:
        player_rupee_amount -= 4
        player_defense += 1
        player_attack += 2
        sleutel = True
    else:
        print("Je koopt niets.")

    print("Je verlaat de kamer…")
    time.sleep(1)

    # ===========================================
    # KAMER 4 (BOSS)
    # ===========================================
    boss_attack = 2
    boss_defense = 0
    boss_health = 3

    print(f'Dapper loop je de kamer binnen.')
    print('Je ziet de dungeon boss staan.')

    boss_hit_damage = max(0, boss_attack - player_defense)
    player_hit_damage = max(1, player_attack - boss_defense)

    if boss_hit_damage == 0:
        print("De boss kan je geen schade doen!")
        boss_attack_amount = 9999
    else:
        boss_attack_amount = math.ceil(player_health / boss_hit_damage)

    player_attack_amount = math.ceil(boss_health / player_hit_damage)

    if player_attack_amount < boss_attack_amount:
        print(f"In {player_attack_amount} rondes versla je de boss!")
    else:
        print("De boss is te sterk!")
        print("Game over.")
        exit()

    # ===========================================
    # KAMER 5 (EIND)
    # ===========================================
    print("Je ziet een schatkist in het midden van de kamer.")

    if sleutel:
        print("Je opent de kist...")
        print("JE HEBT GEWONNEN!!!")
        print("titel einde: winnaar")
    else:
        print("Je hebt geen sleutel, dus je kunt de kist niet openen.")
        print("Einde van het spel.")
        print("titel einde: sleutel vergeten")

    exit()



