from entities.items import Apparel

# This will be a list of apparel templates for ease of creation.

# Apparel Slots:
# 'head', 'face', 'neck', 'back', 'chest', 'torso', 'hands' 
# 'l_shldr', 'r_shldr', 'l_arm', 'r_arm', 'l_wrist', 'r_wrist'
# 'hips', 'l_thgh', 'r_thgh', 'l_calf', 'r_calf', 'ankles', 'feet'

# Layer Explanations:
# Layer 1: Undergarments
# Layer 2: Shirt, Tights
# Layer 3: Overshirt, Sweater, Trousers
# Layer 4: Jacket, Tunic, Armor, Boots
# Layer 5: Robe, Over-Tunic, Cape/Cloak
# Layer 6: Container(can share layer space)

class Tunic(Apparel):
    def __init__(self, name, pl_name, primary_slot='torso'):
        Apparel.__init__(self, name, pl_name, primary_slot='torso')
        self.primary_slot = primary_slot
        self.occupied_slots = {
            'l_shldr': 4, 'r_shldr': 4, 
            'chest': 4, 'torso': 4, 'hips': 4
        }

class Shirt(Apparel):
    def __init__(self, name, pl_name, primary_slot='torso'):
        Apparel.__init__(self, name, pl_name, primary_slot='torso')
        self.primary_slot = primary_slot
        self.occupied_slots = {
            'l_shldr': 2, 'r_shldr': 2, 'l_arm': 2, 'r_arm': 2, 
            'l_wrist': 2, 'r_wrist': 2, 'chest': 2, 'torso': 2,
        }

class Trousers(Apparel):
    def __init__(self, name, pl_name, primary_slot='legs'):
        Apparel.__init__(self, name, pl_name, primary_slot='legs')
        self.primary_slot = primary_slot
        self.occupied_slots = {
            'hips': 3, 'l_thgh': 3, 'r_thgh': 3, 
            'l_calf': 3, 'r_calf': 3, 'ankles': 3
        }

class Boots(Apparel):
    def __init__(self, name, pl_name, primary_slot='feet'):
        Apparel.__init__(self, name, pl_name, primary_slot='feet')
        self.primary_slot = primary_slot
        self.occupied_slots = {
            'ankles': 4, 'feet': 4
        }

class Shoes(Apparel):
    def __init__(self, name, pl_name, primary_slot='feet'):
        Apparel.__init__(self, name, pl_name, primary_slot='feet')
        self.primary_slot = primary_slot
        self.occupied_slots = {
            'feet': 4
        }