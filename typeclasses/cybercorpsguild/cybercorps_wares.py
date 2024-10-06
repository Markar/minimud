from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from random import uniform, randint
from typeclasses.cybercorpsguild.cybercorps_attack import CybercorpsAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes
from typeclasses.utils import PowerCommand

slowdown = 5


def checkAdrenalineBoost(self, wielder):
    duration = wielder.db.adrenaline_boost.get("duration", 0)

    if duration > 0:
        wielder.adjust_ep(-20)
        wielder.db.adrenaline_boost["duration"] -= 1
        if duration == 1:
            wielder.db.adrenaline_boost = {"active": False, "duration": 0}
            wielder.msg(
                f"|CYour adrenaline boost fades, leaving you feeling drained.|n"
            )
            return False
        else:
            wielder.msg(f"|CWith your adrenaline surging, you strike again!|n")
            return True

    return None


# region Guild Level Weapons
class HandRazors(CybercorpsAttack):
    """
    Hand razors are a pair of retractable blades that are attached to the
    user's hands. They are used for close combat and can be used to slash
    and stab at enemies. Hand razors are often used by assassins and other
    stealthy characters who need to be able to quickly dispatch their foes.
    """

    speed = 4
    energy_cost = 0
    name = "hand razors"
    cost = 0
    rank = 1
    skill = "standard weapons"
    skill_req = 1
    short = "A pair of retractable hand razors."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.20
        dmg = 3 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("hand_razors"):
            return
        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = self.speed
            wielder.adjust_ep(-self.energy_cost)

            boost = checkAdrenalineBoost(self, wielder)

            if boost:
                dmg = self._calculate_melee_damage(wielder)
                target.at_damage(wielder, dmg, "edged", "hand_razors")
            if boost == None:
                speed = slowdown

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "hand_razors")
            wielder.cooldowns.add("hand_razors", speed)


# region Shock Hand
class ShockHand(CybercorpsAttack):
    """
    The shock hand is a cybernetic enhancement that allows the user to
    deliver a powerful electric shock to their enemies. The shock hand
    is often used by law enforcement and security personnel to subdue
    criminals and other threats. The shock hand can be used to deliver
    a non-lethal shock to incapacitate a target, or a lethal shock to
    kill them outright.
    """

    speed = 4
    energy_cost = 0
    name = "shock hand"
    skill = "energy weapons"
    skill_req = 2
    rank = 5
    cost = 5
    short = "A cybernetic shock hand."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str * 0.25 + dex * 0.25
        dmg = 10 + glvl * 0.5 + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(self.rank, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if not wielder.cooldowns.ready("shock_hand"):
            return

        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        speed = self.speed
        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "lightning", "shock_hand")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "lightning", "shock_hand")
        wielder.cooldowns.add("shock_hand", speed)


# region Stealth Blade
class StealthBlade(CybercorpsAttack):
    """
    The stealth blade is a high-tech weapon that is designed for covert
    operations and stealthy assassinations. The stealth blade is equipped
    with a cloaking device that makes it nearly invisible to the naked eye,
    allowing the user to strike from the shadows without being detected.
    The stealth blade is often used by spies, assassins, and other operatives
    who need to eliminate targets quietly and efficiently.
    """

    speed = 4
    energy_cost = 0
    name = "stealth blade"
    skill = "standard weapons"
    skill_req = 4
    cost = 10
    rank = 22
    short = "A high-tech stealth blade."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.25
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(self.rank, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        if not wielder.cooldowns.ready("stealth_blade"):
            return

        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "stealth_blade")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "stealth_blade")
        wielder.cooldowns.add("stealth_blade", speed)


# region NanoBlade
class NanoBlade(CybercorpsAttack):
    """
    The nanoblade is a high-tech weapon that uses nanotechnology to create
    a blade that is incredibly sharp and durable. The nanoblade is capable
    of cutting through almost any material with ease, making it a deadly
    weapon in the hands of a skilled user. The nanoblade is often used by
    elite soldiers and assassins who need a weapon that can penetrate armor
    and shields.

    Strength, Dexterity
    """

    speed = 4
    energy_cost = 0
    name = "nanoblade"
    skill = "standard weapons"
    skill_req = 6
    cost = 5
    rank = 28
    short = "A high-tech nanoblade."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(self.rank, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        if not wielder.cooldowns.ready("nanoblade"):
            return

        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "nanoblade")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "nanoblade")
        wielder.cooldowns.add("nanoblade", speed)


# region Energy Sword
class EnergySword(CybercorpsAttack):
    """
    The energy sword is a high-tech weapon that uses a blade made of pure
    energy to slice through armor and shields with ease. The energy sword
    is often used by elite soldiers and special forces operatives who need
    a weapon that can cut through almost anything. The energy sword is
    capable of delivering devastating blows that can cleave through multiple
    enemies in a single strike.
    """

    speed = 3
    energy_cost = 0
    name = "energy sword"
    skill = "energy weapons"
    skill_req = 3
    rank = 13
    cost = 20
    short = "A melee weapon with a blade made of pure energy."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(self.rank, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        if not wielder.cooldowns.ready("energy_sword"):
            return

        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "energy_sword")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "energy_sword")
        wielder.cooldowns.add("energy_sword", speed)


# region Graviton Hammer
class GravitonHammer(CybercorpsAttack):
    """
    The graviton hammer is a heavy weapon that uses gravitational forces to
    crush enemies with immense power. It is often used in military operations
    for its ability to take out armored vehicles and fortified positions.
    """

    speed = 6
    energy_cost = 5
    name = "graviton hammer"
    skill = "heavy weapons"
    skill_req = 7
    rank = 30
    cost = 4
    short = "A heavy weapon that uses gravitational forces to crush enemies."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str * 0.6
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)
        min = 30 + dex

        damage = int(uniform(min, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("graviton_hammer"):
            return

        if not wielder.db.ep >= self.energy_cost:
            return

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "blunt", "graviton_hammer")
        if boost == None:
            speed = slowdown

        wielder.db.ep -= self.energy_cost

        if randint(1, 100) < 30:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg * 1.25, "energy", "graviton_hammer_hit")

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "blunt", "graviton_hammer")
        wielder.cooldowns.add("graviton_hammer", speed)


# region Chainblade
class ChainBlade(CybercorpsAttack):
    """
    A heavy sword with a motorized chain running along its edge, designed
    to slice through enemies with ease. It is often used in close-quarters
    combat for its ability to cut through armor and shields with ease.
    """

    speed = 6
    energy_cost = 0
    name = "chain blade"
    skill = "heavy weapons"
    skill_req = 4
    rank = 24
    cost = 1
    short = "A melee weapon with a retractable chain."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(self.rank, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        if not wielder.cooldowns.ready("chain_blade"):
            return

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "chain_blade")
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "chain_blade")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        dmg2 = self._calculate_melee_damage(wielder)

        target.at_damage(wielder, dmg, "edged", "chain_blade")
        target.at_damage(wielder, dmg2, "edged", "chain_blade")
        wielder.cooldowns.add("chain_blade", speed)


# region Shockwave Hammer
class ShockwaveHammer(CybercorpsAttack):
    """
    The shockwave hammer is a heavy weapon that generates shockwaves upon impact,
    capable of knocking down enemies and destroying structures. It is often used
    in military operations for its ability to create chaos on the battlefield.
    """

    speed = 6
    energy_cost = 5
    name = "shockwave hammer"
    skill = "heavy weapons"
    skill_req = 2
    rank = 14
    cost = 4
    short = "A heavy weapon that generates shockwaves upon impact."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value

        stat_bonus = str * 0.5
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = 10 + int(uniform(self.rank, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        speed = self.speed

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("shockwave_hammer"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        boost = checkAdrenalineBoost(self, wielder)

        if boost:
            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "blunt", "shockwave_hammer")
        if boost == None:
            speed = slowdown

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "blunt", "shockwave_hammer")
        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "blunt", "shockwave_hammer")
        wielder.cooldowns.add("shockwave_hammer", speed)


# region Tactical Shotgun
class TacticalShotgun(CybercorpsAttack):
    """
    The tactical shotgun is a versatile weapon that is effective at close
    range combat. It fires a spread of high-impact projectiles that can
    take down multiple targets with a single shot. The tactical shotgun
    is often used by law enforcement and military personnel for breaching
    and clearing rooms, as well as for crowd control and riot suppression.

    Strength, Standard
    """

    speed = 6
    energy_cost = 1
    name = "tactical shotgun"
    skill = "standard weapons"
    skill_req = 2
    cost = 5
    rank = 11
    short = "A tactical shotgun."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        miss_rate = 30 - (glvl * 0.25) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str * 0.25 + dex * 0.25
        dmg = 30 + glvl + stat_bonus + self.rank * (glvl / 10)
        dmg = int(uniform(dmg * 0.5, dmg) * 0.36)

        # divide the damage by the number of pellets and increase the total damage
        damage = 2 + dmg
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        #
        if not wielder.cooldowns.ready("tactical_shotgun"):
            return
        if wielder.db.strategy == "melee":
            wielder.db.ep -= self.energy_cost

            dmg1 = self._calculate_ranged_damage(wielder)
            dmg2 = self._calculate_ranged_damage(wielder)
            dmg3 = self._calculate_ranged_damage(wielder)

            target.at_damage(wielder, dmg1, "edged", "tactical_shotgun")
            target.at_damage(wielder, dmg2, "edged", "tactical_shotgun")
            target.at_damage(wielder, dmg3, "edged", "tactical_shotgun")

            wielder.cooldowns.add("tactical_shotgun", self.speed)


# region Smart Gun
class SmartGun(CybercorpsAttack):
    """
    The smart gun is a firearm that is equipped with advanced targeting
    systems and AI assistance to enhance accuracy and tracking. The smart
    gun can automatically adjust its aim to compensate for factors such
    as wind, distance, and target movement, making it ideal for long-range
    combat. The smart gun is often used by snipers and marksmen who need
    to make precise shots under challenging conditions.
    """

    speed = 3
    energy_cost = 1
    name = "smart gun"
    skill = "standard weapons"
    skill_req = 5
    rank = 25
    cost = 1
    short = "An AI-enabled smart gun."
    type = "ranged"
    ammo = 8

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str * 0.25 + dex * 0.5
        dmg = 5 + stat_bonus + glvl * 1.5

        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)
        damage = int(uniform(dmg * 0.5, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("smart_gun"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "melee":
            wielder.db.ep -= self.energy_cost

            dmg1 = self._calculate_ranged_damage(wielder)
            dmg2 = self._calculate_ranged_damage(wielder)

            target.at_damage(wielder, dmg1, "edged", "smart_gun")
            target.at_damage(wielder, dmg2, "edged", "smart_gun")

            wielder.cooldowns.add("smart_gun", self.speed)


# region Rail Pistol
class RailPistol(CybercorpsAttack):
    """
    The rail pistol is a compact railgun that fires metal slugs at hypersonic speeds.
    The rail pistol is often used by elite soldiers and special forces operatives who
    need a weapon that can penetrate armor and shields with ease. The rail pistol is
    capable of delivering devastating blows that can cleave through multiple enemies
    in a single strike.
    """

    speed = 3
    energy_cost = 1
    name = "rail pistol"
    skill = "standard weapons"
    skill_req = 3
    rank = 20
    cost = 2
    short = "A compact railgun that fires metal slugs."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str * 0.25 + dex * 0.5
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.5, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("rail_pistol"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "rail_pistol")
        target.at_damage(wielder, dmg2, "edged", "rail_pistol")
        wielder.cooldowns.add("rail_pistol", self.speed)


# region Energy Weapons


# region Laser Pistol
class LaserPistol(CybercorpsAttack):
    """
    The laser pistol is a compact sidearm that emits concentrated laser beams,
    ideal for precision targeting. The laser pistol is often used by law enforcement
    and security personnel for self-defense and crowd control. The laser pistol is
    capable of delivering rapid-fire shots that can penetrate armor and shields with
    ease, making it a versatile weapon for a variety of combat situations.
    """

    speed = 3
    energy_cost = 1
    name = "laser pistol"
    skill = "energy weapons"
    skill_req = 1
    rank = 3
    cost = 1
    short = "A compact sidearm that emits concentrated laser beams."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 75 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str * 0.25 + dex * 0.25
        dmg = glvl + stat_bonus + self.rank * (glvl / 10)

        damage = 10 + int(uniform(dmg * 0.5, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("laser_pistol"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost
        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "laser_pistol")
        target.at_damage(wielder, dmg2, "energy", "laser_pistol")
        wielder.msg(f"[ Cooldown: {self.speed} seconds ]")
        wielder.cooldowns.add("laser_pistol", self.speed)


# region Photon Blaster
class PhotonBlaster(CybercorpsAttack):
    """
    The photon blaster is a high-tech weapon that fires concentrated beams
    of light, capable of cutting through metal and flesh alike. The photon
    blaster is often used by elite soldiers and special forces operatives
    who need a weapon that can penetrate armor and shields with ease. The
    photon blaster is capable of delivering devastating blows that can cleave
    through multiple enemies in a single strike.
    """

    speed = 3
    energy_cost = 3
    name = "photon blaster"
    skill = "energy weapons"
    skill_req = 4
    rank = 21
    cost = 2
    short = "A weapon that fires concentrated beams of light."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.5, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("photon_blaster"):
            return

        # Subtract energy and apply damage to target before their defenses

        speed = 3
        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)

        target.at_damage(wielder, dmg, "energy", "photon_blaster")
        target.at_damage(wielder, dmg2, "energy", "photon_blaster")
        wielder.cooldowns.add("photon_blaster", speed)


# region Plasma Cannon
class PlasmaCannon(CybercorpsAttack):
    """
    The plasma cannon is a heavy weapon that fires large plasma projectiles,
    causing massive damage to structures and vehicles. The plasma cannon is
    often used by military forces and security personnel for anti-vehicle
    and anti-structure operations. The plasma cannon is capable of delivering
    devastating blows that can obliterate enemy fortifications and armored
    vehicles with ease.
    """

    speed = 6
    energy_cost = 25
    name = "plasma cannon"
    skill = "heavy weapons"
    skill_req = 6
    rank = 29
    cost = 3
    short = "A heavy weapon that fires large plasma projectiles."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        dex = wielder.traits.dex.value
        str = wielder.traits.str.value

        miss_rate = 25 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.9, dmg * 1.25))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("plasma_cannon"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "plasma_cannon")
        wielder.cooldowns.add("plasma_cannon", self.speed)


# region Gauss Cannon
class GaussCannon(CybercorpsAttack):
    """
    The gauss cannon is a powerful railgun that uses electromagnetic forces
    to launch projectiles at incredible speeds. The gauss cannon is often used
    by elite soldiers and special forces operatives who need a weapon that can
    penetrate armor and shields with ease. The gauss cannon is capable of delivering
    devastating blows that can cleave through multiple enemies in a single strike.
    """

    speed = 6
    energy_cost = 25
    name = "gauss cannon"
    skill = "heavy weapons"
    skill_req = 5
    rank = 27
    cost = 5
    short = "A powerful railgun that uses electromagnetic forces."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 25 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.9, dmg * 1.25))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("gauss_cannon"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "gauss_cannon")
        wielder.cooldowns.add("gauss_cannon", self.speed)


# region Pulse Rifle
class PulseRifle(CybercorpsAttack):
    """
    The pulse rifle is a versatile weapon that fires bursts of energy pulses,
    effective against both organic and synthetic targets. The pulse rifle is
    often used by military forces and security personnel for anti-personnel
    and anti-robot operations. The pulse rifle is capable of delivering rapid-fire
    shots that can penetrate armor and shields with ease, making it a versatile
    weapon for a variety of combat situations.
    """

    speed = 3
    energy_cost = 6
    name = "pulse rifle"
    skill = "energy weapons"
    skill_req = 6
    rank = 26
    cost = 3
    short = "A versatile weapon that fires bursts of energy pulses."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        # divide the damage by the number of shots and increase the total damage
        damage = int(uniform(dmg * 0.5, dmg) * 0.55)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("pulse_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "pulse_rifle")
        target.at_damage(wielder, dmg2, "energy", "pulse_rifle")
        wielder.cooldowns.add("pulse_rifle", self.speed)


# region Plasma Rifle
class PlasmaRifle(CybercorpsAttack):
    """
    The plasma rifle is a high-energy weapon that fires superheated plasma
    bolts, capable of melting through most materials. The plasma rifle is
    often used by elite soldiers and special forces operatives who need a
    weapon that can penetrate armor and shields with ease.
    """

    speed = 6
    energy_cost = 25
    name = "plasma rifle"
    skill = "energy weapons"
    skill_req = 5
    rank = 23
    cost = 4
    short = "A high-energy weapon that fires superheated plasma bolts."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.9, dmg * 1.25) * 0.35)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("plasma_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        dmg3 = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "plasma_rifle")
        target.at_damage(wielder, dmg2, "energy", "plasma_rifle")
        target.at_damage(wielder, dmg3, "energy", "plasma_rifle")
        wielder.cooldowns.add("plasma_rifle", self.speed)


# region Laser Sniper Rifle
class LaserSniperRifle(CybercorpsAttack):
    """
    The laser sniper rifle is a long-range weapon with pinpoint accuracy,
    using laser technology for silent kills. The laser sniper rifle is often
    used by elite snipers and marksmen who need to eliminate targets from a
    distance without being detected. The laser sniper rifle is capable of
    delivering precise shots that can penetrate armor and shields with ease,
    making it an ideal weapon for long-range combat.
    """

    speed = 9
    energy_cost = 30
    name = "laser sniper rifle"
    skill = "energy weapons"
    skill_req = 7
    rank = 30
    cost = 6
    short = "A long-range weapon with pinpoint accuracy."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        dex = wielder.traits.dex.value

        stat_bonus = dex
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 1, dmg * 1.5))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("laser_sniper_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "laser_sniper_rifle")
        wielder.cooldowns.add("laser_sniper_rifle", self.speed)


# region Rocket Launcher
class RocketLauncher(CybercorpsAttack):
    """
    The rocket launcher is a heavy weapon designed to fire explosive projectiles,
    capable of causing massive damage to both structures and enemies. It is often
    used in military operations for its ability to take out armored vehicles and
    fortified positions.
    """

    speed = 6
    energy_cost = 8
    name = "rocket launcher"
    skill = "heavy weapons"
    skill_req = 3
    rank = 17
    cost = 15
    short = "A heavy weapon that fires explosive projectiles."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value

        stat_bonus = str * 0.5
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("rocket_launcher"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        if randint(1, 100) < 30:
            target.at_damage(wielder, int(dmg * 1.25), "fire", "rocket_launcher_hit")
            return
        target.at_damage(wielder, dmg, "fire", "rocket_launcher")
        wielder.cooldowns.add("rocket_launcher", self.speed)


# region FlameThrower
class FlameThrower(CybercorpsAttack):
    """
    The flamethrower is a close-range weapon that projects a stream of fire,
    capable of causing severe burns to enemies and setting objects ablaze. It
    is often used in military operations for its ability to clear out enemy
    positions and create obstacles for advancing forces.
    """

    speed = 6
    energy_cost = 5
    name = "flamethrower"
    skill = "heavy weapons"
    skill_req = 1
    rank = 8
    cost = 3
    short = "A close-range weapon that projects a stream of fire."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.25
        dmg = 20 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = 2 + int(uniform(dmg * 0.5, dmg) * 0.35)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("flame_thrower"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        dmg3 = self._calculate_ranged_damage(wielder)

        target.at_damage(wielder, dmg, "fire", "flame_thrower")
        target.at_damage(wielder, dmg2, "fire", "flame_thrower")
        target.at_damage(wielder, dmg3, "fire", "flame_thrower")
        wielder.cooldowns.add("flame_thrower", self.speed)


# region Vortex AR-9
class VortexAR9(CybercorpsAttack):
    """
    The Vortex AR-9 is a state-of-the-art assault rifle equipped with a
    smart targeting system and adaptive ammunition. It is often used by
    elite soldiers and special forces operatives who need a weapon that
    can deliver precise shots under challenging conditions.
    """

    speed = 3
    energy_cost = 10
    name = "vortex ar9"
    skill = "standard weapons"
    skill_req = 7
    rank = 15
    cost = 3
    short = "A high-tech assault rifle that fires adaptive ammunition."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        miss_rate = 50 - (glvl * 0.5) - (dex * 0.25)

        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = (str + dex) * 0.33
        dmg = 10 + glvl + stat_bonus + self.rank * (glvl / 10)

        damage = int(uniform(dmg * 0.5, dmg) * 0.4)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("vortex_ar9"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return

        wielder.db.ep -= self.energy_cost

        dmg = self._calculate_ranged_damage(wielder)
        dmg2 = self._calculate_ranged_damage(wielder)
        dmg3 = self._calculate_ranged_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "vortex_ar9")
        target.at_damage(wielder, dmg2, "energy", "vortex_ar9")
        target.at_damage(wielder, dmg3, "fire", "vortex_ar9")
        wielder.cooldowns.add("vortex_ar9", self.speed)


# region Loadout
class CmdLoadout(PowerCommand):
    """
    Equip a weapon from your inventory.

    Usage:
        loadout <weapon>
    """

    key = "loadout"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        stripped_args = args.replace(" ", "")

        if not args:
            caller.msg("Usage: loadout <weapon>")
            return

        for key, value in WaresObjects.items():
            key = key.replace(" ", "")
            if key == stripped_args:
                obj = value
                if not obj.name in caller.db.wares:
                    caller.msg(f"|rYou don't have the {obj.name} in your inventory.")
                    return

                name = obj.name.replace(" ", "")

                if obj.type == "melee":
                    if name == caller.db.melee_weapon.name.replace(" ", ""):
                        caller.msg(f"|rYou already have the {obj.name} equipped.")
                        return
                    if caller.db.guild_level < obj.rank:
                        caller.msg(
                            f"|rYou need guild level {obj.rank} to equip the {obj.name}."
                        )
                        return
                    caller.db.melee_weapon = WaresObjects[args]
                    caller.msg(f"|gYou equip the {obj.name}.")
                    return

                if obj.type == "ranged":
                    if isinstance(
                        caller.db.ranged_weapon, CybercorpsAttack
                    ) and name == caller.db.ranged_weapon.name.replace(" ", ""):
                        caller.msg(f"|rYou already have the {obj.name} equipped.")
                        return

                    if caller.db.guild_level < obj.rank:
                        caller.msg(
                            f"|rYou need guild level {obj.rank} to equip the {obj.name}."
                        )
                        return
                    caller.db.ranged_weapon = WaresObjects[args]
                    caller.msg(f"|gYou equip the {obj.name}.")

        return


# region Loadout Remove
class CmdLoadoutRemove(Command):
    """
    Unequip a ware from your inventory.

    Usage:
        loadout remove <ware>
    """

    key = "loadout remove"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        melee = caller.db.melee_weapon or HandRazors
        ranged = caller.db.ranged_weapon or None

        if not args:
            caller.msg("Usage: loadout remove <ware>")
            return

        if not args in caller.db.wares:
            caller.msg(f"|rYou can't unequip {args}.")
            return

        if args == "handrazors":
            caller.msg(f"|gYou don't want to be caught without your hand razors.")
            return

        if melee.name == args:
            caller.db.melee_weapon = HandRazors()
            caller.msg(f"|gYou put the {args} away and draw your hand razors.")
            return

        if ranged and ranged.name == args:
            caller.db.ranged_weapon = None
            caller.msg(f"|gYou put the {args} away.")
            return


# region Wares
class CmdWares(Command):
    """
    List of wares available to the Cybercorps Guild.

    Usage:
        wares
        wares <item>

        Example: wares hand razors

    """

    key = "wares"
    help_category = "cybercorps"

    def func(self):
        caller = self.caller
        ware = self.args.strip().lower()

        if ware in WaresObjects.keys():
            obj = WaresObjects[ware]
            caller.msg(
                f"    |g{obj.name.title()}\n    |GCost: {obj.cost}\n|G{obj.__doc__}\n"
            )
            return

        if not ware:
            table = EvTable(
                f"|wName",
                f"|wSkill",
                f"|wRank",
                f"|wSpeed",
                f"|wAmmo",
                f"|wLevel",
                border="none",
            )
            for obj in WaresObjects.values():
                glvl = f"|WGlvl {obj.rank}"

                if obj.name in caller.db.wares:
                    table.add_row(
                        f"|Y{obj.name.title()}",
                        f"|Y{obj.skill}",
                        f"|Y{obj.skill_req}",
                        f"|Y{obj.speed}",
                        f"|Y{obj.energy_cost}",
                        f"|Y{glvl}",
                    )
                else:
                    table.add_row(
                        f"|G{obj.name.title()}",
                        f"|G{obj.skill}",
                        f"|Y{obj.skill_req}",
                        f"|G{obj.speed}",
                        f"|G{obj.energy_cost}",
                        f"|G{glvl}",
                    )
            caller.msg(str(table))
        return


WaresObjects = {
    "hand razors": HandRazors(),
    "laser pistol": LaserPistol(),
    "shock hand": ShockHand(),
    "flamethrower": FlameThrower(),
    "tactical shotgun": TacticalShotgun(),
    "energy sword": EnergySword(),
    "rocket launcher": RocketLauncher(),
    "rail pistol": RailPistol(),
    "photon blaster": PhotonBlaster(),
    "stealth blade": StealthBlade(),
    "plasma rifle": PlasmaRifle(),
    "chain blade": ChainBlade(),
    "smart gun": SmartGun(),
    "pulse rifle": PulseRifle(),
    "gauss cannon": GaussCannon(),
    "nanoblade": NanoBlade(),
    "plasma cannon": PlasmaCannon(),
    "laser sniper rifle": LaserSniperRifle(),
    "graviton hammer": GravitonHammer(),
    "vortex ar9": VortexAR9(),
    "shockwave hammer": ShockwaveHammer(),
}


# region CmdSet
class CybercorpsWaresCmdSet(CmdSet):
    key = "Cybercorps Wares CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdLoadout)
        self.add(CmdLoadoutRemove)
        self.add(CmdWares)
