import src.inparse as cmd

from gameworld import *  # This will change to import the world state.
from entities.boxscope import localscope

# List of action verbs for each category of action
# These are explained below in the validate_action method.
travel_actions = ['go', 'travel', 'walk', 'jog']
describe_actions = ['look', 'view', 'describe']
glance_actions = ['glance', 'peek']
take_actions = ['take', 'get', 'grab', 'retrieve', 'nab']
drop_actions = ['drop', 'yeet']
open_actions = ['open', 'close', 'unlock']
put_actions = ['place', 'put', 'set', 'mount']
equip_actions = ['equip', 'eq', 'wear', 'don', 'wield', 'arm']
unequip_actions = ['unequip', 'uq', 'remove', 'strip', 'unarm']
use_actions = ['use', 'activate', 'push']


def validate_action(action, obj, ind_obj, prep):
    if action in travel_actions: pc.travel(action, obj)     # Travel Action
    elif action  == 'enter': pc.enter_submap(obj)           # Enter Submap
    elif action == 'exit': pc.exit()                        # Exit Submap
    elif action in open_actions: pc.open_close(obj, action) # Open/Close Thing
    elif action in describe_actions: pc.look(obj, ind_obj)  # Describe Thing
    elif action in glance_actions: pc.glance(obj, ind_obj)  # Glance Action
    elif action in take_actions: pc.get_item(obj, ind_obj)  # Take Item
    elif action in drop_actions: pc.drop_item(obj)          # Drop Item
    elif action in put_actions: 
        pc.place_item(obj, ind_obj, prep)                   # Place Item
    elif action in equip_actions: pc.equip_item(obj)        # Equip Item
    elif action in unequip_actions: pc.unequip_item(obj)    # Unequip Item
    elif action in use_actions: pc.use_item(obj, ind_obj)   # Use item
    elif action == "quit": return False                     # Exit to Menu
    # Default: 
    else: print(f"You don't know how to {action}")

    return True

def command_loop(game=True):
    pc.current_room.enter()
    localscope.update_scope(pc)
    # On game start, have player re-enter room to re-establish scenery.
    while game:  # Core Game loop, ask for input > get input
        print("What would you like to do?")
        user_input = input("> ")
        action, obj, ind_obj, prep = cmd.parse(user_input)
        # Passes user input to the command parser to gather the basic
        # data.

        game = validate_action(action, obj, ind_obj, prep)
        # Validates the action through all possible methods.

if __name__ == '__main__':
    command_loop()