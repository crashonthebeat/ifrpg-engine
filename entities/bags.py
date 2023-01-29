# A bag is both an apparel and a box, like a backpack or pouch
# All containers share layer 6

from entities.boxes import Box
from entities.items import Apparel

class Backpack(Box, Apparel):
    def __init__(self, name, pl_name, primary_slot='back'):
        Apparel.__init__(self, name, pl_name, primary_slot='back')
        self.primary_slot = primary_slot
        self.inventory = {}
        self.occupied_slots = {
            'back': 6, 'l_shldr': 6, 'r_shldr': 6, 
        }
        self.isbox = True
        self.list_desc = f"in {self.name}"
