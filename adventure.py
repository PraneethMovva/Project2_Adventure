# import sys
# import json

# game_map = {}

# # Check if mapper file is passed as an argument with the Python file or raise an exception
# arg_length = len(sys.argv)
# if arg_length < 2:
#     raise Exception('Invalid usage. Please provide the mapper file as an argument: python3 adventure.py (mapper_file.txt)')

# # Function that defines how to read the mapper file into game_map
# def load(argv):
#     global game_map
#     try:
#         with open(argv[1], 'r') as file:
#             game_map = json.load(file)
#     except Exception as e:
#         print(f'ERROR: {e}')
#         sys.exit()

# def get_data_of_room(room):
#     length = len(game_map)
#     if length > room >= 0:
#         return game_map[room]
#     else:
#         print(f'The room with index {room} does not exist in the map.')
#         return None

# def look(room):
#     room_data = get_data_of_room(room)
#     if room_data is None:
#         return
#     room_name = room_data.get('name')
#     dsc = room_data.get('desc')
#     str = " ".join(room_data['exits'].keys())
#     print(f'> {room_name}\n')
#     print(f'{dsc}\n')
#     if room_data.get('items') is not None and len(room_data.get('items')) != 0:
#         itm_str = ", ".join(room_data['items'])
#         print('Items: ' + itm_str + '\n')
#     print('Exits: ' + str + '\n')

# def observe_room(room_index):
#     room_data = get_data_of_room(room_index)
#     if room_data is None:
#         return
#     room_name = room_data.get('name')
#     description = room_data.get('desc')
#     exits_str = ", ".join(room_data['exits'].keys())
    
#     print(f'> {room_name}\n')
#     print(f'{description}\n')
    
#     if room_data.get('items') and room_data['items']:
#         items_str = ", ".join(room_data['items'])
#         print('Items: ' + items_str + '\n')
    
#     print('Exits: ' + exits_str + '\n')

# def show_inventory():
#     if len(current_inventory) == 0:
#         print('You\'re not carrying anything.')
#     else:
#         print('Inventory:')
#         for item in current_inventory:
#             print(f'  {item}')

# # Defining first room as current
# current_room = 0
# current_inventory = []
# items = []
# directions = []

# def update_available_directions():
#     global directions
#     for room in game_map:
#         exits = room.get('exits')
#         if exits:
#             for direction in exits.keys():
#                 if direction not in directions:
#                     directions.append(direction)

# def update_available_items():
#     global items
#     for room in game_map:
#         room_items = room.get('items')
#         if room_items:
#             for item in room_items:
#                 if item not in items:
#                     items.append(item)

# def observe_current_room():
#     observe_room(current_room)

# def start_game():
#     global current_room
#     observe_current_room()

#     while True:
#         try:
#             user_input = input("What would you like to do? ")
#         except KeyboardInterrupt as e:
#             raise e
#         except EOFError:
#             print('Use \'quit\' to exit.')
#             continue

#         arguments = user_input.strip().lower().split()
#         length = len(arguments)

#         if length == 0:
#             continue

#         matched_verbs = verb_match(arguments[0])
#         verb_count = len(matched_verbs)

#         if verb_count == 0:
#             print('Invalid input.')
#             continue
#         else:
#             if verb_count == 1:
#                 verb = matched_verbs[0]
#                 if verb_list[verb]['params']:
#                     verb_list[verb]['func'](arguments)
#                 else:
#                     verb_list[verb]['func']()
#                 continue
#             else:
#                 matched_verbs_str = list_join(matched_verbs, " or ")
#                 print(f"Did you want to {matched_verbs_str} ?")
#                 continue

# def verb_match(string_input):
#     verb_matches = []
#     for verbe in verb_list:
#         if verbe == string_input:
#             return [verbe]
#         else:
#             if string_input in verbe:
#                 verb_matches.append(verbe)
#     return verb_matches

# def input_match(string_input, options_valid):
#     verb_matches = []
#     leng = len(options_valid)
#     if options_valid is None or leng == 0:
#         return verb_matches
#     for verbe in options_valid:
#         if verbe == string_input:
#             return [verbe]
#         else:
#             if string_input in verbe:
#                 verb_matches.append(verbe)
#     return verb_matches

# def list_join(liste, iden):
#     strr = ", ".join(liste[:-1]).rstrip()
#     return strr + iden + liste[-1]

# def look_present_room():
#     look(current_room)

# def help():
#     print('You can run the following commands:')
#     for verb in verb_list:
#         print(verb, ' : ', verb_list.get(verb).get('desc'))

# def get_item_from_room(item_name, room_name):
#     global current_inventory
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if item_name in data_of_room.get('items'):
#             current_inventory.append(item_name)
#             game_map[room_name]['items'].remove(item_name)
#             print(f"You pick up the {item_name}.")
#         else:
#             print(f"There is no {item_name} anything.")
#     else:
#         return

# def drop_item_in_room(item_name, room_name):
#     global current_inventory
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if item_name in current_inventory:
#             current_inventory.remove(item_name)
#             game_map[room_name].setdefault('items', []).append(item_name)
#             print(f"You drop the {item_name}.")
#         else:
#             print(f"You aren't carrying a {item_name}.")
#     else:
#         return

# def game_quit_now():
#     print('Goodbye!')
#     sys.exit()

# def next_room_go(dir, room_name):
#     global current_room
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if dir in data_of_room.get('exits'):
#             current_room = data_of_room.get('exits').get(dir)
#             print(f'You go {dir}.\n')
#             look_present_room()
#         else:
#             print(f"There's no way to go {dir}.")
#     else:
#         return

# def next_room_go_utils(args):
#     if len(args) != 2:
#         print(f'Sorry, you need to \'go\' somewhere.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         matched_directions = input_match(args[1], room_data.get('exits'))
#         if len(matched_directions) == 0:
#             print(f'There\'s no way to go {args[1]}.')
#             return
#         else:
#             if len(matched_directions) > 1:
#                 current_items = list_join(matched_directions, " or ")
#                 print(f'Did you want to get the {current_items} ?')
#                 return
#             next_room_go(matched_directions[0], current_room)

# def item_get_utils(args):
#     if len(args) != 2:
#         print('Sorry, you need to \'get\' something.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         curr_items = room_data.get('items')
#         try:
#             curr_items = list(filter(lambda i: i not in current_inventory, room_data.get('items')))
#         except:
#             pass
#         matched_items = input_match(args[1], curr_items)
#         if len(matched_items) == 0:
#             print(f'There\'s no {args[1]} anywhere.')
#             return
#         else:
#             if len(matched_items) > 1:
#                 current_items = list_join(matched_items, " or the ")
#                 print(f'Did you want to get the {current_items} ?')
#                 return
#             get_item_from_room(matched_items[0], current_room)

# def item_drop_utils(args):
#     if len(args) != 2:
#         print('Sorry, you need to \'drop\' something.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         matched_items = input_match(args[1], current_inventory)
#         if len(matched_items) == 0:
#             print(f'There\'s no {args[1]} in inventory.')
#             return
#         else:
#             if len(matched_items) > 1:
#                 current_items = list_join(matched_items, " or the ")
#                 print(f'Did you want to drop the {current_items} ?')
#                 return
#             drop_item_in_room(matched_items[0], current_room)

# verb_list = {
#     'go': {
#         'func': next_room_go_utils,
#         'params': True,
#         'desc': 'go <direction>. tries to go in the specified direction <direction> room from the current room.'
#     },
#     'help': {
#         'func': help,
#         'params': False,
#         'desc': 'keeps track of what the verbs in the game are and prints them'
#     },
#     'look': {
#         'func': look_present_room,
#         'params': False,
#         'desc': 'show which room the person is in right now'
#     },
#     'get': {
#         'func': item_get_utils,
#         'params': True,
#         'desc': 'get <item>. lets a player pick the item <item> that is in the room'
#     },
#     'inventory': {
#         'func': show_inventory,
#         'params': False,
#         'desc': 'shows the player what they are carrying'
#     },
#     'quit': {
#         'func': game_quit_now,
#         'params': False,
#         'desc': 'should exit the game. Also, sending an interrupt should end the game immediately'
#     },
#     'drop': {
#         'func': item_drop_utils,
#         'params': True,
#         'desc': 'take the item <item> from your inventory and put it down in the room'
#     }
# }

# # Load the map and start the game
# load(sys.argv)
# update_available_directions()
# update_available_items()
# start_game()








# import sys
# import json

# game_map = {}

# # Check if mapper file is passed as an argument with the Python file or raise an exception
# arg_length = len(sys.argv)
# if arg_length < 2:
#     raise Exception('Invalid usage. Please provide the mapper file as an argument: python3 adventure.py (mapper_file.txt)')

# # Function that defines how to read the mapper file into game_map
# def load(argv):
#     global game_map
#     try:
#         with open(argv[1], 'r') as file:
#             game_map = json.load(file)
#     except Exception as e:
#         print(f'ERROR: {e}')
#         sys.exit()

# def verb_match(string_input):
#     verb_matches = []
#     for verbe in verb_list:
#         if verbe == string_input:
#             return [verbe]
#         else:
#             if string_input in verbe:
#                 verb_matches.append(verbe)
#     return verb_matches

# def input_match(string_input, options_valid):
#     verb_matches = []
#     leng = len(options_valid)
#     if options_valid is None or leng == 0:
#         return verb_matches
#     for verbe in options_valid:
#         if verbe == string_input:
#             return [verbe]
#         else:
#             if string_input in verbe:
#                 verb_matches.append(verbe)
#     return verb_matches

# def list_join(liste, iden):
#     strr = ", ".join(liste[:-1]).rstrip()
#     return strr + iden + liste[-1]

# def show_inventory():
#     if len(current_inventory) == 0:
#         print('You\'re not carrying anything.')
#     else:
#         print('Inventory:')
#         for item in current_inventory:
#             print(f'  {item}')

# # Defining first room as current
# current_room = 0
# current_inventory = []
# items = []
# directions = []

# def update_available_directions():
#     global directions
#     for room in game_map:
#         exits = room.get('exits')
#         if exits:
#             for direction in exits.keys():
#                 if direction not in directions:
#                     directions.append(direction)

# def update_available_items():
#     global items
#     for room in game_map:
#         room_items = room.get('items')
#         if room_items:
#             for item in room_items:
#                 if item not in items:
#                     items.append(item)

# def observe_current_room():
#     observe_room(current_room)

# def start_game():
#     global current_room
#     observe_current_room()

#     while True:
#         try:
#             user_input = input("What would you like to do? ")
#         except KeyboardInterrupt as e:
#             raise e
#         except EOFError:
#             print('Use \'quit\' to exit.')
#             continue

#         arguments = user_input.strip().lower().split()
#         length = len(arguments)

#         if length == 0:
#             continue

#         matched_verbs = verb_match(arguments[0])
#         verb_count = len(matched_verbs)

#         if verb_count == 0:
#             print('Invalid input.')
#             continue
#         else:
#             if verb_count == 1:
#                 verb = matched_verbs[0]
#                 if verb_list[verb]['params']:
#                     verb_list[verb]['func'](arguments)
#                 else:
#                     verb_list[verb]['func']()
#                 continue
#             else:
#                 matched_verbs_str = list_join(matched_verbs, " or ")
#                 print(f"Did you want to {matched_verbs_str} ?")
#                 continue

# def look_present_room():
#     look(current_room)

# def help():
#     print('You can run the following commands:')
#     for verb in verb_list:
#         print(verb, ' : ', verb_list.get(verb).get('desc'))

# def get_data_of_room(room):
#     length = len(game_map)
#     if length > room >= 0:
#         return game_map[room]
#     else:
#         print(f'The room with index {room} does not exist in the map.')
#         return None

# def look(room):
#     room_data = get_data_of_room(room)
#     if room_data is None:
#         return
#     room_name = room_data.get('name')
#     dsc = room_data.get('desc')
#     str = " ".join(room_data['exits'].keys())
#     print(f'> {room_name}\n')
#     print(f'{dsc}\n')
#     if room_data.get('items') is not None and len(room_data.get('items')) != 0:
#         itm_str = ", ".join(room_data['items'])
#         print('Items: ' + itm_str + '\n')
#     print('Exits: ' + str + '\n')

# def observe_room(room_index):
#     room_data = get_data_of_room(room_index)
#     if room_data is None:
#         return
#     room_name = room_data.get('name')
#     description = room_data.get('desc')
#     exits_str = ", ".join(room_data['exits'].keys())
    
#     print(f'> {room_name}\n')
#     print(f'{description}\n')
    
#     if room_data.get('items') and room_data['items']:
#         items_str = ", ".join(room_data['items'])
#         print('Items: ' + items_str + '\n')
    
#     print('Exits: ' + exits_str + '\n')

# def get_item_from_room(item_name, room_name):
#     global current_inventory
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if item_name in data_of_room.get('items'):
#             current_inventory.append(item_name)
#             game_map[room_name]['items'].remove(item_name)
#             print(f"You pick up the {item_name}.")
#         else:
#             print(f"There is no {item_name} anything.")
#     else:
#         return

# def drop_item_in_room(item_name, room_name):
#     global current_inventory
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if item_name in current_inventory:
#             current_inventory.remove(item_name)
#             game_map[room_name].setdefault('items', []).append(item_name)
#             print(f"You drop the {item_name}.")
#         else:
#             print(f"You aren't carrying a {item_name}.")
#     else:
#         return

# def game_quit_now():
#     print('Goodbye!')
#     sys.exit()

# def next_room_go(dir, room_name):
#     global current_room
#     data_of_room = get_data_of_room(room_name)
#     if data_of_room is not None:
#         if dir in data_of_room.get('exits'):
#             current_room = data_of_room.get('exits').get(dir)
#             print(f'You go {dir}.\n')
#             look_present_room()
#         else:
#             print(f"There's no way to go {dir}.")
#     else:
#         return

# def next_room_go_utils(args):
#     if len(args) != 2:
#         print(f'Sorry, you need to \'go\' somewhere.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         matched_directions = input_match(args[1], room_data.get('exits'))
#         if len(matched_directions) == 0:
#             print(f'There\'s no way to go {args[1]}.')
#             return
#         else:
#             if len(matched_directions) > 1:
#                 current_items = list_join(matched_directions, " or ")
#                 print(f'Did you want to get the {current_items} ?')
#                 return
#             next_room_go(matched_directions[0], current_room)

# def item_get_utils(args):
#     if len(args) != 2:
#         print('Sorry, you need to \'get\' something.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         curr_items = room_data.get('items')
#         try:
#             curr_items = list(filter(lambda i: i not in current_inventory, room_data.get('items')))
#         except:
#             pass
#         matched_items = input_match(args[1], curr_items)
#         if len(matched_items) == 0:
#             print(f'There\'s no {args[1]} anywhere.')
#             return
#         else:
#             if len(matched_items) > 1:
#                 current_items = list_join(matched_items, " or the ")
#                 print(f'Did you want to get the {current_items} ?')
#                 return
#             get_item_from_room(matched_items[0], current_room)

# def item_drop_utils(args):
#     if len(args) != 2:
#         print('Sorry, you need to \'drop\' something.')
#         return
#     room_data = get_data_of_room(current_room)
#     if room_data is None:
#         return
#     else:
#         matched_items = input_match(args[1], current_inventory)
#         if len(matched_items) == 0:
#             print(f'There\'s no {args[1]} in inventory.')
#             return
#         else:
#             if len(matched_items) > 1:
#                 current_items = list_join(matched_items, " or the ")
#                 print(f'Did you want to drop the {current_items} ?')
#                 return
#             drop_item_in_room(matched_items[0], current_room)

# verb_list = {
#     'go': {
#         'func': next_room_go_utils,
#         'params': True,
#         'desc': 'go <direction>. tries to go in the specified direction <direction> room from the current room.'
#     },
#     'help': {
#         'func': help,
#         'params': False,
#         'desc': 'keeps track of what the verbs in the game are and prints them'
#     },
#     'look': {
#         'func': look_present_room,
#         'params': False,
#         'desc': 'show which room the person is in right now'
#     },
#     'get': {
#         'func': item_get_utils,
#         'params': True,
#         'desc': 'get <item>. lets a player pick the item <item> that is in the room'
#     },
#     'inventory': {
#         'func': show_inventory,
#         'params': False,
#         'desc': 'shows the player what they are carrying'
#     },
#     'quit': {
#         'func': game_quit_now,
#         'params': False,
#         'desc': 'should exit the game. Also, sending an interrupt should end the game immediately'
#     },
#     'drop': {
#         'func': item_drop_utils,
#         'params': True,
#         'desc': 'take the item <item> from your inventory and put it down in the room'
#     }
# }

# # Load the map and start the game
# load(sys.argv)
# update_available_directions()
# update_available_items()
# start_game()





#You go {direction} not working
import sys
import json

game_map = {}

#check if mapper file is passed as argument with the python file or raise exception
num_args = len(sys.argv)

if num_args < 2:
    raise Exception('Invalid usage. Please provide the mapper file as an argument: python3 adventure.py (mapper_file.txt)')

#function that defines how to read the mapper file into game_map
def load(argv):
    global game_map
    try:
        with open(argv[1], 'r') as file:
            game_map = json.load(file)
    except Exception as error:
        print(f'ERROR: {error}')
        sys.exit()

# Defining first room as current
current_room = 0
current_inventory = []
available_items = []
possible_directions = []

def update_possible_directions():
    global possible_directions
    for room in game_map:
        exits = room.get('exits')
        if exits:
            for direction in exits.keys():
                if direction not in possible_directions:
                    possible_directions.append(direction)

def update_possible_items():
    global available_items
    for room in game_map:
        room_items = room.get('items')
        if room_items:
            for item in room_items:
                if item not in available_items:
                    available_items.append(item)

def display_inventory():
    if not current_inventory:
        print("You're not carrying anything.")
    else:
        print('Inventory:')
        for item in current_inventory:
            print(f'  {item}')

def get_room_data(room_index):
    map_length = len(game_map)
    if 0 <= room_index < map_length:
        return game_map[room_index]
    else:
        print(f'The room with index {room_index} does not exist in the map.\n')
        return None

def observe_room(room_index):
    room_data = get_room_data(room_index)
    if room_data is None:
        return
    room_name = room_data.get('name')
    description = room_data.get('desc')
    exits_str = ", ".join(room_data['exits'].keys())
    
    print(f'> {room_name}\n')
    print(f'{description}\n')
    
    if room_data.get('items') and room_data['items']:
        items_str = ", ".join(room_data['items'])
        print('Items: ' + items_str + '\n')
    
    print('Exits: ' + exits_str + '\n')

def observe_current_room():
    observe_room(current_room)

def display_help():
    print('You can use the following commands:')
    for verb, details in verb_list.items():
        print(f'{verb}: {details["desc"]}')

def pick_up_item(item_name, room_index):
    global current_inventory, game_map

    room_data = get_room_data(room_index)

    if room_data is not None:
        items_in_room = room_data.get('items', [])

        if item_name in items_in_room:
            current_inventory.append(item_name)
            items_in_room.remove(item_name)
            print(f"You pick up the {item_name}.")
        else:
            print(f"There is no {item_name} in this room.")
    else:
        return

def drop_item(item_name, room_index):
    global current_inventory, game_map

    room_data = get_room_data(room_index)

    if room_data is not None:
        if item_name in current_inventory:
            current_inventory.remove(item_name)
            game_map[room_index].setdefault('items', []).append(item_name)
            print(f"You drop the {item_name}.")
        else:
            print(f"You aren't carrying a {item_name}.")
    else:
        return

def quit_game():
    print('Goodbye!')
    sys.exit(0)

def move_to_next_room(direction, current_room):
    global present_room

    room_data = get_room_data(current_room)

    if room_data is not None:
        exits = room_data.get('exits', {})

        if direction in exits:
            present_room = exits[direction]
            print(f'You go {direction}.\n')
            observe_current_room()
        else:
            print(f"There's no way to go {direction}.")
    else:
        return
    
def get_data_of_room(room):
    leng = len(game_map)
    if leng > room >= 0:
        return game_map[room]
    else:
        print(f'The room with index {room} does not exist in the map.')
        return None

def input_match(string_input, options_valid):
    verb_matches = []
    leng = len(options_valid)
    if options_valid is None or leng == 0:
        return verb_matches
    for verbe in options_valid:
        if verbe == string_input:
            return [verbe]
        else:
            if string_input in verbe:
                verb_matches.append(verbe)
    return verb_matches

def list_join(liste, iden):
    strr = ", ".join(liste[:-1]).rstrip()
    return strr + iden + liste[-1]

def look(room):
    room_data = get_data_of_room(room)
    
    if room_data is None:
        return

    room_name = room_data.get('name')
    description = room_data.get('desc')
    exits = room_data.get('exits', {})

    print(f'> {room_name}\n')
    print(f'{description}\n')

    if 'items' in room_data and room_data['items']:
        items_str = ', '.join(room_data['items'])
        print(f'Items: {items_str}\n')

    if exits:
        exits_str = ', '.join(exits.keys())
        print(f'Exits: {exits_str}\n')

def look_present_room():
    look(current_room)

def handle_next_room_go(args):
    if len(args) != 2:
        print("Sorry, you need to 'go' somewhere.")
        return

    global current_room

    room_data = get_data_of_room(current_room)

    if room_data is not None:
        matched_directions = input_match(args[1], room_data.get('exits'))

        if len(matched_directions) == 0:
            print(f"There's no way to go {args[1]}.")
            return

        if len(matched_directions) > 1:
            current_items = list_join(matched_directions, " or ")
            print(f'Did you want to go {current_items}?')
            return

        next_direction = matched_directions[0]

        if next_direction in room_data['exits']:
            current_room = room_data['exits'][next_direction]
            look_present_room()
        else:
            print(f"There's no way to go {next_direction}.")
    else:
        print(f"Invalid room: {current_room}.")

def handle_item_get(args):
    if len(args) != 2:
        print("Sorry, you need to 'get' something.")
        return

    room_data = get_room_data(current_room)
    
    if room_data is None:
        return

    current_items = room_data.get('items', [])

    try:
        current_items = list(filter(lambda item: item not in current_inventory, current_items))
    except Exception:
        pass

    matched_items = match_input_to_options(args[1], current_items)

    if len(matched_items) == 0:
        print(f"There's no {args[1]} anywhere.")
        return

    if len(matched_items) > 1:
        current_items_str = join_list_with_separator(matched_items, " or the ")
        print(f"Did you want to get the {current_items_str}?")
        return

    pick_up_item(matched_items[0], current_room)

def handle_item_drop(args):
    if len(args) != 2:
        print("Sorry, you need to 'drop' something.")
        return

    room_data = get_room_data(current_room)
    
    if room_data is None:
        return

    matched_items = match_input_to_options(args[1], current_inventory)

    if len(matched_items) == 0:
        print(f"There's no {args[1]} in inventory.")
        return

    if len(matched_items) > 1:
        current_items_str = join_list_with_separator(matched_items, " or the ")
        print(f"Did you want to drop the {current_items_str}?")
        return

    drop_item(matched_items[0], current_room)

verb_list = {
    'go': {
        'func': handle_next_room_go,
        'params': True,
        'desc': 'go <direction>. Tries to go in the specified direction <direction> to the next room from the current room.'
    },
    'help': {
        'func': display_help,
        'params': False,
        'desc': 'Keeps track of what the verbs in the game are and prints them.'
    },
    'look': {
        'func': observe_current_room,
        'params': False,
        'desc': 'Shows which room the person is in right now.'
    },
    'get': {
        'func': handle_item_get,
        'params': True,
        'desc': 'get <item>. Lets a player pick up the item <item> that is in the room.'
    },
    'inventory': {
        'func': display_inventory,
        'params': False,
        'desc': 'Shows the player what they are carrying.'
    },
    'quit': {
        'func': quit_game,
        'params': False,
        'desc': 'Should exit the game. Also, sending an interrupt should end the game immediately.'
    },
    'drop': {
        'func': handle_item_drop,
        'params': True,
        'desc': 'Take the item <item> from your inventory and put it down in the room.'
    }
}

def find_matching_verbs(user_input):
    matching_verbs = [verb for verb in verb_list if verb == user_input or user_input in verb]
    return matching_verbs

def match_input_to_options(user_input, valid_options):
    matched_options = []
    options_length = len(valid_options)

    if valid_options is None or options_length == 0:
        return matched_options

    for option in valid_options:
        if option == user_input:
            return [option]
        elif user_input in option:
            matched_options.append(option)

    return matched_options

def join_list_with_separator(items_list, separator):
    concatenated_str = ", ".join(items_list[:-1]).rstrip()
    return concatenated_str + separator + items_list[-1]

def play_game():
    global current_room
    observe_current_room()

    while True:
        try:
            user_input = input("What would you like to do? ")
        except KeyboardInterrupt as e:
            raise e
        except EOFError:
            print('Use \'quit\' to exit.')
            continue

        arguments = user_input.strip().lower().split()
        length = len(arguments)

        if length == 0:
            continue

        matched_verbs = find_matching_verbs(arguments[0])
        verb_count = len(matched_verbs)

        if verb_count == 0:
            print('Invalid input.')
            continue
        else:
            if verb_count == 1:
                verb = matched_verbs[0]
                if verb_list[verb]['params']:
                    verb_list[verb]['func'](arguments)
                else:
                    verb_list[verb]['func']()
                continue
            else:
                matched_verbs_str = join_list_with_separator(matched_verbs, " or ")
                print(f"Did you want to {matched_verbs_str} ?")
                continue


load(sys.argv)
update_possible_directions()
update_possible_items()
play_game()
