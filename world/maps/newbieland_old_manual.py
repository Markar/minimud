
#
@dig/teleport Newbieland;newbie#01 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yOutside of the city
#
@spawn scrawny_gnoll
#
@sethome gnoll = newbie#01
#


@dig/teleport Newbieland;newbie#02 : typeclasses.rooms.Room = south;s,north;n
#
@desc |ySouth of the city, there are dangerous foes about.
#


@dig/teleport Newbieland;newbie#03 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yYou smell the scent of gnolls, better be careful.
#


@dig/teleport Newbieland;newbie#04 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yYou smell the scent of gnolls, better be careful.
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#04
#
@dig/teleport Newbieland;newbie#05 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yYou smell the scent of gnolls, better be careful.
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#05
#

@dig/teleport Newbieland;newbie#06 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yYou smell the scent of gnolls, better be careful.
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#06
#


@dig/teleport Newbieland;newbie#07 : typeclasses.rooms.Room = south;s,north;n
#
@desc |yYou hear something like bones crackling.
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#07
#


@dig/teleport Newbieland;newbie#08 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yYou hear something like bones crackling.
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#08
#


@dig/teleport Newbieland;newbie#09 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yYou hear something like bones crackling.
#
@spawn SCRAWNY_GNOLL
#
@sethome gnoll = newbie#09
#


@dig/teleport Newbieland;newbie#10 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yYou hear something like bones crackling.
#


@dig/teleport Newbieland;newbie#11 : typeclasses.rooms.Room = west;w,east;e
#
@desc |yYou hear something like bones crackling.
#
open north;n,south;s = newbie#11
#
open west;w,east;e = newbie#06
#
@create/drop scrawny gnoll;gnoll
#
@sethome gnoll = newbie#11
#


@dig/teleport Newbieland;newbie#12 : typeclasses.rooms.Room = north;n,south;s
#
@desc |yYou smell the scent of gnolls, better be careful.
#
open north;n,south;s = newbie#03
#
en west;w,east;e = newbie#05
#


@dig/teleport Newbieland;newbie#13 : typeclasses.rooms.Room = east;e,west;w
#
@desc |yYou smell the scent of gnolls, better be careful.
#
open north;n,south;s = newbie#02
#
open south;s,north;n = newbie#10
#