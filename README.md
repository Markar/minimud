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

# Bomb all in limbo
py _ = [obj.delete() for obj in self.search("#2").contents]

# Add maps
evennia xyzgrid add world.maps.mystical_forest
evennia xyzgrid add world.maps.chessboard
evennia xyzgrid add world.maps.training_grounds
evennia xyzgrid add world.maps.crushbone
evennia xyzgrid add world.maps.youtube
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

# open_xyz_exits.py

### DELETE ROOMS
from typeclasses.rooms import NewbieSnake
all = NewbieGoblin.objects.all()

for x in all:
    caller.msg(f"x: {x}")
    x.delete()

### RESET LOCKS
 self.caller.tags.add("player", category="type")
 from evennia import search_object
 bark = search_object("Bark")[0]
 bark.locks.add("call:false(); control:perm(Developer); delete:id(3) or perm(Admin);drop:holds(); edit:pid(3) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid(3) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()")
 
 # The ID must match the player's account: so 9 for this account
 Name/key: Pits (#6827)
 Typeclass: PlayerCharacter (typeclasses.characters.PlayerCharacter)
 Sessions: #37
 Account: Chummer (#9)
 #
 chummer.locks.add("call:false(); control:perm(Developer); delete:id(9) or perm(Admin);drop:holds(); edit:pid(9) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid(9) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()")

 pits.locks.add("call:false(); control:perm(Developer); delete:id(9) or perm(Admin);drop:holds(); edit:pid(9) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid(9) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()")

bark.locks.add("call:false(); control:perm(Developer); delete:id(10) or perm(Admin);drop:holds(); edit:pid(10) or perm(Admin); examine:perm(Builder); get:false(); puppet:id(4270) or pid(10) or perm(Developer) or pperm(Developer); teleport:perm(Admin); teleport_here:perm(Admin); tell:perm(Admin); view:all()")

### SEARCH BY TAG
  hasPlayerTags = caller.tags.has("player", "status")

### SPAWN OBJECT BY PROTOTYPE IN CODE
 corpse = {
     "key":"a corpse",
     "typeclass": "typeclasses.corpse.Corpse",
     "desc": "A small corpse",
     "location": self.caller.location
 }
 spawner.spawn(corpse)

### USE SPAWNER IN CODE
 objs = spawner.spawn(*list(search_tag("MOB_CORPSE")))
 for obj in objs:
     self.caller.msg(f"obj: {obj}")
     obj.location = self.location
        
### TEST FUNCTION CALL
msg = self.caller.get_npc_attack_emote(self.caller, 4, "fart")

### SET LOCAL KEY
 self.caller.location.key = "Millennium Square"
    py
        room = self.search("688")
        room.key = "Sunlit Meadow"

### DELETE CMDSET ON PLAYER
 self.caller.cmdset.delete(ChangelingCmdSet)

### SET ROOM KEY
 py setattr(here, "key", "Nexus Road - CyberBank HQ")


for room in MobRoom.objects.all_family():
    room.respawn_mobs()
    
 batch_update_objects_with_prototype 