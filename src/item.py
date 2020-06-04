
# This will be the _base class_ for specialized item types to be declared later.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '"{}": "{}"'.format(self.name, self.description)

    #  Call this method when the `Item` is picked up by the player, name is name of item

    def on_take(self):
        return 'You have picked up' f"{self.name}"

    #  Add an `on_drop` method to `Item`. Implement it similar to `on_take`

    def on_drop(self):
        print('You have dropped' f"{self.name}")
