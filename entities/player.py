from entities.basic import Entity
from src.text import proper, intr

class Player(Entity):
    def __init__(self, name, current_room):
        Entity.__init__(self, name)
        self.name = name
        self.entity_type = 'player'
        self.current_room = current_room

    def travel(self, action, direction):
        # This method is for travelling within the same mapspace.

        # First check if the direction is even valid.
        if direction in self.current_room.exits.keys(): pass
        else:
            # If it's not a valid exit, go back to game loop.
            print(f"You cannot go {direction}.")
            return True
        
        # Next check if the way is open or shut, deny if the way is shut.
        if self.current_room.exits[direction].entity_type == 'door':
            # If the way is shut, prompt the user to open the door.
            print(f"You run into {self.current_room.exits[direction].name}.")
            print(f"You should probably {intr('open')} that first.")
        else:
            # Insert Method to Clear the Screen
            # The below methods transfer a player from roomspace to another.
            print(f"You {action} {direction}.")
            new_room = self.current_room.exits[direction]
            new_room.enter()
            self.current_room = new_room

    def enter(self, place):
        # This will take the place the user wants to enter
        # and pass it to the current room to check if it's
        # a valid submap entry point.

        for name in self.current_room.submaps:
            if place in name:
                submap = self.current_room.submaps[name]
                print(f"You enter {proper(submap.name)}.")
                submap.enter()
                self.current_room = submap
                return True
        else: 
            print(f"You don't see {place} here.")
    
    def exit(self):
        # This will pass to the current room to check if 
        # there's an exit. 
        if self.current_room.exit:
            new_room = self.current_room.exit
            new_room.enter()
            self.current_room = new_room
            return True
        else: 
            print("There's no exit here.")

    # The following three methods are user actions to interact with doors.
    def open_door(self, dir):
        self.current_room.open(dir)

    def close_door(self, dir):
        self.current_room.close(dir)

    def unlock_door(self, dir):
        self.current_room.exits[dir].unlock_door()

    ####################
    ### EYES METHODS ###
    ####################

    def look(self, obj, ind_obj):
        # If the player types 'look at' vs just 'look'
        if ind_obj: obj = ind_obj

        if (not obj or obj == 'room'):
            self.current_room.describe()
            # If no object is given, assume user wants to look at room.
        elif obj in ['self', 'me', 'player', 'myself']:
            self.describe()
        else:
            # TODO add item search when items are added.
            print(f"You don't see {obj} here.")

    def glance(self, obj, ind_obj):
        # Exact same method as above, but for short descriptions. 
        if ind_obj: obj = ind_obj

        if (not obj or obj == 'room'):
            print(f"What are you glancing at in {self.current_room.name}?")
        elif obj in ['self', 'me', 'player', 'myself']:
            self.quick_describe()
        else:
            print(f"You don't see {obj} here.")