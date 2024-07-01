from evennia import create_object
from typeclasses import rooms, exits

# rooms
meadow = create_object(rooms.Room, key="Meadow")
forest = create_object(rooms.Room, key="Forest")

# exits
create_object(exits.Exit, key="east", location=meadow, destination=forest)
create_object(exits.Exit, key="west", location=forest, destination=meadow)
