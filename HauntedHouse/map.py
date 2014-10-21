from items import *

entrance_hall = {
    "name": "Entrance Hall",

    "description":
    """You are in the entrance hall to the Manor House. The room is dark and dank, 
the stench of damp is overpowering. Every surface is covered with a thick layer 
of dust, undisturbed even by your footsteps. Spiders have long since taken up 
residence, their webs cling to the walls and across the corners of the room. 
Each step you take it matched by the groan of the floor boards, scuttling 
above your head... perhaps the house is not a deserted as you first thought. 

You try the door once again, but it's firmly bolted shut. Looks like you're 
going to need a key to escape. 

There are only two exits: North will take you to the kitchen. 
West to the Lounge.""",
    "description2":"",

    "exits": {"north": "Kitchen", "west": "Lounge"},

    "items": [item_fuse]
}

kitchen = {
    "name": "kitchen",

    "description":
    """The kitchen door opens with a heavy shove, sending a plague of 
rats scurrying away. But immediately upon entering, the stench of 
long forgotten food and an infestation of rats is nauseating. 

To the north of the kitchen you can vaguely make out the back garden
through the dirty windows. To the east there looks to be some 
kind of industrial freezer. West will take you to the dining room. 
South back to the entrance hall.""",
    "description2":"",
    "exits": {"north": "Backyard", "east": "Freezer", "west": "Dining", "south": "Hall"},

    "items": [item_torch]
}

freezer = {
    "name": "the kitchen freezer",

    "description":
    """The cool air hits you as you enter. But the cold has only 
preserved an odd stale smell.There's something on the floor, 
but it's too dark. You need some light. There is only one exit, back 
into the kitchen.""",
    "description2":"",
    "exits": {"west": "Kitchen"},

    "items": []
}

garage = {
    "name": "the garage",

    "description":
    """You are in the garage. Amongst a horde of odd machinery 
parts and decomposing boxes - nothing that seems to be any 
use. You continue to search...there must be something around 
here. You come across an empty fuse box. Perhaps if you can 
find the fuse you can restore the power? """,
    "description2":"",
    "exits": {"north": "Backyard"},

    "items": []
}

lounge = {
    "name": "the lounge",

    "description":
    """The lounge is in a decrepit state; furniture is
over-turned and broken, upholstery has been slashed. There 
are paintings on the wall - faded landscapes and creepy
portraits - all bearing the same violent slashes. You move 
towards the largest portrait, inspecting the cut marks 
a little closer. You notice there is something hidden 
behind the painting...it's a safe, built into the wall. 
It's locked.You'll need to pick the lock. """,
    "description2":"",
    "exits": {"north": "Dining"},

    "items": [item_map]
}

dining_room = {
    "name": "the dining room",

    "description":
    """Glass and china crack under your feet as you 
enter the dining room. The floor is littered with 
the remains of a large dining service. The long 
table has been pushed against the wall, its surface 
marred with dents and scratches. """,
    "description2":"",   
    "exits": {"north": "Backyard", "east": "Kitchen"},

    "items": [item_glass]
}

backyard = {
    "name": "the backyard",

    "description":
    """The back yard resembles a jungle. Overgrown and untended. Surrounding 
the entire garden is a brick wall, far too high to climb over. The only
light available is that of the moon, illuminating the heaps of rubbish amongst
the plants. You wonder if there is anything of use? 

Back south is the kitchen. To the east is the garage.""",
    "description2":"",
    "exits": {"south": "Kitchen", "east": "Garage"},

    "items": []
}

rooms = {
    "Kitchen": kitchen, 
    "Hall": entrance_hall, 
    "Freezer": freezer, 
    "Garage": garage, 
    "Lounge": lounge, 
    "Dining": dining_room, 
    "Backyard": backyard
}
