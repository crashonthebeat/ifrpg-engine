from entities.basic import Item

class InteractItem(Item):
    # InteractItems can be interacted with by the player, but cannot be 
    # picked up or moved from the room. 
    pass

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
    pass

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

