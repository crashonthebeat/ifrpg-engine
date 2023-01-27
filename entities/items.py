from entities.basic import Item

class InteractItem(Item):
    # InteractItems can be interacted with by the player, but cannot be 
    # picked up or moved from the room. 
    pass

class Equipment(Item):
    # These are items that can be picked up and worn or otherwise held. 
    pass

class Consumable(Item):
    # Consumables have a certain number of charges, and are gone when those
    # charges are used. Can be fixed or non-fixed.
    pass

class KeyItem(Item):
    # KeyItems are important items that can unlock doors (hence the key) or
    # are otherwise important for advancing or changing the gamestate.
    pass

class TradeItem(Item):
    # TradeItems are a nice word for trash items, some can be sold, but some
    # are truly useless.
    pass

