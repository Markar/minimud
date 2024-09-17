from evennia import CmdSet
from evennia.utils.evtable import EvTable
from commands.command import Command
from random import uniform, randint
from typeclasses.cybercorpsguild.cybercorps_attack import CybercorpsAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes


# Plasma Blade: A melee weapon with a blade of superheated plasma, cutting through armor with ease.
# Shock Baton: A non-lethal weapon that delivers high-voltage electric shocks to incapacitate targets.

# Plasma Rifle: A high-energy weapon that fires superheated plasma bolts, capable of melting through most materials.
# Gauss Cannon: A powerful railgun that uses electromagnetic forces to launch projectiles at incredible speeds.
# Pulse Rifle: A versatile weapon that fires bursts of energy pulses, effective against both organic and synthetic targets.
# Plasma Cannon: A heavy weapon that fires large plasma projectiles, causing massive damage to structures and vehicles.
# Photon Blaster: A weapon that fires concentrated beams of light, capable of cutting through metal and flesh alike.
# EMP Rifle: A rifle that fires electromagnetic pulses, disabling electronics and cybernetics from a distance.
# Laser Sniper Rifle: A long-range weapon with pinpoint accuracy, using laser technology for silent kills.
# Shockwave Cannon: A weapon that generates powerful shockwaves, knocking back and damaging multiple targets.

# Flame Thrower: A weapon that projects a stream of incendiary liquid, setting targets ablaze.
# Sonic Disruptor: A non-lethal weapon that uses high-frequency sound waves to disorient and incapacitate enemies.
# Rail Pistol: A compact railgun that fires metal slugs at hypersonic speeds.
# Explosive Bolts: Crossbow bolts with explosive tips, designed for silent yet devastating attacks.
# Neural Disruptor: A weapon that interferes with the neural signals of cybernetic implants, causing temporary paralysis.
# Gravity Gun: A weapon that manipulates gravitational forces to lift and throw objects or enemies.
# Tactical Shotgun: A close-quarters weapon with a spread of high-impact projectiles.
# Bio-Rifle: A weapon that fires biological agents, causing severe damage to organic targets.

# Cryo Grenade: A grenade that releases a freezing agent, immobilizing targets and creating hazardous ice patches.
# Thermal Detonator: A grenade that releases intense heat, incinerating everything within its blast radius.
# EMP Grenade: A tactical device that emits an electromagnetic pulse, disabling electronic devices and cybernetic implants within its blast radius.
# Pulse Grenade: A grenade that emits a burst of energy, stunning and damaging targets within its radius.
# Tactical Drone: An autonomous drone equipped with various weaponry, including machine guns and missile launchers.
# Nano Swarm: A deployable device that releases a swarm of nanobots, attacking and dismantling targets at a microscopic level.
# Holo-Projector: A device that creates realistic holographic decoys to confuse and distract enemies.


# region Guild Level Weapons
class HandRazors(CybercorpsAttack):
    """
    Hand razors are a pair of retractable blades that are attached to the
    user's hands. They are used for close combat and can be used to slash
    and stab at enemies. Hand razors are often used by assassins and other
    stealthy characters who need to be able to quickly dispatch their foes.
    """

    speed = 3
    energy_cost = 0
    name = "hand razors"
    cost = 0
    rank = 1
    skill = "cybernetic enhancements"
    short = "A pair of retractable hand razors."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.20
        dmg = 10 + stat_bonus + glvl * 0.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("hand_razors"):
            return
        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = 3
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "hand_razors")
            wielder.cooldowns.add("hand_razors", speed)


class ShockHand(CybercorpsAttack):
    """
    The shock hand is a cybernetic enhancement that allows the user to
    deliver a powerful electric shock to their enemies. The shock hand
    is often used by law enforcement and security personnel to subdue
    criminals and other threats. The shock hand can be used to deliver
    a non-lethal shock to incapacitate a target, or a lethal shock to
    kill them outright.
    """

    speed = 3
    energy_cost = 0
    name = "shock hand"
    skill = "energy solutions"
    rank = 5
    cost = 5
    short = "A cybernetic shock hand."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str * 0.25 + dex * 0.5
        dmg = 15 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("shock_hand"):
            return

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "electric", "shock_hand")
        wielder.cooldowns.add("shock_hand", self.speed)


class StealthBlade(CybercorpsAttack):
    """
    The stealth blade is a high-tech weapon that is designed for covert
    operations and stealthy assassinations. The stealth blade is equipped
    with a cloaking device that makes it nearly invisible to the naked eye,
    allowing the user to strike from the shadows without being detected.
    The stealth blade is often used by spies, assassins, and other operatives
    who need to eliminate targets quietly and efficiently.
    """

    speed = 3
    energy_cost = 0
    name = "stealth blade"
    skill = "corporate espionage"
    cost = 10
    rank = 10
    short = "A high-tech stealth blade."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.25
        dmg = 15 + stat_bonus + glvl * 0.33

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if not wielder.cooldowns.ready("stealth_blade"):
            return
        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "stealth_blade")
        wielder.cooldowns.add("stealth_blade", self.speed)


class NanoBlade(CybercorpsAttack):
    """
    The nanoblade is a high-tech weapon that uses nanotechnology to create
    a blade that is incredibly sharp and durable. The nanoblade is capable
    of cutting through almost any material with ease, making it a deadly
    weapon in the hands of a skilled user. The nanoblade is often used by
    elite soldiers and assassins who need a weapon that can penetrate armor
    and shields.

    Strength, Dexterity, Corporate Espionage
    """

    speed = 4
    energy_cost = 0
    name = "nanoblade"
    skill = "corporate espionage"
    cost = 5
    rank = 15
    short = "A high-tech nanoblade."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 30 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if not wielder.cooldowns.ready("nanoblade"):
            return
        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "edged", "nanoblade")
        wielder.cooldowns.add("nanoblade", self.speed)


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
    skill = "energy solutions"
    rank = 20
    cost = 20
    short = "A melee weapon with a blade made of pure energy."
    type = "melee"

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 35 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("energy_sword"):
            return

        dmg = self._calculate_melee_damage(wielder)
        target.at_damage(wielder, dmg, "energy", "energy_sword")
        wielder.cooldowns.add("energy_sword", self.speed)


# region Ranged Weapons
class TacticalShotgun(CybercorpsAttack):
    """
    The tactical shotgun is a versatile weapon that is effective at close
    range combat. It fires a spread of high-impact projectiles that can
    take down multiple targets with a single shot. The tactical shotgun
    is often used by law enforcement and military personnel for breaching
    and clearing rooms, as well as for crowd control and riot suppression.

    Strength, Security Services
    """

    speed = 6
    energy_cost = 1
    name = "tactical shotgun"
    skill = "security services"
    cost = 5
    rank = 3
    short = "A tactical shotgun."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value
        miss_rate = 30 - (glvl * 0.25) - (dex * 0.25)
        if randint(1, 100) < miss_rate:
            return 0

        stat_bonus = str * 0.25 + dex * 0.5
        dmg = 10 + stat_bonus + glvl * 1.5

        # divide the damage by the number of pellets and increase the total damage
        damage = int(uniform(dmg * 0.5, dmg) * 0.36)
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        # if wielder.db.strategy == "ranged":
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
    skill = "artificial intelligence"
    rank = 4
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

        damage = int(uniform(dmg * 0.5, dmg))
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


# Energy Weapons


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
    skill = "energy solutions"
    rank = 2
    cost = 1
    short = "A compact sidearm that emits concentrated laser beams."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str * 0.25 + dex * 0.5
        dmg = 5 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("laser_pistol"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "laser_pistol")
            wielder.cooldowns.add("laser_pistol", self.speed)


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
    skill = "energy solutions"
    rank = 6
    cost = 2
    short = "A weapon that fires concentrated beams of light."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 35 + stat_bonus + glvl * 1.5

        if glvl < 10:
            dmg += 2
        elif glvl < 20:
            dmg += 5
        elif glvl < 30:
            dmg += 10
        elif glvl < 40:
            dmg += 15
        else:
            dmg += 20

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)
        if not wielder.cooldowns.ready("photon_blaster"):
            return

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "ranged":
            speed = 3
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "photon_blaster")
            wielder.cooldowns.add("photon_blaster", speed)


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
    energy_cost = 3
    name = "plasma cannon"
    skill = "energy solutions"
    rank = 8
    cost = 3
    short = "A heavy weapon that fires large plasma projectiles."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 40 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("plasma_cannon"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "plasma_cannon")
            wielder.cooldowns.add("plasma_cannon", self.speed)


class GaussCannon(CybercorpsAttack):
    """
    The gauss cannon is a powerful railgun that uses electromagnetic forces
    to launch projectiles at incredible speeds. The gauss cannon is often used
    by elite soldiers and special forces operatives who need a weapon that can
    penetrate armor and shields with ease. The gauss cannon is capable of delivering
    devastating blows that can cleave through multiple enemies in a single strike.
    """

    speed = 3
    energy_cost = 3
    name = "gauss cannon"
    skill = "energy solutions"
    rank = 12
    cost = 5
    short = "A powerful railgun that uses electromagnetic forces."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 35 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("gauss_cannon"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "gauss_cannon")
            wielder.cooldowns.add("gauss_cannon", self.speed)


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
    energy_cost = 2
    name = "pulse rifle"
    skill = "energy solutions"
    rank = 16
    cost = 3
    short = "A versatile weapon that fires bursts of energy pulses."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 25 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("pulse_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "pulse_rifle")
            wielder.cooldowns.add("pulse_rifle", self.speed)


class PlasmaRifle(CybercorpsAttack):
    """
    The plasma rifle is a high-energy weapon that fires superheated plasma
    bolts, capable of melting through most materials. The plasma rifle is
    often used by elite soldiers and special forces operatives who need a
    weapon that can penetrate armor and shields with ease. The plasma rifle
    is capable of delivering devastating blows that can cleave through multiple
    enemies in a single strike.
    """

    speed = 3
    energy_cost = 2
    name = "plasma rifle"
    skill = "energy solutions"
    rank = 18
    cost = 4
    short = "A high-energy weapon that fires superheated plasma bolts."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 30 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("plasma_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "plasma_rifle")
            wielder.cooldowns.add("plasma_rifle", self.speed)


class LaserSniperRifle(CybercorpsAttack):
    """
    The laser sniper rifle is a long-range weapon with pinpoint accuracy,
    using laser technology for silent kills. The laser sniper rifle is often
    used by elite snipers and marksmen who need to eliminate targets from a
    distance without being detected. The laser sniper rifle is capable of
    delivering precise shots that can penetrate armor and shields with ease,
    making it an ideal weapon for long-range combat.
    """

    speed = 6
    energy_cost = 3
    name = "laser sniper rifle"
    skill = "energy solutions"
    rank = 24
    cost = 6
    short = "A long-range weapon with pinpoint accuracy."
    type = "ranged"

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 40 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if not wielder.cooldowns.ready("laser_sniper_rifle"):
            return
        if not wielder.db.ep >= self.energy_cost:
            return
        if wielder.db.strategy == "ranged":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_ranged_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "laser_sniper_rifle")
            wielder.cooldowns.add("laser_sniper_rifle", self.speed)


# region Wares Commands
class CmdLoadout(Command):
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

                    if caller.db.skills[obj.skill] < obj.rank:
                        caller.msg(
                            f"|rYou need rank {obj.rank} in {obj.skill} to equip the {obj.name}."
                        )
                        return
                    caller.db.ranged_weapon = WaresObjects[args]
                    caller.msg(f"|gYou equip the {obj.name}.")

        if args == "adaptive armor":
            if caller.db.adaptive_armor:
                caller.msg(f"|rYou already have adaptive armor equipped.")
                return

            caller.db.adaptive_armor = True
            caller.msg(f"|gYou equip the adaptive armor.")

        return


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

        if args == "nanoblade":
            if not melee.name == args:
                caller.msg(f"|rYou don't have the nanoblade equipped.")
                return
            caller.db.melee_weapon = None
            caller.msg(f"|gYou gracefully put the nanoblade back into its sheath.")

        if args == "tactical shotgun":
            if not ranged.name == args:
                caller.msg(f"|rYou don't have the tactical shotgun equipped.")
                return
            caller.db.ranged_weapon = False
            caller.msg(f"|gYou put the tactical shotgun on your back.")

        if args == "adaptive armor":
            if not caller.db.adaptive_armor:
                caller.msg(f"|rYou don't have adaptive armor equipped.")
                return
            caller.db.adaptive_armor = False
            caller.msg(f"|gYou remove the adaptive armor.")

        return


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
            table = EvTable(f"|wName", f"|wSkill", f"|wRank", border="none")
            for obj in WaresObjects.values():
                if obj.type == "melee":
                    rank = f"|wGlvl {obj.rank}"
                else:
                    rank = f"|w{obj.rank}"

                if obj.name in caller.db.wares:
                    table.add_row(
                        f"|Y{obj.name.title()}",
                        f"|Y{obj.skill}",
                        f"|Y{rank}",
                    )
                else:
                    table.add_row(
                        f"|G{obj.name.title()}", f"|G{obj.skill}", f"|G{rank}"
                    )
            caller.msg(str(table))
        return


WaresObjects = {
    # guild level based weapons
    "hand razors": HandRazors(),
    "shock hand": ShockHand(),
    "stealth blade": StealthBlade(),
    "nanoblade": NanoBlade(),
    "energy sword": EnergySword(),
    # security services
    "tactical shotgun": TacticalShotgun(),
    "smart gun": SmartGun(),
    # Energy Weapons
    "laser pistol": LaserPistol(),
    "photon blaster": PhotonBlaster(),
    "plasma cannon": PlasmaCannon(),
    "gauss cannon": GaussCannon(),
    "pulse rifle": PulseRifle(),
    "plasma rifle": PlasmaRifle(),
    "laser sniper rifle": LaserSniperRifle(),
}


class CybercorpsWaresCmdSet(CmdSet):
    key = "Cybercorps Wares CmdSet"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdLoadout)
        self.add(CmdLoadoutRemove)
        self.add(CmdWares)
