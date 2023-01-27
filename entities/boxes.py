from entities.basic import Item

class Box(Item):
    # Boxes are anything that has an internal inventory. A player and a room
    # can both be a box, as they both have inventories. Boxes can also 
    # contain other inventories.
    def __init__(self, name):
        Item.__init__(self, name)
        self.inventory = {}
        self.isbox = True

class Holster(Box):
    # Holsters are boxes that have a specific slot for one type of item. 
     def __init__(self, name):
        Box.__init__(self, name)

