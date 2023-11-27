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

    verbs_dict = {"go": "Move in a direction listed in room exits.\n(Example: go east)\n"
                         "You can also directly enter the direction without using go, i.e., e for east to go east",
                  "get": "Pick up an item (Example: get controller)",
                  "look": "Understand your current location",
                  'inventory': "Check items in inventory",
                  'help': "See the commands you can use in the game",
                  'quit': "Exit/end the game"}

    if input_str.startswith('go'):
        direction = input_str[3:]
        if len(direction) == 0:
            print("Please specify a direction to 'go'.")
        else:
            matching_directions = [d for d in current_place['exits'].keys() if d.startswith(direction)]
            if len(matching_directions) == 1:
                direction = matching_directions[0]
                new_place_id = current_place['exits'][direction]
                new_place = adventure_map[new_place_id]
                print(f'You move {direction}.\n')
                return new_place
            elif len(matching_directions) > 1:
                print(f"Did you want to go {', '.join(matching_directions)}?")
            else:
                print(f"There's no way to go {direction}.")
    elif len(input_str) == 1 and input_str in {'e', 'w', 'n', 's'}:
        direction_dict = {'e': 'east', 'w': 'west', 'n': 'north', 's': 'south'}
        direction = direction_dict[input_str]
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
            print("Your inventory is full. You cannot carry more than 6 items.")
            pass
        elif len(item_name) == 0:
            print("Please specify an item to 'get'.")
        else:
            matching_items = [item for item in current_place.get('items', []) if item.startswith(item_name)]
            if len(matching_items) == 1:
                item_name = matching_items[0]
                current_place['items'].remove(item_name)
                inventory.append(item_name)
                print(f'You pick up the {item_name}.')
            elif len(matching_items) > 1:
                print(f"Did you want to get {', '.join(matching_items)}?")
            else:
                print(f"There's no {item_name} here.")
    elif input_str in {'inventory', 'inv', 'i'}:
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
            matching_inventory_items = [item for item in inventory if item.startswith(item_name)]
            if len(matching_inventory_items) == 1:
                item_name = matching_inventory_items[0]
                if "items" in current_place:
                    current_place['items'].append(item_name)
                    inventory.remove(item_name)
                    print(f'You drop the {item_name}.')
                else:
                    current_place['items'] = [item_name]
            elif len(matching_inventory_items) > 1:
                print(f"Did you want to drop {', '.join(matching_inventory_items)}?")
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

