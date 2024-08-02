steps to run
python -m venv .venv
Mac: source .venv/bin/activate 
Win: cd .venv/Scripts, ./Activate

superuser for minimud
markar
werty678

\\wsl.localhost\Ubuntu\home\mark\home\muddev\evennia-minimud\server

# Delete the current combat script, freeing up related variables
py here.scripts.get('combat').delete()
>>> here.scripts.get('combat').delete()
(1, {'scripts.CombatScript': 1})


evennia xyzgrid add world.maps.newbie_land
evennia xyzgrid 

Set an attribute on a room in game
py setattr(here, "key", "Training Grounds")

@tel town#15
#
@dig/teleport A vortex of swirling Chaos;chaos#1 : typeclasses.rooms.Room = enter,vortex
#
@desc |yA swirling vortex of pure Chaos. You can jump through the vortex to get back to the safety of town, or you can choose to explore the realm.
#


#
@dig/teleport In front of a chessboard;chaos#2 : typeclasses.rooms.Room = east;e,west;w
#
@desc |gIn front of you stands a gigantic chessboard, but with real monsters instead of game pieces. It looks pretty dangerous.
#
@open chessboard = (1,1,chessboard)
#
chessboard
#
@open leave = chaos#2