from entities.items import InteractItem

class Button(InteractItem):
    def __init__(self, name, states, usable):
        InteractItem.__init__(self, name, states, usable, current_state=1)
        self.name = name
        self.item_name = name

class Switch(InteractItem):
    def __init__(self, name, states, current_state, usable):
        InteractItem.__init__(self, name, states, current_state, usable)
        self.name = name
        self.item_name = name

class Slot(InteractItem):
    # This is an interactitem that needs a specific item in order to 
    # be activated.
    def __init__(self, name, states, current_state, usable):
        InteractItem.__init__(self, name, states, current_state, usable)
        self.name = name
        self.item_name = name