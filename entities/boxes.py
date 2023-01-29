from entities.basic import Item
from src.text import numstr, wraptxt, intr

class Box(Item):
    # Boxes are anything that has an internal inventory. A player and a room
    # can both be a box, as they both have inventories. Boxes can also 
    # contain other inventories.
    def __init__(self, name, closed, locked):
        Item.__init__(self, name, pl_name=False)
        self.inventory = {}
        self.isbox = True
        self.closed = closed
        self.locked = locked
        self.keys = []
        self.list_desc = f"inside {self.name}"

    def describe(self):
        for line in self.desc: print(line)
        if self.closed: pass
        else: [print(line) for line in self.list_items()]

    def add_item(self, item):
        if item in self.inventory.keys():
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def remove_item(self, item):
        if self.inventory[item] == 1:
            del self.inventory[item]
        else:
            self.inventory[item] -= 1

    def search_scope(self, search_item):
        found = 0
        found_item = False

        for item in self.inventory.keys():
            if search_item in item.name and found == 0:
                found += 1
                found_item = item
            elif search_item in item.name and found > 0:
                found_item = 'multiple'

        return found_item, self


    def list_items(self):
        # This method returns a list of strings for all items in the box,
        # returning the plural name if the quantity is more than one.
        # The method takes each open box and attempts to print the items 
        # inside on one line, using textwrap to wrap long lines. 

        openboxes = list()  # A blank list of all open boxes in the scope
        nonboxes = dict()  # A blank list of all items that aren't open boxes

        for item in self.inventory.keys():
            # First all items are separated into the above categories
            if (item.isbox and len(item.inventory) > 0) and not item.closed:
                openboxes.append(item)
            elif self.entity_type == 'player':
                if item in self.worn_items: pass 
                # Worn items are described in a different way.
                else: nonboxes[item] = self.inventory[item]
            else:
                nonboxes[item] = self.inventory[item]

        itemcnt = len(nonboxes)  # A count of items left to add to the string
        all_items = f"{intr(self.list_desc.capitalize())}: "  # The itemlist starter

        for item in nonboxes.keys():
            qty = nonboxes[item]
            if qty > 1 and itemcnt > 1:
                # If there are items left and the item quantity is more than 1
                # list the quantity of the item, the item, and add a comma.
                all_items += f"{numstr(qty)} {item.pl_name}, "
                itemcnt -= 1
            elif qty > 1 and len(nonboxes) == 1:
                # If there's just one item in the list, list only item and qty.
                all_items += f"{numstr(qty)} {item.pl_name}."
                itemcnt -= 1
            elif qty > 1:
                # Otherwise, end the list by starting with and.
                all_items += f"{numstr(qty)} {item.pl_name}."
            elif qty == 1 and itemcnt > 1:
                # Same as above 3, but only list the singular item name
                all_items += f"{item.name}, "
                itemcnt -= 1
            elif qty == 1 and len(nonboxes) == 1:
                all_items += f"{item.name}."
                itemcnt -= 1
            elif qty == 1:
                all_items += f"{item.name}."

        itemlist = list()  # A blank list for all items in all boxes in scope
        itemlist.extend(wraptxt(all_items))  # Start itemlist with root items
            
        for box in openboxes:  
            # Add any open boxes to the list with recursive call
            [itemlist.append(line) for line in box.list_items()]

        return itemlist
            
    def open_box(self):
        if self.closed and not self.locked:
            self.closed = False
            print(f"You open {self.name}.")
        elif self.closed and self.locked:  # TODO implement door/box locks
            print(f"{self.name.capitalize()} is locked.")
        else:
            print(f"{self.name.capitalize()} is already open")

    def close_box(self):
        if self.closed:
            print(f"{self.name.capitalize()} is already closed.")
        else:
            self.closed = True
            print(f"You close {self.name}.")

    def unlock_box(self, actor):
        if self.locked:
            found = False
            for key in self.keys:
                if key in actor.inventory.keys():  # lol
                    self.locked = False
                    found = True
                    print(f"Unlocked {self.name}.")
            if found == False: 
                print(f"You need the key to unlock {self.name} first!")
                return True
        elif not self.locked:
            print(f"{self.name.capitalize()} is already unlocked.")
        
        print(f"Would you like to open {self.name}?")
        choice = input("(y/n)> ")
        if choice.lower()[0] == 'y': self.open_box()
        elif choice.lower()[0] == 'n': return True
        else:
            print(f"I didn't understand that, {self.name} is still closed.")


class RoomBox(Box):
    # This is for all containers that are stuck in a room.
    def __init__(self, name, closed, locked):
        Item.__init__(self, name, pl_name=False)
        self.fixed = True


class Holster(Box):
    # Holsters are boxes that have a specific slot for one type of item. 
     def __init__(self, name):
        Box.__init__(self, name)
