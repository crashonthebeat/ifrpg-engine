from entities.basic import Item

class InteractItem(Item):
    # InteractItems can be interacted with by the player, but cannot be 
    # picked up or moved from the room. 
    def __init__(self, name, states, current_state, usable):
        Item.__init__(self, name, pl_name=False)
        self.itemfunction = False  # What the item does
        self.itemtype = ''  # Button, Lever, Switch, etc.
        self.states = states  # How many positions the item can be in.
        self.current_state: current_state  # Current position of item
        # Default state of an interactable should be 1 unless the
        # puzzle or function needs otherwise.
        self.usable = usable  # Whether the item can be interacted with
        # One state is just a momentary pushbutton or switch
        # More states would be like a switch, lever or a dial.
        self.item_name = name
        # The actual name will be overwritten with the item's state.


class Apparel(Item):
    # These are items that can be picked up and worn or otherwise held. 
    def __init__(self, name, pl_name, primary_slot):
        Item.__init__(self, name, pl_name)
        self.primary_slot = primary_slot
        self.occupied_slots = {}
        self.entity_type = 'apparel'
        # Occupied slots are a dict of body slots and the layer they
        # occupy, so that a person can't wear two pieces of armor that
        # both cover the chest, for example, but they can wear a shirt
        # and/or tunic with the armor. See apparel.py for a list of slots.


class Tool(Item):
    def __init__(self, name, pl_name, use_case, hands, use_hands):
        Item.__init__(self, name, pl_name)
        self.use_case = use_case  # What the tool does
        self.hands = hands  # How many hands does this item take to hold.
        self.use_hands = use_hands  # How many more hands to use the item
        # Ex. hold a bow in one hand, need both hands to shoot.
        self.entity_type = 'tool'

class Consumable(Item):
    # Consumables have a certain number of charges, and are gone when those
    # charges are used. Can be fixed or non-fixed.
    pass


class KeyItem(Item):
    # KeyItems are important items that can unlock doors (hence the key) or
    # are otherwise important for advancing or changing the gamestate.
    # They are unique.
    def __init__(self, name):
        Item.__init__(self, name, pl_name=False)


class TradeItem(Item):
    # TradeItems are a nice word for trash items, some can be sold, but some
    # are truly useless.
    def __init__(self, name, pl_name):
        Item.__init__(self, name, pl_name)

