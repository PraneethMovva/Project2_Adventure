import json
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python3 game_script.py [map_file]")
    sys.exit()

filename = sys.argv[1]

adventure_map = json.load(open(filename, "r"))

start_map = adventure_map
inventory = []

initial_location = adventure_map[0]
current_place = adventure_map[0]

def show_current_place():
    print(f"> {current_place['name']}")
    print(f"\n{current_place['desc']}")
    if "items" in current_place and len(current_place["items"]) > 0:
        items_in_area = current_place["items"]
        items = ", ".join(items_in_area)
        print(f"\nItems: {items}")
    print(f"\nExits: {' '.join(current_place['exits'].keys())}\n")

def process_input(input_str):
    input_str = input_str.lower().strip()

    verbs_dict = {"go": "move in a direction listed in room exits \n(example: go east) \nYou can also directly enter the direction without using go i.e e for east to go east",
                  "\nget": "pick up an item (example: get controller)",
                  "\nlook": "understand your current location",
                  '\ninventory': "check items in inventory",
                  '\nhelp': "see the commands you can use in the game",
                  '\nquit': "exit/end the game"}

    if input_str.startswith('go'):
        direction = input_str[3:]
        if len(direction) == 0:
            print("Please specify a direction to 'go'.")
        else:
            if direction in current_place['exits']:
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            else:
                print(f"There's no way to go {direction}.")
    elif len(input_str) == 1:
        if input_str.startswith('e'):
            direction = 'east'
            if direction in current_place['exits']:
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('w'):
            direction = 'west'
            if direction in current_place['exits']:
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('n'):
            direction = 'north'
            if direction in current_place['exits']:
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            else:
                print(f"There's no way to go {direction}.")
        elif input_str.startswith('s'):
            direction = 'south'
            if direction in current_place['exits']:
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            else:
                print(f"There's no way to go {direction}.")
    elif input_str.startswith('get'):
        item_name = input_str[4:]
        if len(inventory) == 6:
            print("Your inventory is full, you cannot carry more than 6 items.")
            pass
        elif len(item_name) == 0:
            print("Please specify an item to 'get'.")
        else:
            if 'items' in current_place and item_name in current_place['items']:
                current_place['items'].remove(item_name)
                inventory.append(item_name)
                print(f'You pick up the {item_name}.')
            else:
                print(f"There's no {item_name} here.")
    elif input_str == 'inventory' or input_str == 'inv' or input_str == 'i':
        if len(inventory) == 0:
            print("You're not carrying anything.")
        else:
            inv_str = ", ".join(inventory)
            print("Inventory:")
            for item in inventory:
                print(f"  {item}")
    elif input_str.startswith("drop"):
        item_name = input_str[5:]
        if len(item_name) == 0:
            print("Please specify an item to 'drop'.")
        else:
            if item_name in inventory:
                if "items" in current_place:
                    current_place['items'].append(item_name)
                    inventory.remove(item_name)
                    print(f'You drop the {item_name}.')
                else:
                    current_place['items'] = [item_name]
            else:
                print(f"There's no {item_name} in your inventory.\n")
    elif input_str.startswith("look"):
        show_current_place()
    elif input_str.startswith("help"):
        print("You can use the following commands: \n")
        for key, value in verbs_dict.items():
            print(key, ":", value)
    else:
        print('I don\'t understand that. Please enter a valid command.')

game_active = True
place_count = 0

while game_active:
    if place_count == 0:
        show_current_place()
        place_count += 1
    try:
        action = input('What would you like to do? ')
        if re.match(re.compile(r'quit', re.IGNORECASE), action.lower().strip()):
            break
        new_place = process_input(action)
        if new_place:
            current_place = new_place
            show_current_place()

    except (EOFError):
        print("\nType 'quit' to exit.")
        pass

print("Goodbye!")