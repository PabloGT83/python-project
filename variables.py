# define rooms and items

#Game Room
couch = {
    "name": "couch",
    "type": "furniture_hint",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}



hint_1 = {
    "name": "Envolope 1",
    "type": "hint",
    "message": "Go back to basics, which is the 4th decimal of pi?",
    "anwer": 6
}


#Bedroom 1
door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

queenbed = {
    "name": "queenbed",
    "type": "furniture",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

#Bedroom 2

door_b = {
    "name": "door b",
    "type": "door",
}

doublebed = {
    "name": "doublebed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

#Living Room

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

diningtable = {
    "name": "Dining Table",
    "type": "furniture",
}

#Rooms:

game_room = {
    "name": "game room",
    "type": "room",
}

bed_room1 = {
    "name": "bedroom 1",
    "type": "room",
}

bed_room2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [game_room,bed_room1,bed_room2,living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "couch":[hint_1],
    "outside": [door_d],
    "door a": [game_room, bed_room1],
    "bedroom 1":[door_a, queenbed, door_b, door_c],
    "queenbed": [key_b],
    "door b": [bed_room1,bed_room2],
    "door c": [bed_room1,living_room],
    "door d":[living_room, outside],
    "bedroom 2":[doublebed,door_b, dresser],
    "doublebed": [key_c],
    "dresser":[key_d],
    "living room": [door_c, diningtable, door_d] 
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "hints_read": [],
    "lifes": 3,
}