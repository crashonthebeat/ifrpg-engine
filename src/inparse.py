# This is the command parser. It takes a user input and then divides that
# input into three basic elements: the verb (primary action), the direct 
# object (the recipient of the action), and the indirect object (the 
# recipient of the object). 
# 
# For those who slept through grammar class, in the command "drop sword", 
# drop is the verb, and sword is the direct object, as the sword is what
# you are dropping. In the command, "take sword from stone", "take" is 
# the action, the sword is what you are "taking", and the stone is the 
# indirect object, indicating that is where you are taking the sword from.
# This indirect object is typically after a preposition. 
# 
# This will be explained to players in the help file. 

fillers = ["the", "a", "an", "i", "we", "me", "us", "some"]
prepositions = ["with", "to", "in", "from", "on", "of", "at"]
directions = ["north", "n", "east", "e", "south", "s", "west", "w",
              "up", "down", "northeast", "ne", "southeast", "se", 
              "southwest", "sw", "northwest", "nw"]
# A list of shorthand direction names.
shorthand = {
            "n": "north", "s": "south", "e": "east", "w": "west",
            "nw": "northwest", "ne": "northeast", 
            "se": "southeast", "sw": "southwest"
        }

def remove_fillers(user_input):
    # This method takes away all of the articles and pronouns from a user
    # input in order leave just the important parts of speech. It simply
    # loops over every word in the user_input list and pops out the fillers.

    i = 0
    while i < len(user_input):
        if user_input[i] in fillers:
            user_input.remove(user_input[i])
            i += 1
        else: 
            i += 1

    return user_input

def get_objects(user_input):
    # This method depends on the preposition, which will separate the 
    # direct object from the indirect object. It pops out that word and
    # stores it (if it's needed for future additions) and then marks
    # its index as the start of the indirect object. Then it returns 
    # the two strings and the preposition.

    prep = False
    ind_obj = False

    for i in range(len(user_input)-1):
        if user_input[i] in prepositions:
            prep = user_input.pop(i)
            indobj_index = i
        else: continue

    if prep:
        ind_obj = " ".join(user_input[indobj_index:])
        obj = " ".join(user_input[:indobj_index])
    else:
        obj = ' '.join(user_input)
        
    return obj, ind_obj, prep

def direction_parse(dir):
    # This method will transform the user input if they just entered a
    # direction or directional shorthand.

    if dir in shorthand.keys():
        dir = shorthand[dir]

    return dir

def parse(user_input):
    # This method takes a string, splits it into a list, and then passes
    # it through the above methods to get all the parts of speech into
    # their own separate strings.

    user_input = user_input.lower().split(" ")  # Split user_input into a list
    user_input = remove_fillers(user_input)  # Remove filler words

    action = user_input.pop(0)  # Get action from user_input

    if action in directions:  # Allows a user to input just a direction.
        return 'go', direction_parse(action), False, False

    # If the verb is removed and nothing is left in the user input, that
    # means the user just entered an action verb, so that should be 
    # returned rather than passing it through the next method.
    if len(user_input) == 0: return action, False, False, False

    obj, ind_obj, prep = get_objects(user_input)  # Get objects, see above

    if obj in shorthand.keys():
        obj = direction_parse(obj)

    return action, obj, ind_obj, prep