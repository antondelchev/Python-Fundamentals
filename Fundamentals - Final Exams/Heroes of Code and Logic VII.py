n = int(input())
heroes = {}

for _ in range(n):
    name, hp, mp = input().split(" ")
    hp = int(hp)
    mp = int(mp)

    heroes[name] = {'HP': hp, 'MP': mp}

data = input()

while not data == "End":
    data = data.split(" - ")
    command = data[0]
    chosen_hero = data[1]

    if command == "CastSpell":
        mp_needed = int(data[2])
        spell_name = data[3]

        if heroes[chosen_hero]['MP'] >= mp_needed:
            heroes[chosen_hero]['MP'] -= mp_needed
            print(f"{chosen_hero} has successfully cast {spell_name} and now has {heroes[chosen_hero]['MP']} MP!")
        else:
            print(f"{chosen_hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage_taken = int(data[2])
        attacker_name = data[3]

        if heroes[chosen_hero]['HP'] - damage_taken > 0:
            heroes[chosen_hero]['HP'] -= damage_taken
            print(f"{chosen_hero} was hit for {damage_taken} "
                  f"HP by {attacker_name} and now has {heroes[chosen_hero]['HP']} HP left!")
        else:
            print(f"{chosen_hero} has been killed by {attacker_name}!")
            heroes.pop(chosen_hero)

    elif command == "Recharge":
        amount_mp = int(data[2])

        if heroes[chosen_hero]['MP'] + amount_mp <= 200:
            print(f"{chosen_hero} recharged for {amount_mp} MP!")
            heroes[chosen_hero]['MP'] += amount_mp
        else:
            print(f"{chosen_hero} recharged for {200 - heroes[chosen_hero]['MP']} MP!")
            heroes[chosen_hero]['MP'] = 200

    elif command == "Heal":
        amount_hp = int(data[2])

        if heroes[chosen_hero]['HP'] + amount_hp <= 100:
            print(f"{chosen_hero} healed for {amount_hp} HP!")
            heroes[chosen_hero]['HP'] += amount_hp
        else:
            print(f"{chosen_hero} healed for {100 - heroes[chosen_hero]['HP']} HP!")
            heroes[chosen_hero]['HP'] = 100

    data = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))

for el in sorted_heroes:
    print(f"{el[0]}")
    print(f"  HP: {el[1]['HP']}")
    print(f"  MP: {el[1]['MP']}")
