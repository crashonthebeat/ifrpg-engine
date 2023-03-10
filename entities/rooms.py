from entities.basic import Roomspace
from entities.boxes import Box
from src.text import *

class MapRoom(Roomspace):
    # A MapRoom is an overworld scene. There won't be any items but 
    # locations and directions can still be uncovered. 
    def __init__(self, name):
        Roomspace.__init__(self, name)
        self.entity_type = 'overworld'

    def list_exits(self):
        # This method will list all exits of a room and their direction.
        # This differs from the inherited method as there will be no
        # exits from the overworld map, but there can be several entrances
        # in one specific map location.

        print(f"Locations in {proper(self.name)}:")
        for submap in self.submaps.values():  # List all entrances first.
            print(f"{proper(intr(submap.name))}")
        for dir, exit in zip(self.exits.keys(), self.exits.values()):
            # Then list all same-space exits.
            print(f"{ex(dir.upper())}: {proper(exit.name)}")

class Room(Roomspace, Box):
    # This is a classic scene, with all features.
    def __init__(self, name):
        Roomspace.__init__(self, name)
        self.list_desc = f"inside {self.name}"
        self.closed_dirs = {}
        # A key of the direction and either what the room beyond should be,
        # or the a door, if the direction can be closed.
        self.inventory = {}
        

    def describe(self):
        # This method will differ from other describe methods since it will
        # include inventory as well as exits.
        for line in self.desc: print(line)
        for line in self.list_items(): print(line)

    def open(self, dire):
        # This method opens a direction if it is closed.
        # Method doesn't actually open a door.
        if self.exits[dire].entity_type != 'door':
            # I.E. Check if there's a door in the way first.
            print("The way is already open.")
            return True
        elif not self.exits[dire].locked:
            # Also, check if the door is locked. 
            print(f"You open {self.exits[dire].name}.")
            self.exits[dire], self.closed_dirs[dire] = swap_items(
                self.exits[dire],
                self.closed_dirs[dire])
            return True
        else:
            # Otherwise, there's a door in the way and it's locked.
            print(f"You need to {intr('unlock')} {self.exits[dire].name} first.")

    def close(self, dire):
        # This method closes a direction if it can be.
        if self.exits[dire].entity_type == 'door':
            print(f"{self.exits[dire].name.capitalize()} is already closed")
            return True
        else:
            print(f"You close {self.closed_dirs[dire].name}.")
            self.exits[dire], self.closed_dirs[dire] = swap_items(
                self.exits[dire],
                self.closed_dirs[dire])
            return True

class Door(Roomspace):
    # Open and Close Method will swap out a closed door for the room beyond
    # the door for ease of displaying exits. Players should not be able to
    # actually go inside doors.

    def __init__(self, name, locked):
        Roomspace.__init__(self, name)
        self.locked = locked
        self.desc = ["How the hell did you end up here?"]
        self.quick_desc = [
            "You're inside a door.", 
            "Either you cheated or there's a bug."]
        self.keys = []
        self.entity_type = 'door'
        # This will be set in the inventory initialization with the key item.

    def unlock_door(self, actor, dire):
        if self.locked:
            found = False
            for key in self.keys:
                if key in actor.inventory.keys():
                    self.locked = False
                    print(f"Unlocked {self.name}.")
                    found = True
            if found == False: 
                print(f"You need the key to unlock {self.name} first!")
        else:
            print(f"{self.name.capitalize()} is already unlocked.")
            return False  # Stop method if already unlocked.

        print(f"Would you like to open {self.name}?")
        choice = input("(y/n)> ")
        if choice.lower()[0] == 'y': actor.current_room.open(dire)
        elif choice.lower()[0] == 'n': return True
        else:
            print(f"I didn't understand that, {self.name} is still closed.")