import json
import sys
import re

class Game:
    def __init__(self, map_filename):
        self.game_map = json.load(open(map_filename, "r"))
        self.restart_map = self.game_map
        self.player_inventory = []
        self.current_location = self.game_map[0]
        self.valid_verb_dict = {
            "go": "Move in a direction listed in room exits (e.g., go east)",
            "get": "Pick up an item (e.g., get controller)",
            "look": "Understand the current location",
            "inventory": "Check the items in inventory",
            "help": "Provide a list of available commands",
            "quit": "Exit/end the game"
        }

    def generate_help_text(self):
        help_text = "You can run the following commands:\n"
        for key, value in self.valid_verb_dict.items():
            help_text += f"  {key} {value} ...\n" if "..." in value else f"  {key} - {value}\n"
        return help_text

    def show_current_place(self):
        print(f"> {self.current_location['name']}")
        print(f"\n{self.current_location['desc']}")
        if "items" in self.current_location and self.current_location["items"]:
            items = ", ".join(self.current_location["items"])
            print(f"\nItems: {items}")
        print(f"\nExits: {' '.join(self.current_location['exits'].keys())}\n")

    def process_input(self, input_str):
        input_str = input_str.lower().strip()

        if input_str.startswith('go'):
            direction = input_str[3:]
            if not direction:
                print("Sorry, you need to 'go' somewhere.")
            else:
                matching_directions = [d for d in self.current_location['exits'].keys() if d.startswith(direction)]
                if len(matching_directions) == 1:
                    direction = matching_directions[0]
                    new_location_id = self.current_location['exits'][direction]
                    new_location = self.game_map[new_location_id]
                    print(f'You go {direction}.\n')
                    return new_location
                elif len(matching_directions) > 1:
                    print(f"Did you want to go {', '.join(matching_directions)}?")
                else:
                    print(f"There's no way to go {direction}.")

        elif len(input_str) == 1:
            direction_dict = {'e': 'east', 'w': 'west', 'n': 'north', 's': 'south'}
            if input_str in direction_dict:
                direction = direction_dict[input_str]
                if direction in self.current_location['exits']:
                    new_location_id = self.current_location['exits'][direction]
                    new_location = self.game_map[new_location_id]
                    print(f'You go {direction}.\n')
                    return new_location
                else:
                    print(f"There's no way to go {direction}.")
            else:
                print("Invalid direction.")

        elif input_str.startswith('get'):
            item_name = input_str[4:]
            if len(self.player_inventory) == 6:
                print("You cannot carry more than 6 items in your inventory")
                pass
            elif len(item_name) == 0:
                print("Sorry, you need to 'get' something.")
            else:
                matching_items = [item for item in self.current_location.get('items', []) if item.startswith(item_name)]
                if len(matching_items) == 1:
                    item_name = matching_items[0]
                    self.current_location['items'].remove(item_name)
                    self.player_inventory.append(item_name)
                    print(f'You pick up the {item_name}.')
                elif len(matching_items) > 1:
                    print(f"Did you want to get {', '.join(matching_items)}?")
                else:
                    print(f"There's no {item_name} anywhere.")

        elif input_str in {'inventory', 'inv', 'i'}:
            if len(self.player_inventory) == 0:
                print("You're not carrying anything.")
            else:
                inv_str = ", ".join(self.player_inventory)
                print("Inventory:")
                for item in self.player_inventory:
                    print(f"  {item}")

        elif input_str.startswith("drop"):
            item_name = input_str[5:]
            if len(item_name) == 0:
                print("Sorry, you need to 'drop' something.")
            else:
                matching_inventory_items = [item for item in self.player_inventory if item.startswith(item_name)]
                if len(matching_inventory_items) == 1:
                    item_name = matching_inventory_items[0]
                    if "items" in self.current_location:
                        self.current_location['items'].append(item_name)
                        self.player_inventory.remove(item_name)
                        print(f'You drop the {item_name}.')
                    else:
                        self.current_location['items'] = [item_name]
                elif len(matching_inventory_items) > 1:
                    print(f"Did you want to drop {', '.join(matching_inventory_items)}?")
                else:
                    print(f"There's no {item_name} in inventory.\n")

        elif input_str.startswith("look"):
            self.show_current_place()
            
        elif input_str.startswith("help"):
            help_text = self.generate_help_text()
            print(help_text)
        else:
            print('I don\'t understand that enter a valid command.')

    def run_game(self):
        game_running = True
        location_count = 0

        while game_running:
            if location_count == 0:
                self.show_current_place()
                location_count += 1
            try:
                action = input('What would you like to do? ')
                if re.match(re.compile(r'quit', re.IGNORECASE), action.lower().strip()):
                    break
                new_location = self.process_input(action)
                if new_location:
                    self.current_location = new_location
                    self.show_current_place()

            except (EOFError):
                print("\nUse 'quit' to exit.")
                pass

        print("Goodbye!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 program_name.py [map_file]")
        sys.exit()

    filename = sys.argv[1]

    game_instance = Game(filename)
    game_instance.run_game()
