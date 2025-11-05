import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
sleutel = False



som_getal_1 =random.randint(10,25)
som_getal_2 =random.randint(-5,75)
operator_list = ["+","-","x"]
operator = random.choice(operator_list)

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f"Daarboven zie je een som staan {som_getal_1} {operator} {som_getal_2} =")
antwoord = int(input('Wat toets je in?\n'))

if antwoord == eval(f"{som_getal_1}{operator}{som_getal_2}"):
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel = True
else:
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')


zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()


# === [kamer 3] === #
lootpool_kamer3 = ["schild","zwaard"]
item = random.choice(lootpool_kamer3)
if item == ("schild"):
    player_defense += 1
else:
    player_attack +=2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)


# === [kamer 4] === #
BOSS_zombie_attack = 2
BOSS_zombie_defense = 0
BOSS_zombie_health = 3
print(f'Dapper loop je de kamer binnen met jouw nieuwe {item}.')
print('Je loopt tegen een zombie aan.')

BOSS_zombie_hit_damage = (zombie_attack - player_defense)
if BOSS_zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    BOSS_zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - BOSS_zombie_defense)
    player_attack_amount = math.ceil(BOSS_zombie_health / player_hit_damage)

    if player_attack_amount < BOSS_zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')



if sleutel == True:
    print("je opent de kist en hebt gewonnen!!!")
else:
    print("je kan de kist niet openen dus je hebt verloren")