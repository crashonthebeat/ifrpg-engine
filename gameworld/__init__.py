# This is the game module that imports the world. 
# Worldspace: All locations, exits, descriptions of locations
# Worldspace should be divided into folders based on regions.
# Overworlds can go into the root worldspace folder. 

import gameworld.worldspace
import gameworld.items
from entities.player import Player

pc = Player("Thom the Tester", gameworld.worldspace.ardanion.cabinclearing.start_cabin)