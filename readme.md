# IFRPG-ENGINE v 0.2 - Hand Stuff

This is a text-adventure rpg engine written from scratch in python. I'm not intending this to be something for people to just use out of the box, since this will just be a creative outlet for me as well as a vessel to expand my knowledge of python, as well as git, so you'll hopefully see how I improve with commits and other things. 

Additionally, I've rewritten this code several times, not including this time. I will most likely re-write it again, but I'll fork the old versions off like I did this time. I'm not out to get a job in coding, so this version control might be chaos. I truly do apologize for that, I do have other project ideas that I will be better at versioning. 

## Current Functionality

* Travelling between rooms in the same "dimension" (cardinal directions, up/down)
* Travelling across mapspaces (to and from overworld, to and from submaps)
* Opening, Closing, and Unlocking Doors/Directions (Key functionality will come with the usable items update)
* Item interaction, getting items, placing items into containers or dropping them into the room

## The Plan

This Engine will be a complex series of python files that will eventually be able to serve an interactive fiction story as a playable open-ish world rpg. I'm taking inspiration from old sierra games and MUD/MUSHes where there's an open text input. There will be a help file, though.

I'm going to work on different parts of the game methodically. The reason for this is I want to gather all the features I want that could be related to one of the parts, work out how they interact with existing code and with each other, and then put them to silicon. 

### Stage 1 - The Basics **Complete**

* Classes - Different Entity Types
    * Basic Entities: Location, Item, and Person
    * Additional Entity Types: Container (That which holds an item), Gamestate (Puzzle state, Quest state, story state), Topic (for Dialogue), Probably more to come
* Travelling
    * Going between roomspaces, subspaces, and the overworld. 
    * What happens when you enter and leave a room.
* Descriptions and Looking
    * The text that displays when you look at a certain thing, whether it be a person, place, or thing
    * Looking closer at specific objects of interest, finding out additional information.

### Stage 2 - Items and Containers **Complete**

* Three types of inventories:
    * Root Inventories, like that of a room's inventory or your own inventory
    * Sub-Inventories, things in an open chest in a room or a backpack, pouch, or holster
    * Equipped Items: Things on your person, or things in a room that can be used
* Finding Items - Iterating over several lists
    * How does the game find items? How does it decide what inventory(ies) to search through? \
    In a nutshell, the find item method will have a set scope. Some scopes only include certain inventories, like equip/unequip only looking for items in the user's inventory with the correct equip state, and "get" only looking for roomspace items, unless a specific container was called. This was to me the hardest method to figure out, and I didn't plan it out well in advance, hence the need to rewrite the entire code because of it. I'm hoping I learn from my mistakes.

### Stage 3 - Interactive Items

* Interacting with items
    * As I said above, different interactions will have different search scopes, which makes it important to add specific attributes to items. For example, adding an is_container attribute to an item in order to get a search method to search those containers, but also an is_open method so closed/locked chests cant be cheated through.
* Equipment
    * Equipping and Unequipping items presents its own challenges, like how to deal with item slots in a way that makes sense but also fulfills my need to make things complicated. In the previous rewrite, I used slot amounts for specific parts of the body, ex. a jacket would take 1 slot on the upper arm but a shirt would only take up half since it's presumably thinner. This enabled different items to share the same body-space. Instead of this, I will keep body slots but use layers, so that two clothes/armors can share the same item space but not if they're the same layer. This will also let me do things like 'you can't put your undershirt on over your chestplate! take that off first.' If that gives you an idea of how complicated I want this engine to be, and you're not scared, you're my kinda people.

### Stage 4 - Basic Puzzles and Quests
Puzzles and Quests and the same thing: the player needs to do a certain number of things, possibly in a specific order, possibly in different locations, in order to satisfy a requirement. Once that is satisfied, something happens.

* Gamestate could have a dict attribute. These attributes will affect other items in the world, and possibly other people, changing their statuses.
* Interactable items (from stage 2) will be used, as well as locked doors, searching, etc. 

### Stage 5 - Game Menu, Saving, Loading, General Interface

* Once the core mechanics are finished, the game will need a way to save and load the gamestate as well as have a menu to manage those things. Saving and Loading are not something I've done before, and I don't know how other python games or text games in general do it, so I'll do some research before that's done.
* The game will need a pre-game menu, a help file, and an in-game menu to see inventory and eventually stats and the journal.
* Possibly also going to add a map, but I really don't know how that's going to be done yet.

### Beta Release

At this point, I would consider the basic engine ready to go. There would be no combat or dialogue, but quests and puzzles could be strung together into a basic story for a satisfying enough game. 

But I want more.

### Stage ? - Dialogue
I want a Morrowind-style dialogue system. Haven't played morrowind? Don't know what I mean? Let me explain.

* The game has a list of topics, and people have varying degrees of knowledge on those topics. 
* The player knows certain topics, and can ask about them by keyword. 
* Sometimes discovering things in the game or talking to people can unlock new keywords to ask about.
* Dialogue will be its own sub-loop like combat. 
* The player will have a journal to review certain topics.

### Stage ? - Combat
In equipment, I decided specifically not to add weapons and armor because I don't know how I want combat and health and stats to work. The combat system will be a major undertaking. I'm not sure how i'll do it but it will definitely not be a turn-based system. Part of me wants to do it like runescape, where you have different combat styles you can change on the fly.

### Stage ? - Character Creation
I want so much customizability here by the time people are done they've forgotten there's a game waiting for them.
