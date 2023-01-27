from entities.rooms import MapRoom
from gameworld.worldspace.cabinclearing import *


### ARDANION ###
ardanion_south = MapRoom("ardanion - south")
ardanion_central = MapRoom("central ardanion")
ardanion_east = MapRoom("ardanion - east")

ardanion_desc = [
    "The region of Ardanion is one of the oldest inhabited regions in Auralia. The region is the homeland for the",
    "Marstalith Elves, the indigenous people of northern Auralia. Ardanion is an ancient forest with large hardwood",
    "trees with spots of Red Maple and Cherry Trees. Here, the Silurian River joins the Celtain River as they run",
    "east to the Alausian Sea.",
    "Other than a few smaller towns and forts, the only major city in Ardanion is Eviscore, one of the great cities",
    "of pre-Imperial times. Since the fall of Thyrathea, Eviscore has retaken its title as the political and cultural",
    "center of Auralia."
]

ardanion_south.desc = ardanion_desc
ardanion_central.desc = ardanion_desc.extend([
    "The great city of Eviscore dominates the landscape, its silver-glass tower rising up from the trees. In it lies",
    "one of the only three ways of crossing the Celtain River in the region, the other two being the bridge along",
    "the Auraclian Way in the east region, and the far-less travelled Toraval bridge."
])
ardanion_east.desc = ardanion_desc

ardanion_south.quick_desc = []
ardanion_central.quick_desc = []
ardanion_east.quick_desc = []

ardanion_south.exits = {
    'north': ardanion_central,
    'northeast': ardanion_east,
}

ardanion_central.exits = {
    'east': ardanion_east,
    'south': ardanion_south
}

ardanion_east.exits = {
    'west': ardanion_central,
    'southwest': ardanion_south
}