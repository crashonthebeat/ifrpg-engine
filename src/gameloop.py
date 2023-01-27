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
put_actions = ['place', 'put', 'set', 'mount']
equip_actions = ['equip', 'eq', 'wear', 'don', 'wield', 'arm']
unequip_actions = ['unequip', 'uq', 'remove', 'strip', 'unarm']


def validate_action(action, obj, ind_obj, prep):
    # Travel Action (Moving between roomspaces): 
    if action in travel_actions: pc.travel(action, obj)
    # Enter Action (Moving to Submap):
    elif action  == 'enter': pc.enter(obj)
    # Exit Action (Moving out of Submap):
    elif action == 'exit': pc.exit()
    # Open/close Door:
    elif action == 'open': pc.open_door(obj)
    elif action == 'close': pc.close_door(obj)
    elif action == 'unlock': pc.unlock_door(obj)
    # Describe Action (Getting an object's description): 
    elif action in describe_actions: pc.look(obj, ind_obj)
    # Quick Describe Action (Glancing):
    elif action in glance_actions: pc.glance(obj, ind_obj)
    # Take Action:
    elif action in take_actions: pc.get_item(obj, ind_obj)
    # Exit to Menu: 
    elif action == "quit": return False
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