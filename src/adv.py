from room import Room
from player import Player
from item import Item


# Note: formatting text (room desc, look at textwrap module might be useful here: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/).


def show_welcome_message():
    welcome_message = "Welcome to Adventure Game!"
    print(welcome_message)


# Declare all the rooms
# This dict holds many instances (objects) of Room
# This key references the instance of new Room object created from room class
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# Because the key in room dict creates a new instance of room (object) we can access the directions attributed by dot notation (just like we do for a method)

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Creating new instances of items

items = {
    "apple": Item("apple", "nice apple"),
    "orange": Item("orange", "nice organge"),
    "banana": Item("banana", "nice banana"),
    "avocado": Item("avocado", "nice avo"),
    "passionfruit": Item("passionFruit", "nice passionfruit"),

}

# Func for player getting and dropping items from room


def select_item_room(player, room):

    response = input(
        'Do you want to take or drop items from this room?: take: take item or drop: drop item, nothing: no nothing:  ')

    verb, obj = response.split(' ')

    # 1)  check if room has item
    # 2) if item present call add_play_item func (player)

    # for i in room.items:
    if verb == 'take':
        if items[obj] in player.current_room.items:
            player.add_play_item(items[obj])
            player.show_items()

        elif items[obj] not in player.current_room.items:
            print('item doesnt exist in your room')

    elif verb == 'drop':
        if items[obj] not in player.current_room.items:
            player.drop_play_item(items[obj])
            player.show_items()

    elif verb == 'nothing':
        print('You Can Continue...!')


# Add item objects to rooms using method from rooms class so it stores it in memory on class
room['outside'].add_room_item(items["apple"])
room['foyer'].add_room_item(items['orange'])
room['overlook'].add_room_item(items['banana'])
room['narrow'].add_room_item(items['avocado'])
room['treasure'].add_room_item(items['passionfruit'])


#
# Main
#
# Start of Game
show_welcome_message()

# Variables

lost_way = 'You have Lost your way!!'

# Make a new player object that is currently in the 'outside' room.
# Passing in a key from the dict that refers a specific instance (object) of Room that was created

name = input('What is your name? ')

new_player = Player(name, room['outside'])

initial_room = new_player.current_room

print(initial_room)


# Showing user list of their items upon inputting 'i' into input
# should return zero or empty array because no adding functionality added yet

def get_items_of_player(player):
    response = input("Press i to see your items you hold:  ")

    if len(response) == 1 and 'i':
        # if response == 'i':
        player.show_items()

    else:
        print('Wrong Command!!!')


# User input directions
user_input = input(
    'Enter Your cardinal direction. Your options are: "n": "North", "s": "South", "e": "East", "w": "West" :  ')

# Write a loop that:

while user_input != 'q':
    if user_input == 'n':
        new_room = new_player.current_room.n_to

        # no room associated with this direction
        if new_room == None:
            print(lost_way)
            print(new_player.current_room)

        else:
            # assign new location to player by calling method in player class to update current room attribute on class
            new_player.change_room(new_room)
            print(new_player.current_room)
            print(new_player.current_room.room_items())

    elif user_input == 's':
        new_room = new_player.current_room.s_to
        # no room associated with this direction
        if new_room == None:
            print(lost_way)
            print(new_player.current_room)

        else:
            # assign new location to player by calling method in player class to update current room attribute on class
            new_player.change_room(new_room)
            print(new_player.current_room)
            print(new_player.current_room.room_items())

    elif user_input == 'e':
        new_room = new_player.current_room.e_to
        # no room associated with this direction
        if new_room == None:
            print(lost_way)
            print(new_player.current_room)

        else:
            # assign new location to player by calling method in player class to update current room attribute on class
            new_player.change_room(new_room)
            print(new_player.current_room)
            print(new_player.current_room.room_items())

    elif user_input == 'w':
        new_room = new_player.current_room.w_to
        # no room associated with this direction
        if new_room == None:
            print(lost_way)
            print(new_player.current_room)

        else:
            # assign new location to player by calling method in player class to update current room attribute on class
            new_player.change_room(new_room)
            print(new_player.current_room)
            print(new_player.current_room.room_items())

    get_items_of_player(new_player)
    select_item_room(new_player, new_room)
    user_input = input(
        'Enter Your cardinal direction. Your options are: "n": "North", "s": "South", "e": "East", "w": "West" :  ')


if user_input == 'q':
    print('you have quitted the game, see you soon')
