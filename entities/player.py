from entities.basic import Entity
from entities.boxes import Box
from entities.boxscope import localscope, scenescope, selfscope, weaponscope
from src.text import proper, intr, wraptxt
from itertools import chain

directions = [
    "north", "east", "south", "west", "northeast", "northwest",
    "southeast", "southwest", "up", "down"]

class Player(Box):
    def __init__(self, name, current_room):
        Entity.__init__(self, name)
        self.name = name
        self.entity_type = 'player'
        self.current_room = current_room
        self.list_desc = 'in your hands'
        self.worn_items = []  # Items worn on body
        self.held_items = []  # Items not in a pouch/bag
        self.wield_items = []  # Tools/Weapons wielded
        self.hands = 2  # We only got 2
        self.carry_slots = 20  # How much player can hold in hand.
        self.used_slots = 0
        self.inventory = {}  # A dict of items
        # This game engine doesn't have a classic inventory where anything
        # you pick up goes into a pile above your head. You will have a 
        # limited space to put things based on weight and size. So, if
        # you pick something up it'll go into your hands if you have a
        # free hand.
        self.closed = False

    def describe(self):
        for line in self.desc: print(line)
        if len(self.inventory) > 0:
            for line in self.list_items(): print(line)
        print("You are wielding: ")
        [print(item.name) for item in self.wield_items]
        print("You are wearing: ")
        [print(item.name) for item in self.worn_items]

    def open_close(self, obj, action):
        # This and the following method will check if the object is
        # a direction or container, as well as what the player wants
        # do do, and then passes it to the correct method.

        #
        # DOOR OPEN/CLOSE
        if obj in directions and action == 'open':
            # Opens a Direction
            self.current_room.open(obj)
        elif obj in directions and action == 'close':
            # Closes a Direction
            self.current_room.close(obj)
        elif obj in directions and action == 'unlock':
            # Unocks a Direction
            self.current_room.exits[obj].unlock_door(self, obj)
        #
        # BOX OPEN/CLOSE
        #
        elif action == 'open':
            box, parent = self.find_item(obj, scenescope)
            if box: box.open_box()
        elif action == 'close':
            box, parent = self.find_item(obj, scenescope)
            if box: box.close_box()
        elif action == 'unlock':
            box, parent = self.find_item(obj, scenescope)
            if box: box.unlock_box(self)

    #######################
    ### UTILITY METHODS ###
    #######################

    def find_box(self, search_box):
        # This method searches localscope for the user defined box and 
        # checks if the item can in fact be a box or not.
        box, parent = localscope.search_scope(search_box)

    def find_item(self, search_item, scope):
        item, box = scope.search_scope(search_item)

        if not item:
            print(f"You don't see {search_item} here.")
            return False, False
        elif item == 'multiple':
            print(f"Which {search_item} do you mean?")
            return False, False
        elif box.name == self.current_room.name:
            return item, box
        elif box and box.closed:
            print(f"You don't see {search_item} here.")
            return False, False
        else:
            return item, box

    def test_for_fit(self, item):
        # This method iterates over all items worn, and checks the test
        # item against all slots currently occupied. If the method finds
        # a matching layer on a matching slot, then the item does not fit

        itemslots = item.occupied_slots  # To enhance readability

        for article in self.worn_items:  # Looping over all items
            usedslots = article.occupied_slots  # Another readability thing
            for slot in itemslots:  # looping over all item's slots
                # Keep going until you find a matching layer on a slot
                if slot not in usedslots.keys(): pass
                elif itemslots[slot] == usedslots[slot]:
                    print("That won't fit over what you're wearing!")
                    return False
        
        # Otherwise the item fits.
        return True

    ######################
    ### TRAVEL METHODS ###
    ######################

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
            self.current_room = new_room
            self.current_room.enter(self)
    
    def enter_submap(self, place):
        # This will take the place the user wants to enter
        # and pass it to the current room to check if it's
        # a valid submap entry point.

        for name in self.current_room.submaps:
            if place in name:
                submap = self.current_room.submaps[name]
                print(f"You enter {proper(submap.name)}.")
                self.current_room = submap
                self.current_room.enter(self)
                return True
        else: 
            print(f"You don't see {place} here.")
    
    def exit(self):
        # This will pass to the current room to check if 
        # there's an exit. 
        if self.current_room.exit:
            new_room = self.current_room.exit
            self.current_room = new_room
            self.current_room.enter(self)
            return True
        else: 
            print("There's no exit here.")

    ####################
    ### EYES METHODS ###
    ####################

    def look(self, obj, ind_obj):
        # If the player types 'look at' vs just 'look'
        if ind_obj: obj = ind_obj

        if (not obj or obj == 'room'):
            # If no object is given, assume user wants to look at room.
            self.current_room.describe()
            self.current_room.list_exits()
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

        if item in self.inventory.keys():
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
            self.held_items.append(item)  # Add to held items
        
        self.used_slots += item.itemsize

    def remove_item(self, item):
        if self.inventory[item] == 1:
            del self.inventory[item]
            self.held_items.remove(item)  # Remove from Held Items
            self.used_slots -= item.itemsize
        else:
            self.inventory[item] -= 1

    def get_item(self, search_item, search_box):
        # In this case, the ind_obj will be the box, and the obj itself
        # is the item they want to get.

        if search_box and search_box != 'room':
            box, parent = self.find_item(search_box, localscope)
            if not box: return True
            else: item, box = self.find_item(search_item, box)
        elif self.current_room.entity_type == 'overworld':
            print("This is too broad an area to find one item.")
            return True
        else:
            # Otherwise, search localscope for the item and return the
            # item and box. 
            item, box = self.find_item(search_item, scenescope)
        if not item: return True
        if item.fixed:
            print(f"You can't pick up {item.name}!")
        elif item.itemsize > (self.carry_slots - self.used_slots):
            print("You can't hold that with everything else " +
            "you are carrying!")
            print("Put something away or drop something first.")
        else:
            box.remove_item(item)
            self.add_item(item)
            print(f"You get {item.name} from {box.name}.")
            if item.isbox: localscope.update_scope(self)

    def drop_item(self, search_item):
        # This method only searches held items, as the player can't
        # Directly drop something from a worn inventory. (May add)

        found = 0
        found_item = False

        for item in self.inventory.keys():
            if search_item in item.name and found == 0:
                found += 1
                found_item = item
            elif search_item in item.name:
                print(f"Which {search_item} do you want to drop?")
                return True
        
        if found_item and found_item in self.worn_items:
            print("You need to unequip that first.")
        elif found_item:
            if self.current_room.entity_type == 'overworld':
                print("You are travelling in the overworld.")
                print("If you drop an item, it will be lost forever.")
                print(f"Are you sure you want to drop {item.name}?")
                choice = input("(y/n)> ")
                if choice.lower()[0] == 'y': 
                    self.remove_item(found_item)
                    print(f"You drop {found_item.name}")
                    return True
                else: return True
            self.remove_item(found_item)
            self.current_room.add_item(found_item)
            print(f"You drop {found_item.name}")
        else:
            print(f"You can't find {search_item}")

    def place_item(self, search_item, search_box, prep):
        # This item is for placing an item directly into a user
        # defined box.

        # First check if the defined box exists in localscope
        box, parent = self.find_item(search_box, localscope)
        if not box: return True
        # Now check if player has item in hands.
        else: item, parent = self.find_item(search_item, self)
        if not item: return True
        elif item in self.worn_items:
            print("You need to unequip that first.")
            return True
        else: pass
        if box.entity_type == 'rack' and box.test_item(item) == False:
            return True
        else:
            if item in self.wield_items: 
                self.wield_items.remove(item)
                self.used_slots += (item.itemsize)  # Add hand slots.
                self.used_slots -= (item.hands * 10)
            box.add_item(item)
            self.remove_item(item)
            print(f"You put {item.name} {prep} {box.name}.")


    #####################
    ### EQUIP METHODS ###
    #####################

    def wear_item(self, item):
        itemfits = self.test_for_fit(item)  # Test item for fit

        if itemfits:
            self.worn_items.append(item)
            self.used_slots -= item.itemsize
            # add the item to worn items.
            print(f"You put {item.name} on your {item.primary_slot}.")
            if item.isbox: 
                localscope.update_scope(self)
                item.closed = False
        else: return True

    def wield_item(self, item):
        # Test if player has free hands to use the tool effectively
        # Item takes up all its effective hand slots to wield
        # 1h = 10 slots, 2h = 20 slots. Otherwise item can be held.
        if  (item.hands * 10 - item.itemsize) > \
            (self.carry_slots - self.used_slots):
            # If there's too much in player hands to wield item.
            print(
                f"You cannot effectively wield {item.name}! " +
                f"{item.name.capitalize()} needs {item.hands} hands free.")
            print("You will need to put some things away first.")
            return True
        else: 
            # Otherwise, the item can be wielded, so wield it.
            print(f"You take a ready stance with {item.name}.")
            self.wield_items.append(item)  # add item to wielded items.
            self.used_slots -= (item.itemsize)  # Add hand slots.
            self.used_slots += (item.hands * 10)

    def equip_item(self, search_item):
        # This method searches for an item, tests what it is,
        # and if it's apparel, passes it to the wear_item
        # or wield_item method.
        
        item, box = self.find_item(search_item, self)
        if not item: return True
        elif 'apparel' in item.entity_type: self.wear_item(item)
        elif 'weapon' in item.entity_type: self.wield_item(item)
        else: print("You can't equip that!")

    def unequip_item(self, search_item):
        item, box = self.find_item(search_item, self)
        if not item: return True
        elif item not in chain(self.worn_items, self.wield_items):
            print(f"You haven't equipped {item.name}.")
            return True
        elif item in self.wield_items:
            self.wield_items.remove(item)
            print(f"You drop your stance with {item.name} but still hold it.")
            self.used_slots -= (item.hands * 10)
            self.used_slots += (item.itemsize)  # Add hand slots.
            return True
        else: pass

        if item.itemsize > (self.carry_slots - self.used_slots):
            print(
                f"You can't remove {item.name}, you need to " + 
                "put something away first!")
        else: 
            print(f"You remove {item.name} and hold it in your hands.")
            self.worn_items.remove(item)
            self.used_slots += item.itemsize

    def sheath_all(self):
        for item in self.wield_items:
            for sheath in weaponscope.boxes:
                if sheath.test_item(item, verbose=False):
                    sheath.add_item(item)
                    self.wield_items.remove(item)
                    self.used_slots += (item.itemsize)  # Add hand slots.
                    self.used_slots -= (item.hands * 10)
                    self.remove_item(item)
                    print(f"You return {item.name} to {sheath.name}.")

        for item in self.wield_items:
            print(f"You could not find a place for {item.name}")

    def sheath_weapon(self, search_item):
        if not search_item:
            self.sheath_all()
            return True

        item, box = self.find_item(search_item, self)
        if not item: return True

        elif item not in self.wield_items:
            print(f"You are not currently wielding {item.name}")
            return True
        elif item in self.wield_items:
            for sheath in weaponscope.boxes:
                if sheath.test_item(item, verbose=False):
                    sheath.add_item(item)
                    self.wield_items.remove(item)
                    self.used_slots += (item.itemsize)  # Add hand slots.
                    self.used_slots -= (item.hands * 10)
                    self.remove_item(item)
                    print(f"You return {item.name} to {sheath.name}.")

    def draw_action(self, item, sheath):
        if  (item.hands * 10 - item.itemsize) > \
            (self.carry_slots - self.used_slots):
            # If there's too much in player hands to wield item.
            print(
                f"You cannot effectively wield {item.name}! " +
                f"{item.name.capitalize()} needs {item.hands} hands free.")
            print("You will need to put some things away first.")
            return True
        else: 
            # Otherwise, the item can be wielded, so wield it.
            print(f"You draw {item.name}.")
            sheath.remove_item(item)
            self.add_item(item)
            self.wield_items.append(item)  # add item to wielded items.
            self.used_slots -= (item.itemsize)  # Add hand slots.
            self.used_slots += (item.hands * 10)

    def draw_all(self):
        for sheath in weaponscope.boxes:
            for item in list(sheath.inventory.keys()):
                self.draw_action(item, sheath)

    def draw_weapon(self, search_item):
        if search_item == False:
            self.draw_all()
            return True

        item, sheath = self.find_item(search_item, weaponscope)
        if not item: return True
        else: self.draw_action(item, sheath)
        
                    