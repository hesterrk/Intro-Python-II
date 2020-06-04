# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

# Capability to add `Item`s to the player's inventory that player picks up in method below
        self.items = []


# Add ability for player to pick up item

    def add_play_item(self, item):

        self.items.append(item)
        # Need to remove the item from the players current room
        self.current_room.items.remove(item)

    def drop_play_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)

    def __str__(self):
        return (f'Your items are: {self.items}')

    def change_room(self, new_room):
        self.current_room = new_room

    def show_items(self):
        if len(self.items) == 0:
            print('No items')
            return

        for i in self.items:
            print(i)
