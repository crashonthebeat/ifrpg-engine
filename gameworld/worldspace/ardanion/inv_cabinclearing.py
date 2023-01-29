from gameworld.items.apparel import *
from gameworld.items.boxes import *
from gameworld.items.keyitems import *
from gameworld.items.tools import *
from gameworld.items.tradeitems import *
from gameworld.items.weapons import *
from gameworld.worldspace.ardanion.cabinclearing import *

start_cabin.inventory = {
    armor_chest: 1, cabin_weapon_rack: 1, sword_sheath: 1
}

armor_chest.inventory = {
    player_backpack: 1, leather_tunic: 1, wool_shirt: 1, wool_trousers: 1,
    leather_boots: 1, player_vault_key: 1
}

cabin_weapon_rack.inventory = {steel_longsword: 1}

cabin_loft.inventory = {
    pc_armorchest_key: 1, cork_sandals: 1
}

woodshed.inventory = {
    wood_lever: 2
}

cabin_safe_door.keys = [player_vault_key]
armor_chest.keys = [pc_armorchest_key]