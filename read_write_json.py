import json

spells = [
    ["fire", 100, 50],
    ["ice", 50, 70],
    ["water", 10, 100]
]

x = json.dumps(spells)
file = open("spells.json","a")
file.write(x)


def show_spellbook():
    print("<SPELLBOOK>")
    for x in range(len(spells)):
        type = spells[x][0]
        damage = spells[x][1]
        speed = spells[x][2]
        print(f"type: {type} | damage: {damage} | speed: {speed}")  # f-string for clean formatting


def add_spell(type, damage, speed):
    spells.append([type, damage, speed])
    print(f"Spell '{type}' added successfully!")


def remove_spell(type):
    removed = False
    for x in range(len(spells)):
        if spells[x][0] == type:
            spells.pop(x)
            removed = True
            print(f"Spell '{type}' removed.")
            break  # Exit the loop after removal

    if not removed:
        print(f"Spell '{type}' not found in spellbook.")



def run():
    while True:
        print("Pick option:")
        print("1 - Show spells in spellbook")
        print("2 - Add new spell to spellbook")
        print("3 - Remove spell from spellbook")
        option = input("> ")

        # Convert input to integer for safer comparison (optional)
        try:
            option = int(option)
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue  # Skip to the next iteration if input is not a number

        if option == 1:
            show_spellbook()
        elif option == 2:
            type = input("Type > ")
            damage = int(input("Damage > "))  # Convert damage input to integer
            speed = int(input("Speed > "))    # Convert speed input to integer
            add_spell(type, damage, speed)
        elif option == 3:
            type = input("Type > ")
            remove_spell(type)
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


run()
