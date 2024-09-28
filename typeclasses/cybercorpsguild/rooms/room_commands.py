from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from typeclasses.cybercorpsguild.cybercorps_commands import CybercorpsCmdSet
from typeclasses.cybercorpsguild.cybercorps_wares import WaresObjects
from typeclasses.cybercorpsguild.cyber_implants import ImplantObjects
from evennia import TICKER_HANDLER as tickerhandler

# from commands.shops import ShopCmdSet
# from evennia.utils import create
# from typeclasses.scripts import RestockScript


class CmdJoinCybercorps(Command):
    """
    Join the Cybercorps Mega corporation
    """

    key = "join cybercorps"

    def func(self):
        caller = self.caller
        if caller.db.guild == "adventurer":
            caller.msg(f"|rYou sign up to join the Cybercorps Mega Corporation")
            caller.swap_typeclass(
                "typeclasses.cybercorps.Cybercorps",
                clean_attributes=False,
            )

            caller.cmdset.add(CybercorpsCmdSet, persistent=True)

            try:
                tickerhandler.remove(
                    interval=6,
                    callback=caller.at_pc_tick,
                    idstring=f"{caller}-regen",
                    persistent=True,
                )
                tickerhandler.remove(
                    interval=60 * 5,
                    callback=caller.at_superpower_tick,
                    idstring=f"{caller}-superpower",
                    persistent=True,
                )
            except ValueError:
                print(f"tickerhandler.remove failed")
        else:
            caller.msg(f"|rYou are already in a guild")


# region Leave Cybercorps
class CmdLeaveCybercorps(Command):
    """
    Leave the Cybercorps Mega Corporation
    """

    key = "leave cybercorps"

    def strip(self):
        caller = self.caller
        caller.cmdset.delete(CybercorpsCmdSet)
        del caller.db.docwagon
        del caller.db.skills
        del caller.db.guild_level
        del caller.db.strategy
        del caller.db.wares
        del caller.db.melee_weapon
        del caller.db.ranged_weapon
        del caller.db.adaptive_armor
        del caller.db.nano_reinforced_skeleton
        del caller.db.nrs_amount
        del caller.db.adrenaline_boost

        try:
            tickerhandler.remove(
                interval=6,
                callback=caller.at_tick,
                idstring=f"{caller}-regen",
                persistent=True,
            )
            tickerhandler.remove(
                interval=60 * 5,
                callback=caller.at_docwagon_tick,
                idstring=f"{caller}-superpower",
                persistent=True,
            )
        except ValueError:
            print(f"tickerhandler.remove failed")

        return

    def func(self):
        caller = self.caller
        if caller.db.guild == "cybercorps":
            self.strip()
            caller.swap_typeclass("typeclasses.characters.PlayerCharacter")
            caller.msg(f"|rYou leave the Cybercorps Mega Corporation")
        else:
            caller.msg(f"|rYou are already an adventurer")


# region List Wares
class CmdListWares(Command):
    """
    List wares available for purchase from the Cybercorps Mega Corporation
    """

    key = "list"

    def func(self):
        caller = self.caller
        table = EvTable(
            f"|wWares", f"|wSkill", f"|wRank", f"|wCost", f"|wLevel", border="table"
        )
        for ware in WaresObjects.values():
            if ware.name in caller.db.wares:
                table.add_row(
                    f"|Y{ware.name}",
                    f"|Y{ware.skill}",
                    f"|Y{ware.skill_req}",
                    f"|Y{ware.cost}",
                    f"|Y{ware.rank}",
                )
            else:
                table.add_row(
                    f"|G{ware.name}",
                    f"|G{ware.skill}",
                    f"|Y{ware.skill_req}",
                    f"|G{ware.cost}",
                    f"|G{ware.rank}",
                )

        caller.msg(str(table))


# region list implants
class CmdListImplants(Command):
    """
    List implants available for purchase from the Cybercorps Mega Corporation
    """

    key = "list"

    def func(self):
        caller = self.caller
        table = EvTable(
            f"|wImplant", f"|wSkill", f"|wRank", f"|wCost", f"|wLevel", border="table"
        )
        for implant in ImplantObjects:
            table.add_row(
                f"|Y{implant['name']}",
                f"|Y{implant['skill']}",
                f"|Y{implant['skill_req']}",
                f"|Y{implant['cost']}",
                f"|Y{implant['rank']}",
            )

        caller.msg(str(table))


# region buy implants
class CmdBuyImplant(Command):
    """
    Buy implant from the Cybercorps Mega Corporation
    """

    key = "buy"

    def func(self):
        caller = self.caller
        implant = self.args.strip().lower()
        owned_implants = getattr(caller.db, "implants", [])

        if caller.db.guild != "cybercorps":
            caller.msg(
                f"|rYou need to be part of the Cybercorps Mega Corporation to buy implants."
            )
            return

        if not implant:
            caller.msg(f"|rUsage: buy <implant>")
            return

        if implant in owned_implants:
            caller.msg(f"|rYou already have the {implant}.")
            return

        for obj in ImplantObjects:
            if obj["name"].lower() == implant:
                skill_req = obj["skill_req"]
                skill = obj["skill"]
                name = obj["name"]
                rank = obj["rank"]
                cost = obj["cost"]

                if caller.db.guild_level < obj["rank"]:
                    caller.msg(
                        f"|rYou need to be guild level {rank} to buy the {name}."
                    )
                    return

                if caller.db.skills.get(obj["skill"], 0) < obj["skill_req"]:
                    caller.msg(
                        f"|rYou need to have at least {skill_req} ranks in {skill} to buy the {name}."
                    )
                    return

                if caller.db.coins < obj["cost"]:
                    caller.msg(
                        f"|rYou need {cost - caller.db.coins} more coins to buy the {name}."
                    )
                    return

                caller.db.implants.append(name.lower())
                caller.db.coins -= cost
                caller.msg(
                    f"|gYou buy the {name} from the Cybercorps Mega Corporation."
                )
                return

        caller.msg(f"|rYou can't buy the {name}.")
        return


# region buy wars
class CmdBuyWares(Command):
    """
    Buy wares from the Cybercorps Mega Corporation
    """

    key = "buy"

    def func(self):
        caller = self.caller
        ware = self.args.strip().lower()

        if caller.db.guild != "cybercorps":
            caller.msg(
                f"|rYou need to be part of the Cybercorps Mega Corporation to buy wares."
            )
            return
        if not ware:
            caller.msg(f"|rUsage: wares buy <ware>")
            return

        if ware in caller.db.wares:
            caller.msg(f"|rYou already have the {ware}.")
            return

        for obj in WaresObjects.values():
            if obj.name.lower() == ware:
                ware = obj

                if caller.db.guild_level < ware.rank:
                    caller.msg(
                        f"|rYou need to be guild level {ware.rank} to buy the {ware.name}."
                    )
                    return
                if caller.db.skills.get(ware.skill, 0) < ware.skill_req:
                    caller.msg(
                        f"|rYou need to have at least {ware.skill_req} ranks in {ware.skill} to buy the {ware.name}."
                    )
                    return

                if caller.db.coins < ware.cost:
                    caller.msg(
                        f"|rYou need {ware.cost - caller.db.coins} more coins to buy the {ware.name}."
                    )
                    return

                caller.db.wares.append(ware.name)
                caller.db.coins -= ware.cost
                caller.msg(
                    f"|gYou buy the {ware.name} from the Cybercorps Mega Corporation."
                )
                return

        caller.msg(f"|rYou can't buy the {ware.name}.")
        return


class CybercorpsWaresCmdSet(CmdSet):
    key = "Cybercorps Wares CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdBuyWares)
        self.add(CmdListWares)


class CybercorpsImplantsCmdSet(CmdSet):
    key = "Cybercorps Implants CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        self.add(CmdBuyImplant)
        self.add(CmdListImplants)


# class CyberShop(RoomParent, DefaultRoom):
#     """
#     A grid-aware room that has built-in shop-related functionality.
#     """

#     def at_object_creation(self):
#         """
#         Initialize the shop inventory and commands
#         """
#         super().at_object_creation()

#         # add the shopping commands to the room
#         self.cmdset.add(ShopCmdSet, persistent=True)
#         # create an invisible, inaccessible storage object
#         self.db.storage = create.object(
#             key="shop storage",
#             locks="view:perm(Builder);get:perm(Builder);search:perm(Builder)",
#             home=self,
#             location=self,
#         )

#         self.db.inventory = [
#             ("CYBER_CHESTGUARD", 3),
#             ("CYBER_LEG_GUARDS", 3),
#             ("CYBER_BOOTS", 3),
#         ]
#         self.scripts.add(RestockScript, key="restock", autostart=True)

#     def add_stock(self, obj):
#         """
#         Adds new objects to the shop's sale stock
#         """
#         if storage := self.db.storage:
#             # only do this if there's a storage location set
#             obj.location = storage
#             # price is double the sale value
#             val = obj.db.value or 0
#             obj.db.price = val * 2
#             return True
#         else:
#             return False
