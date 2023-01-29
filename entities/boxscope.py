# These classes are global inventory scopes that represent self updating
# aggregates of all inventories in an area to iterate over, depending on
# either the method's scope or the user selected scope.

class BoxScope:
    # This is the class for all global inventory objects. Each scope will
    # include closed inventories, as the specific caller methods should be
    # the ones to determine whether or not an item can be called. 
    def __init__(self, name):
        self.name = name
        self.boxes = []  # All boxes in inventory

    def update_scope(self):
        # This is a method called when an inventory is moved from or to
        # the target scope.
        pass

    def search_scope(self, search_item):
        # This method searches for an item in all boxes within the scope.
        # It return the box object so that the console will list what box
        # an item came from for verbosity's sake.

        found = 0  # The counter for if an item has been found
        found_item = False  # If no item is found, this will return
        found_box = False 

        for box in self.boxes:  # Loop over all boxes
            for item in box.inventory.keys():  # Loop over all items in a box
                if search_item in item.name and found == 0:  
                    # If search term matches and item hasn't been found
                    found += 1  # Increment counter
                    found_item = item  # Return the item object
                    found_box = box  # Return the box object
                elif search_item in item.name:
                    # If the search term was too vague to match an item,
                    # Tell the find item function that multiples were found.
                    found_item = 'multiple'  # Change found item status
                    return found_item, found_box  # Stop the function.

        return found_item, found_box


class SelfScope(BoxScope):
    # This is the class for all inventories on a player, including equip.
    # Non-equipped boxes will not be part of this or any scope.
    def __init__(self, name):
        BoxScope.__init__(self, name) 
    
    def update_scope(self, player):
        # When called, this method will find any container on the body, 
        # ensure that it is opened and remake the list.
        self.boxes = [player]
        for item in player.worn_items:
            if item.isbox: self.boxes.append(item)
        

selfscope = SelfScope('selfscope')


class SceneScope(BoxScope):
    # SceneScope is for any inventory that exists in the room not in the
    # players inventory or equipped items. 
    def __init__(self, name):
        BoxScope.__init__(self, name)
        self.boxes = []
    
    def update_scope(self, player):
        # When called, this method will check the room's inventory for
        # items that are containers, and add them to the scope along with
        # the current room's inventory.

        if player.current_room.entity_type == 'overworld':
            self.boxes = []  # Overworlds do not have inventory.
        else:
            self.boxes = [player.current_room]
            for item in player.current_room.inventory.keys():
                if item.isbox: 
                    self.boxes.append(item)

scenescope = SceneScope('scenescope')  # All non-player inventories in a room.


class LocalScope(BoxScope):
    # This is the class for all accessible inventories in the local scene, 
    # including the player inventory and equipped items. 
    def __init__(self, name):
        BoxScope.__init__(self, name)

    #def search_scope(self, search_item):
        #return super(LocalScope, self).search_scope(search_item)
    
    def update_scope(self, player):
        # When this method is called, it will update the scope to add both
        # scene and self scope.
        localscope.boxes = []  # Clear out localscope

        selfscope.update_scope(player)
        scenescope.update_scope(player)

        self.boxes.extend(scenescope.boxes)
        self.boxes.extend(selfscope.boxes)


localscope = LocalScope('localscope')


