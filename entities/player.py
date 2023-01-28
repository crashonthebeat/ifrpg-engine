from entities.basic import Entity
from entities.boxscope import localscope, scenescope, selfscope
from src.text import proper, intr

class Player(Entity):
    def __init__(self, name, current_room):
        Entity.__init__(self, name)
        self.name = name
        self.entity_type = 'player'
        self.current_room = current_room
        self.worn_items = []  # A list of items
        self.held_items = {}  # A dict of items - "inventory"
        # This game engine doesn't have a classic inventory where anything
        # you pick up goes into a pile above your head. You will have a 
        # limited space to put things based on weight and size. So, if
        # you pick something up it'll go into your hands if you have a
        # free hand.

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

    #######################
    ### UTILITY METHODS ###
    #######################

    def find_box(self, search_box):
        # This method searches localscope for the user defined box and 
        # checks if the item can in fact be a box or not.
        box, scope = localscope.search_scope(search_box)

    def find_item(self, search_item, scope):
        item, box = scope.search_scope(search_item)

        if not item:
            print(f"You don't see {search_item} here.")
            return False, False
        elif item == 'multiple':
            print(f"Which {search_item} do you mean?")
            return False, False
        elif box.name == self.current_room.name:
            print(f"You pick up {item.name}.")
            return item, box
        elif box and not box.open:
            print(f"You don't see {search_item} here.")
            return False, False
        elif box and box.open:
            print(f"You get {item.name} from {box.name}.")
            return item, box
        else:
            print(f"You pick up {item.name}.")
            return item, box

    ######################
    ### TRAVEL METHODS ###
    ######################
    
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
            # If no object is given, assume user wants to look at room.
            self.current_room.describe()
        elif obj in ['self', 'me', 'player', 'myself']:
            self.describe()
        else:
            item, box = self.find_item(obj, localscope)
            if item: item.describe()

    def glance(self, obj, ind_obj):
        # Exact same method as above, but for short descriptions. 
        if ind_obj: obj = ind_obj

        if (not obj or obj == 'room'):
            print(f"What are you glancing at in {self.current_room.name}?")
        elif obj in ['self', 'me', 'player', 'myself']:
            self.quick_describe()
        else:
            item, box = self.find_item(obj, localscope)
            if item: item.quick_describe()

    ####################
    ### ITEM METHODS ###
    ####################

    def add_item(self, item):
        if item in self.held_items.keys():
            self.held_items[item] += 1
        else:
            self.held_items[item] = 1
        

    def get_item(self, search_item, search_box):
        # In this case, the ind_obj will be the box, and the obj itself
        # is the item they want to get.

        if search_box:
            # If the player specifies a box, search localscope for the
            # box, and then search the box for the item.
            # Box will need to be checked if it's open or not.
            pass  # TODO Implement after get_item finished.
        else:
            # Otherwise, search localscope for the item and return the
            # item and box. 
            item, box = self.find_item(search_item, localscope)
            if not item: return True
            else:
                box.remove_item(item)
                self.add_item(item)
                if item.isbox: localscope.update_scope(self)