# Project2_Adventure

## Name: Praneeth Movva       (CWID: 20022864)
## Login: pmovva1@stevens.edu

## Git URL: https://github.com/PraneethMovva/Project2_Adventure

## I have spent around 23 - 28 hours on this project out of which I have spent around 14 hours debugging the code to get it right in the AutoGrader and the rest implementing the code

## How I tested my code:
I have first created a map file that is similar to the one that professor has provided and based on that I have created a class Game and started to implement my baseline features after implementing the baseline features I have used the terminal to run the command (python (filename.py) (filename.map)) that is python adventure.py asset.map to run and see how my code was behaving and debugged the errors. Then I have uploaded into my git repo and tried it in AutoGrader where only 2 test cases were passed and had to change the code again and test everything. Later I have started to do the extensions and followed a similar pattern to test and debugg

## Any Known Bugs:
Currently there are no known bugs. The program is working fine

## An example of difficult issue and how I resolved it:
The difficult issue is definitely getting it right in the AutoGrader I have resubmitted several times I have to change the entire code several times to get it right in there. The baseline features were working fine whenever I started to add in the extensions the AutoGrader isn't passing the testcases especially with the help extension being reflective. And also when implementing the extensions I have implemented both Abbrevation for verbs, directions and items and also directions become verbs when implementing both of these simultaneously I had encountered several bugs where only one of it was getting accepted and other one is getting bugs then I found out what is the problem and created a separate variable for direction as verbs and solved it.

## List Of Extensions:
I have implemented a total of 4 extensions.
1. Abbreviations for verbs, directions, and items:
You can implement this extension by just typing go no(go north), get cons(get console) etc. These can be pretty convinient when playing the game. Below are few examples of this extension
```
python adventure.py asset.map
> Gaming Room

You are in a Gaming Room.

Items: controller, console

Exits: north east

What would you like to do? go ea
You go east.

> Common Area

A Common area nothing fancy here!

Exits: north west

What would you like to do? go no
You go north.

> Cafeteria/Lounge

You are in a Cafeteria and Lounge area where you can get food or relax.

Items: coffee, popcorn, ice-cream

Exits: west south

What would you like to do? get cof
You pick up the coffee.
What would you like to do?
```

2. Directions become verbs:
You can implement this extension by just typing e (for east), n (for north) etc. Below are few examples of this
```
python adventure.py asset.map
> Gaming Room

You are in a Gaming Room.

Items: controller, console

Exits: north east

What would you like to do? n
You go north.

> Restroom

You are in a Restroom.

Exits: east south

What would you like to do? e
You go east.

> Cafeteria/Lounge

You are in a Cafeteria and Lounge area where you can get food or relax.

Items: coffee, popcorn, ice-cream

Exits: west south

What would you like to do?
```

3. A drop verb:
This extension can be helpful to drop an item which we picked up from a room. If there is no item to drop it just says you don't have anything to drop. You can implement this by typing drop (item_name). Below is an example of this.
```
python adventure.py asset.map
> Gaming Room

You are in a Gaming Room.

Items: controller, console

Exits: north east

What would you like to do? get console
You pick up the console.
What would you like to do? look
> Gaming Room

You are in a Gaming Room.

Items: controller

Exits: north east

What would you like to do? drop cons
You drop the console.
What would you like to do? look
> Gaming Room

You are in a Gaming Room.

Items: controller, console

Exits: north east

What would you like to do?
```

4. A help verb:
Help verb can be very useful to anyone who doesn't know about the game and what commands does it have and also these commands are used to advance through the game. And help being reflective can be very useful whenever there are new verbs. Below is an example of help command.
```
python adventure.py asset.map
> Gaming Room

You are in a Gaming Room.

Items: controller, console

Exits: north east

What would you like to do? help
You can run the following commands:
  go - Move in a direction listed in room exits (e.g., go east)
  get - Pick up an item (e.g., get controller)
  look - Understand the current location
  inventory - Check the items in inventory
  help - Provide a list of available commands
  quit - Exit/end the game

What would you like to do?
```

#### Note: I have implemented 4 extensions but I am not in any group so for grading purpose you can consider the first three extensions i.e.. Abbreviations for verbs, directions, and items, Directions become verbs, and A drop verb extensions.