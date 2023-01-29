from src.text import *
from entities.boxscope import localscope, scenescope

class Entity:
    # Everything noun that exists in the world will have the methods and 
    # attributes listed in this class. So far, a name and a description.

    def __init__(self, name):
        self.name = name
        self.desc = [
            f"You see nothing special about {self.name}.",
            "This description has yet to be written."]
        # A full description for looking directly at something.
        self.quick_desc = [
            f"You see nothing special about {self.name}.",
            "This quick description has yet to be written."]
        # A quick description for glancing. 
        self.entity_type = False
        # Entity type is a string that tells the game what the primary type
        # the object is. Used for validation of actions. If the code is
        # looking for an id (variable name) it will look for:
        # entityType_id (box_id, item_id, etc.)

    def describe(self):
        # This method is run when the player looks at an entity. It will 
        # be descriptive and verbose, not intended for a quick look. 
        for line in self.desc: print(line)

    def quick_describe(self):
        # This method will be like describe, but for a quick look, called 
        # by 'glance' or a similar word.
        for line in self.quick_desc: print(line)

    def inspection(self):
        # This method will be called if a player closely inspects a
        # specific item looking for clues or anything that didn't
        # immediately pop out.

        # Ideally this would be gated behind different player levels
        # or skill of inspection and a diceroll.
        pass

class Person(Entity):
    pass

class Roomspace(Entity):
    # A roomspace can be an overworld location (for map travelling),
    # as well as rooms and subrooms. Map spaces will be more broad,
    # general areas, whereas rooms will typically be areas that 
    # are within sight range, divided up in a way that makes sense for
    # the creation of said space.

    def __init__(self, name):
        Entity.__init__(self, name)
        # Room name will be a short, lowercase string with no punc.
        self.entity_type = 'place'
        self.exits = {}  # A dict of 'direction' to place id.
        self.submaps = {}  # A dict of submaps in a room, string:submap
        self.exit = False  # Where the exit goes, if there is one.
        self.visited = False  # If the player has visited a roomspace.

    def list_exits(self):
        # This method will list all exits of a room and their direction.

        for submap in self.submaps.keys():  # List all entrances first.
            print(f"An entrance to {intr(submap)} is here.")
        for dir, exit in zip(self.exits.keys(), self.exits.values()):
            # Then list all same-space exits.
            print(f"{ex(dir.upper())}: {proper(exit.name)}")
        if self.exit: print(f"{ex('EXIT')}: {proper(self.exit.name)}.")
        # Finally, if this place is an exit, say so. 

    def enter(self, actor):
        # This is the method that performs all tasks necessary
        # when the player enters this specific room.

        # Separates previous roomscene until a better display method
        # is found. 
        localscope.update_scope(actor)
        print(title('---' + proper(self.name) + '---'))
        # If the player has not visited a room, print the full 
        # description. Otherwise, give a partial one.
        if self.visited: 
            self.quick_describe()
        else: 
            self.describe()
            self.visited = True

        if self.entity_type == 'room': pass 
        # Saving this line for when a room will list its contents.
        self.list_exits()  # Finally, list all room exits.

class Item(Entity):
    def __init__(self, name, pl_name, itemsize):
        Entity.__init__(self, name)
        self.pl_name = pl_name  # The plural name of an item.
        self.fixed = False  # Whether the object can move between inventories
        self.isbox = False
        self.itemsize = itemsize  # How big the item is