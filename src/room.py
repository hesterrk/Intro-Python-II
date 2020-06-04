# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.e_to = None
        self.n_to = None
        self.w_to = None
        self.s_to = None

    # Add the ability to add items to rooms -->  visible to the player when they are in that room.

        self.items = []

    def add_room_item(self, item):
        self.items.append(item)


# Printing and formatting users current room


    def __str__(self):
        return "Your current room is: {}, {}".format(self.name, self.description)

    def room_items(self):
        if len(self.items) == 0:
            print('No items in room')
            return

        for i in self.items:
            return f'Items in this room are: {i.name}'
