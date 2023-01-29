from entities.rooms import Room, Door
from gameworld.worldspace.auralia import ardanion_south

#######################################
### START AREA - THE CABIN CLEARING ###
#######################################
start_cabin = Room("your cabin")
cabin_saferoom = Room("a saferoom")
cabin_loft = Room("cabin loft")
cabin_clearing = Room("outside your cabin")
outhouse = Room("the outhouse")
outhouse_in = Room("inside the outhouse")
woodshed = Room("woodshed")
behind_cabin = Room("behind your cabin")
outdoor_kitchen = Room("A amall eating area")
riverbank_1 = Room("riverbank")
riverbank_2 = Room("riverbank")
forest_path_1 = Room("a path through the forest")
forest_path_2 = Room("a path through the forest")
forest_path_3 = Room("a path through the forest")

cabin_safe_door = Door("a reinforced door", True)

start_cabin.desc = [
    "You look around your cabin, the place you've lived for the last ten years. It's the first place since childhood",
    "that's felt like home. In the center is a modest brick stove with a few cooking elements and a chimney that",
    "pierces your roof."
]

start_cabin.quick_desc = [
    "You are in the main room of your cabin. It's warm and feels like home."
]
cabin_saferoom.desc = [
    "This is your saferoom, where you store all of your various treasures and other special items from your many",
    "adventures. It is small and stuffy, but the walls are lined with iron bars and the door is especially strong."
]
cabin_saferoom.quick_desc = [
    "You are standing in your cabin's saferoom with all your treasures."
]
cabin_loft.desc = [
    "Up the stairs is a small loft with your bed and a small table for reading. There's just enough headspace for",
    "dressing, but floorspace remains limited. As you are the only one who is ever here, it's never been an issue."
]
cabin_loft.quick_desc = [
    "You are upstairs in your cabin, looking over the railing to the ground floor."
]
cabin_clearing.desc = [
    "You stand in front of your cabin, with walls made of oak logs and a steep slate-tile roof that also forms your",
    "east and west walls. The only window sits at the back of the cabin, but is usually covered with a large banner.",
    "You don't typically spend a lot of time indoors anyway."
]
cabin_clearing.quick_desc = [
    "You stand outside your cabin in a small clearing."
]
outhouse.desc = [
    "They say you should't defecate where you masticate, which is why you built your outhouse on the opposite side.",
    "Like all outhouses, it's a humble wooden shack with a seven pointed star on the door. Luckily for you, the",
    "landscape slopes to the southwest from here in case of any overflow issues."
]
outhouse.quick_desc = [
    "You stand next to your outhouse, it smells used."
]
woodshed.desc = [
    "You come to an area cleared of foliage and debris with a large oak chopping block in the center. On the side",
    "of your cabin is an ample woodshed built into the roofslope. This is where you find yourself when you don't",
    "want to think, or to enjoy the crisp, cool air of Ardanion."
]
woodshed.quick_desc = [
    "You stand by your woodshed, contemplating filling your woodshed with more wood."
]
behind_cabin.desc = [
    "The backside of your cabin is decorated with an elk skull and the banner of your former lord. Here, there is",
    "little separation between the small civilization you have built and the untamed wilds of the forest. Regardless",
    "it has always seemed as if your home was protected by a greater power."
]
behind_cabin.quick_desc = [
    "You lean against the back wall of your cabin, staring into the forest."
]
outdoor_kitchen.desc = [
    "On the river side of your cabin, you have set up a fire pit with a few wooden benches, and a table for when you",
    "feel like eating outside. There are a few tanning racks and drying huts that line this side of your cabin, and a",
    "couple barrels for storing things you don't want inside."
]
outdoor_kitchen.quick_desc = [
    "You stand next to your outdoor firepit, watching the river roll by."
]
riverbank_1.desc = [
    "You are on the east bank of Cerbrant Creek, one of the many tributaries of the Silurian River. The creek is",
    "gentle and full of fish when they're in season, a good reason why you built your cabin along it. On the other",
    "side of the creek lies a fairly steep and wooded hill, and while you have occasionally felt the desire to see",
    "what lies at the top, building a bridge or finding a crossing has always proved too much of a task."
]
riverbank_1.quick_desc = [
    "You stand by the banks of a small river."
]
riverbank_2.desc = riverbank_1.desc
riverbank_2.quick_desc = riverbank_1.quick_desc
forest_path_1.desc = [
    "You are on a narrow path through the forest of Ardanion. Sunlight creeps in through the canopy above you, ",
    "providing enough light to move comfortably and to see any threats that might be on the road before you.",
    "The road, though frequently travelled by you, is still barely worn through the thick brush. Over the sound of",
    "the river to the east, you can hear the birdsong and occasional predatory calls of nature."
]
forest_path_1.quick_desc = [
    "You stand the forest path between your home and the rest of the world."
]
forest_path_2.desc = forest_path_1.desc
forest_path_2.quick_desc = forest_path_1.quick_desc
forest_path_3.desc = forest_path_1.desc
forest_path_3.quick_desc = forest_path_1.quick_desc

start_cabin.exits = {
    'southwest': cabin_safe_door,
    'up': cabin_loft
}
start_cabin.exit = cabin_clearing
start_cabin.closed_dirs = {
    'southwest': cabin_saferoom
}
cabin_saferoom.exits = {
    'northeast': start_cabin
}
cabin_loft.exits = {
    'down': start_cabin
}
cabin_clearing.exits = {
    "north": forest_path_1,
    "west": outhouse,
    "east": riverbank_2,
    "southwest": woodshed,
    "southeast": outdoor_kitchen
    
}
cabin_clearing.submaps = {'your cabin': start_cabin}
outhouse.exits = {
    "east": cabin_clearing,
    "south": woodshed
}
outhouse.submaps = [outhouse_in]
outhouse_in.exit = outhouse
woodshed.exits = {
    "north": outhouse,
    "northeast": cabin_clearing,
    "southeast": behind_cabin
}
behind_cabin.exits = {
    "northwest": woodshed,
    "northeast": outdoor_kitchen,
    "southeast": riverbank_1
}
outdoor_kitchen.exits = {
    "northwest": cabin_clearing,
    "north": riverbank_2,
    "southwest": behind_cabin,
    "south": riverbank_1
    
}
riverbank_1.exits = {
    "northwest": behind_cabin,
    "north": outdoor_kitchen,
}
riverbank_2.exits = {
    "west": cabin_clearing,
    "south": outdoor_kitchen
    
}
forest_path_1.exits = {
    "north": forest_path_2,
    "south": cabin_clearing
}
forest_path_2.exits = {
    "north": forest_path_3,
    "south": forest_path_1
}
forest_path_3.exits = {
    "south": forest_path_2
}

forest_path_3.exit = ardanion_south

ardanion_south.submaps = {
    'riverside cabin': forest_path_3,
}
