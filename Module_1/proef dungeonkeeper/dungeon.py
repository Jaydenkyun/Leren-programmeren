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
ruppee_kans = random.randint(1,10)
print("je loopt een nieuwe kamer in.")
if ruppee_kans ==2:
    print("verderop zie je een deur links van je en er is een deur rechts van je ")
    print("pak je de deur links voor je of de deur rechts van je")
    deur_keuze1 = input("kies je de deur links van je typ(1) kies je de deur rechts van je typ(2)")

else:
    print("je ziet een rupee op de grond liggen en pakt hem op")
    player_rupee_amount += 1
    print("verderop zie je een deur links van je en er is een deur rechts van je ")
    print("pak je de deur links voor je of de deur rechts van je")
    deur_keuze1 = input("kies je de deur links van je typ(1) kies je de deur rechts van je typ(2)")

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
        print('Het stadbeeld laat een rupee vallen en je pakt het op')
        player_rupee_amount +=1
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
            print("de zombie dropt een rupee")
            player_rupee_amount +=1
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            print('')
            time.sleep(1)
            exit()

        print("je kijkt even rond na dat jij de zombie had verslagen")
        print("je ziet een deur voor je en een deur rechts van je")
        deur_keuze_zombiekamer = input("neem jij de deur (voor) je of neem jij de deur (rechts) van je")
        if deur_keuze_zombiekamer == "voor":
                # === [kamer 3] === #
            print('Je stapt een hele lange kamer binnen.')
            print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
            print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
            print("je krijgt de kans om wat te komen van jouw ene rupee en toevallig kost het zwaard een rupee en het schild een rupee dus je krijgt de keus: koop jij het zwaard? koop jij het schild? of koop je helemaal niets en loop je door?")
            if player_rupee_amount == 0:
              print("het zit er naaruit dat jij geeen rupees hebt en dus ook niets kunt kopen")

            elif player_rupee_amount == 1:
               shop_items_keuze = input("typ: (schild) of (zwaard) of (geen) als je geen wapen wilt kopen")
            elif player_rupee_amount == 2:
                shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
            elif player_rupee_amount == 3:
              shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
            elif player_rupee_amount == 4:
              shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (alles) of (geen) als je geen wapen wilt kopen")
    
            print('Op naar de volgende deur.')
            print('')
            time.sleep(1)

            if shop_items_keuze == "schild":
                player_rupee_amount -= 1
                player_defense += 1
            elif shop_items_keuze == "zwaard":
                player_rupee_amount -= 1
                player_attack += 2
            elif shop_items_keuze == "beide":
                player_rupee_amount -= 2
                player_defense += 1
                player_attack_amount += 2
            elif shop_items_keuze == "sleutel":
                player_rupee_amount -= 2
                sleutel = True
            elif shop_items_keuze == "alles":
                player_rupee_amount -=4
                player_defense += 1
                player_attack_amount +=2
                sleutel = True
            else:
                shop_items_keuze == "geen"
                player_attack += 0
            print("je koopt niets en bent nu officieël een jood")
            time.sleep(1)

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

    # === [kamer 8] === #
    dobbelsteen_uitkomst = random.randint(2,12)
    print("je komt een nieuwe kamer.")
    print("in deze kamer staat een goblin in kleermakers zit op de vloer en hij grijnst naar je.")
    print("hij zegt dat hij de Gamble goblin heet en hij zegt dat jouw leven in zijn handen zit.")
    print("vervolgens pakt hij twee zeszijdige dobbelstenen uit zijn zak en zegt als jij hoger dan zeven gooit dan krijg jij een extra ruppee")
    print("maar als jij lager dan zeven gooit dan mag ik jouw een keertje steken met een grijns 0^0")
    print("je pakt de dobbelstenen en rolt ze over de grond heen")
    if dobbelsteen_uitkomst == 7:
        print("de goblin kijkt geschokt en zegt EEN ZEVEN DAT IS NIET DE BEDOELING hij begint te tweaken.")
        print("hij sprint op jouw af met een mes en jij ontwijkt zijn aanval en slaat hem hard op zijn achterhoofd.")
        print("hij despawned en hij dropt een Ruppee en een healt potion jij neemt de ruppee mee en de healt potion in en loopt verder")
        player_rupee_amount +=1
        player_health +=4
    elif dobbelsteen_uitkomst > 7:
        print(f"je rolt een {dobbelsteen_uitkomst} en de goblin zegt goed dan en hij geeft jouw een ruppee")
        player_rupee_amount += 1
    elif dobbelsteen_uitkomst < 7:
        player_health -= 1
        print(f"dat is nou jammer een {dobbelsteen_uitkomst} en hij steekt jouw in je zij een verdwijnt")
    time.sleep(1)


        # === [kamer 9] === #
    altaar_lijst =["schild"," hart "]
    altaar_kans = random.choice(altaar_lijst)
    print("je stapt een donkere kamer binnen met een altaar in het midden dat licht geeft")
    print("je legt jouw hand op het altaar en het begint heftiger te schijnen ")
    print(f"er begint een vorm van een {altaar_kans} te vormen op het altaar ")
    if altaar_kans == "schild":
        print("je wordt betoverd en jouw defense is verhoogd")
        player_defense += 1
    else:
        print("je wordt betoverd en jouw gezondheid is verhoogd")




        # === [kamer 3] === #


    print('Je stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
    print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
    print("je krijgt de kans om wat te komen van jouw ene rupee en toevallig kost het zwaard een rupee en het schild een rupee dus je krijgt de keus: koop jij het zwaard? koop jij het schild? of koop je helemaal niets en loop je door?")
    if player_rupee_amount == 0:
        print("het zit er naaruit dat jij geeen rupees hebt en dus ook niets kunt kopen")

    elif player_rupee_amount == 1:
        shop_items_keuze = input("typ: (schild) of (zwaard) of (geen) als je geen wapen wilt kopen")
    elif player_rupee_amount == 2:
        shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
    elif player_rupee_amount == 3:
        shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
    elif player_rupee_amount == 4:
        shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (alles) of (geen) als je geen wapen wilt kopen")
    
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

    if shop_items_keuze == "schild":
        player_rupee_amount -= 1
        player_defense += 1
    elif shop_items_keuze == "zwaard":
        player_rupee_amount -= 1
        player_attack += 2
    elif shop_items_keuze == "beide":
        player_rupee_amount -= 2
        player_defense += 1
        player_attack_amount += 2
    elif shop_items_keuze == "sleutel":
        player_rupee_amount -= 2
        sleutel = True
    elif shop_items_keuze == "alles":
        player_rupee_amount -=4
        player_defense += 1
        player_attack_amount +=2
        sleutel = True
    else:
        shop_items_keuze == "geen"
        player_attack += 0
        print("je koopt niets en bent nu officieël een jood")
else:
    # === [kamer 8] === #
    dobbelsteen_uitkomst = random.randint(2,12)
    print("je komt een nieuwe kamer.")
    print("in deze kamer staat een goblin in kleermakers zit op de vloer en hij grijnst naar je.")
    print("hij zegt dat hij de Gamble goblin heet en hij zegt dat jouw leven in zijn handen zit.")
    print("vervolgens pakt hij twee zeszijdige dobbelstenen uit zijn zak en zegt als jij hoger dan zeven gooit dan krijg jij een extra ruppee")
    print("maar als jij lager dan zeven gooit dan mag ik jouw een keertje steken met een grijns 0^0")
    print("je pakt de dobbelstenen en rolt ze over de grond heen")
    if dobbelsteen_uitkomst == 7:
        print("de goblin kijkt geschokt en zegt EEN ZEVEN DAT IS NIET DE BEDOELING hij begint te tweaken.")
        print("hij sprint op jouw af met een mes en jij ontwijkt zijn aanval en slaat hem hard op zijn achterhoofd.")
        print("hij despawned en hij dropt een Ruppee en een healt potion jij neemt de ruppee mee en de healt potion in en loopt verder")
        player_rupee_amount +=1
        player_health +=4
    elif dobbelsteen_uitkomst > 7:
        print(f"je rolt een {dobbelsteen_uitkomst} en de goblin zegt goed dan en hij geeft jouw een ruppee")
        player_rupee_amount += 1
    elif dobbelsteen_uitkomst < 7:
        player_health -= 1
        print(f"dat is nou jammer een {dobbelsteen_uitkomst} en hij steekt jouw in je zij een verdwijnt")
        time.sleep(1)

        # === [kamer 9] === #
altaar_lijst =["schild"," hart "]
altaar_kans = random.choice (altaar_lijst)
print("je stapt een donkere kamer binnen met een altaar in het midden dat licht geeft")
print("je legt jouw hand op het altaar en het begint heftiger te schijnen ")
print(f"er begint een vorm van een {altaar_kans} te vormen op het altaar ")
if altaar_kans == "schild":
    print("je wordt betoverd en jouw defense is verhoogd")
    player_defense += 1
else:
    print("je wordt betoverd en jouw gezondheid is verhoogd")
time.sleep(1)

        
    # === [kamer 3] === #
print('Je stapt een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een bord waarop staat zwaard en schild te koop.')
print(f'Achter het bord staat een goblin die aan jouw vraagt of jij iets zou willen kopen.')
print("je krijgt de kans om wat te komen van jouw ene rupee en toevallig kost het zwaard een rupee en het schild een rupee dus je krijgt de keus: koop jij het zwaard? koop jij het schild? of koop je helemaal niets en loop je door?")
if player_rupee_amount == 0:
    print("het zit er naaruit dat jij geeen rupees hebt en dus ook niets kunt kopen")

elif player_rupee_amount == 1:
    shop_items_keuze = input("typ: (schild) of (zwaard) of (geen) als je geen wapen wilt kopen")
elif player_rupee_amount == 2:
    shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
elif player_rupee_amount == 3:
    shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (geen) als je geen wapen wilt kopen")
elif player_rupee_amount == 4:
    shop_items_keuze = input("typ: (schild) of (zwaard) of (zwaard en schild) of (sleutel) of (alles) of (geen) als je geen wapen wilt kopen")
    
print('Op naar de volgende deur.')
print('')
time.sleep(1)

if shop_items_keuze == "schild":
    player_rupee_amount -= 1
    player_defense += 1
elif shop_items_keuze == "zwaard":
    player_rupee_amount -= 1
    player_attack += 2
elif shop_items_keuze == "beide":
    player_rupee_amount -= 2
    player_defense += 1
    player_attack_amount += 2
elif shop_items_keuze == "sleutel":
    player_rupee_amount -= 2
    sleutel = True
elif shop_items_keuze == "alles":
    player_rupee_amount -=4
    player_defense += 1
    player_attack_amount +=2
    sleutel = True
else:
    shop_items_keuze == "geen"
    player_attack += 0
    print("je koopt niets en bent nu officieël een jood")
    time.sleep(1)

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