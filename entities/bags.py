# A bag is both an apparel and a box, like a backpack or pouch
# All containers share layer 6

from entities.boxes import Box, Rack
from entities.items import Apparel

class Backpack(Box, Apparel):
    def __init__(self, name, primary_slot='back'):
        Apparel.__init__(self, name, pl_name='bags', itemsize=20, primary_slot='back')
        self.primary_slot = primary_slot
        self.inventory = {}
        self.occupied_slots = {
            'back': 6, 'l_shldr': 6, 'r_shldr': 6, 
        }
        self.isbox = True
        self.locked = False
        self.list_desc = f"in {self.name}"

class Sheath(Rack, Apparel):
    def __init__(self, name, item_type, slots, size_limit, primary_slot='belt', itemsize=10):
        Apparel.__init__(self, name, pl_name='bags', itemsize=10, primary_slot='belt')
        Rack.__init__(self, name, item_type, slots, size_limit)
        self.entity_type = 'apparel sheath'
        self.inventory = {}
        self.occupied_slots = {
            'belt': 40
        }
        self.fixed = False
        self.list_desc = f'sheathed in {self.name}'
