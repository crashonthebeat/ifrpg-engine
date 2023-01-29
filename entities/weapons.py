from entities.items import Item

class Weapon(Item):
    def __init__(self, name, pl_name, itemsize, hands, combat_style, weap_type):
        Item.__init__(self, name, pl_name, itemsize)
        self.hands = hands
        self.combat_style = combat_style  # Type of Melee, Type of Ranged
        self.weap_type = weap_type  # Sword, Mace, Club, Bow, etc.
        self.entity_type = 'weapon'
        self.use_case='weapon'

class Longsword(Weapon):
    def __init__(self, name, pl_name):
        Weapon.__init__(self, name, pl_name, itemsize=10, hands=2, combat_style='melee', weap_type='sword')
        self.entity_type = 'med_melee_weapon'

class Woodaxe(Weapon):
    def __init__(self, name, pl_name):
        Weapon.__init__(self, name, pl_name, itemsize=10, hands=2, combat_style='melee', weap_type='axe')
        self.entity_type = 'med_melee_weapon'