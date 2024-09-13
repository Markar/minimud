from random import uniform, randint
from typeclasses.cybercorpsguild.cybercorps_attack import CybercorpsAttack
from typeclasses.elementalguild.attack_emotes import AttackEmotes


# Plasma Blade: A melee weapon with a blade of superheated plasma, cutting through armor with ease.
# Nano-Blade: A melee weapon with a blade composed of nanomaterials, capable of cutting through almost anything with ease.
# Shock Baton: A non-lethal weapon that delivers high-voltage electric shocks to incapacitate targets.

# Plasma Rifle: A high-energy weapon that fires superheated plasma bolts, capable of melting through most materials.
# Laser Pistol: A compact sidearm that emits concentrated laser beams, ideal for precision targeting.
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

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.25
        dmg = 5 + stat_bonus + glvl * 3

        damage = int(uniform(dmg / 2, dmg))
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
    energy_cost = 5
    name = "stealth blade"
    skill = "corporate espionage"
    cost = 2
    rank = 5
    short = "A high-tech stealth blade."

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 5 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if not wielder.cooldowns.ready("stealth_blade"):
            return
        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = 3
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "stealth_blade")
            wielder.cooldowns.add("stealth_blade", speed)


class NanoBlade(CybercorpsAttack):
    """
    The nano blade is a high-tech weapon that uses nanotechnology to create
    a blade that is incredibly sharp and durable. The nano blade is capable
    of cutting through almost any material with ease, making it a deadly
    weapon in the hands of a skilled user. The nano blade is often used by
    elite soldiers and assassins who need a weapon that can penetrate armor
    and shields.
    """

    speed = 4
    energy_cost = 3
    name = "nano blade"
    skill = "corporate espionage"
    cost = 5
    rank = 7
    short = "A high-tech nano blade."

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 5 + stat_bonus + glvl * 1.5

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        if not wielder.cooldowns.ready("nano_blade"):
            return
        if not wielder.db.ep >= self.energy_cost:
            wielder.msg("You can only maintain your hand razors.")
            return

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = 4
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "edged", "nano_blade")
            wielder.cooldowns.add("nano_blade", speed)


class TacticalShotgun(CybercorpsAttack):
    """
    The tactical shotgun is a versatile weapon that is effective at close
    range combat. It fires a spread of high-impact projectiles that can
    take down multiple targets with a single shot. The tactical shotgun
    is often used by law enforcement and military personnel for breaching
    and clearing rooms, as well as for crowd control and riot suppression.
    """

    speed = 4
    energy_cost = 1
    name = "tactical shotgun"
    skill = "security services"
    cost = 5
    rank = 3
    short = "A tactical shotgun."

    def _calculate_ranged_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str / 4 + dex / 2
        dmg = 5 + stat_bonus + glvl * 3 / 2

        if glvl < 10:
            dmg += 7
        elif glvl < 20:
            dmg += 14
        elif glvl < 30:
            dmg += 28
        elif glvl < 40:
            dmg += 42
        else:
            dmg += 65

        damage = int(uniform(dmg / 2, dmg))
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

    def _calculate_ranged_damage(self, wielder):
        # miss rate
        if randint(1, 100) < 40:
            return 0
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str / 4 + dex / 2
        dmg = 5 + stat_bonus + glvl * 3 / 2

        if glvl < 10:
            dmg += 7
        elif glvl < 20:
            dmg += 14
        elif glvl < 30:
            dmg += 28
        elif glvl < 40:
            dmg += 42
        else:
            dmg += 65

        damage = int(uniform(dmg / 2, dmg))
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
    energy_cost = 5
    name = "shock hand"
    skill = "cybernetic enhancements"
    rank = 3
    cost = 1
    short = "A cybernetic shock hand."

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = str / 4 + dex / 2
        dmg = 5 + stat_bonus + glvl * 3 / 2

        damage = int(uniform(dmg / 2, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "electric", "shock_hand")
            wielder.cooldowns.add("attack", self.speed)


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
    energy_cost = 3
    name = "energy sword"
    skill = "cybernetic enhancements"
    rank = 6
    cost = 2
    short = "A melee weapon with a blade made of pure energy."

    def _calculate_melee_damage(self, wielder):
        glvl = wielder.db.guild_level
        str = wielder.traits.str.value
        dex = wielder.traits.dex.value

        stat_bonus = (str + dex) * 0.33
        dmg = 35 + stat_bonus + glvl * 1.5

        if glvl < 10:
            dmg += 7
        elif glvl < 20:
            dmg += 14
        elif glvl < 30:
            dmg += 28
        elif glvl < 40:
            dmg += 42
        else:
            dmg += 65

        damage = int(uniform(dmg * 0.5, dmg))
        return damage

    def at_attack(self, wielder, target, **kwargs):
        super().at_attack(wielder, target, **kwargs)

        # Subtract energy and apply damage to target before their defenses
        if wielder.db.strategy == "melee":
            speed = 3
            wielder.db.ep -= self.energy_cost

            dmg = self._calculate_melee_damage(wielder)
            target.at_damage(wielder, dmg, "energy", "energy_sword")
            wielder.cooldowns.add("energy_sword", speed)
