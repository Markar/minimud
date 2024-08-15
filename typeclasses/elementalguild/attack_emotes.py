class AttackEmotes:
    """
    Get the right attack emotes
    """
    def get_emote(attacker, emote, tn, which):
        color = "|r"
        
        if emote == "earth_elemental_melee":
            return [
                f"{color}$You() hurl a handful of dirt, but it scatters harmlessly.",
                f"{color}$pron(Your) rocky fist grazes {tn}{color}, causing minor scratches.",
                f"{color}$pron(Your) stone punch leaves {tn}{color} with a few bruises.",
                f"{color}$You() $conj(slam) into {tn}{color}, leaving a deep dent!",
                f"{color}$pron(Your) crushing blow causes {tn}{color} to stagger and bleed.",
                f"{color}$pron(Your) mighty strike cracks {tn}{color}'s bones!",
                f"{color}$You() $conj(pummel) {tn}{color} with chunks of earth!",
                f"{color}$You() $conj(smash) {tn}{color}'s limbs with a boulder!!",
                f"{color}$You() $conj(grind) {tn}{color} into the ground like gravel!!",
                f"{color}$You() $conj(crush) {tn}{color} so hard that dust and debris fly everywhere!!!",
                f"{color}$You() $conj(shatter) {tn}{color} with $pron(your) immense strength, leaving them in ruins!!!"
            ]
        if emote == "fire_elemental_melee":
            return [
                f"{color}$You() swipe at {tn}{color} with a fiery claw, leaving scorch marks.",
                f"{color}$pron(Your) blazing punch singes {tn}{color}'s flesh.",
                f"{color}$You() $conj(ignite) {tn}{color} with a searing touch!",
                f"{color}$pron(Your) molten fist melts {tn}{color}'s armor!",
                f"{color}$You() $conj(engulf) {tn}{color} in flames with a powerful strike!",
                f"{color}$pron(Your) fiery kick sends {tn}{color} reeling, smoke rising from the wound.",
                f"{color}$You() $conj(blast) {tn}{color} with a burst of intense heat!",
                f"{color}$You() $conj(incinerate) {tn}{color}'s limbs with a fiery blow!!",
                f"{color}$You() $conj(char) {tn}{color} to a crisp with a devastating punch!!",
                f"{color}$You() $conj(immolate) {tn}{color}, leaving nothing but ashes!!!",
                f"{color}$You() $conj(consume) {tn}{color} in a whirlwind of flames, reducing them to cinders!!!"
            ]
        if emote == "water_elemental_melee":
            return [
                f"{color}$You() lash out at {tn}{color} with a watery tendril, leaving them drenched.",
                f"{color}$pron(Your) fluid punch splashes against {tn}{color}, soaking them.",
                f"{color}$You() $conj(surge) into {tn}{color} with a powerful wave!",
                f"{color}$pron(Your) liquid strike leaves {tn}{color} gasping for breath!",
                f"{color}$You() $conj(drench) {tn}{color} with a torrent of water!",
                f"{color}$pron(Your) watery kick sends {tn}{color} sprawling, water cascading from the impact.",
                f"{color}$You() $conj(crash) into {tn}{color} with the force of a tidal wave!",
                f"{color}$You() $conj(submerge) {tn}{color}'s limbs in a whirlpool of water!!",
                f"{color}$You() $conj(drown) {tn}{color} in a deluge of liquid fury!!",
                f"{color}$You() $conj(engulf) {tn}{color} in a vortex of water, leaving them gasping!!!",
                f"{color}$You() $conj(consume) {tn}{color} in a maelstrom of water, reducing them to a soaked heap!!!"
            ]
        if emote == "air_elemental_melee":
            return [
                f"{color}$You() swipe at {tn}{color} with a gust of wind, ruffling their clothes.",
                f"{color}$pron(Your) airy punch sends {tn}{color} stumbling back.",
                f"{color}$You() $conj(buffet) {tn}{color} with a powerful blast of wind!",
                f"{color}$pron(Your) whirlwind strike leaves {tn}{color} disoriented!",
                f"{color}$You() $conj(gust) {tn}{color} with a forceful breeze!",
                f"{color}$pron(Your) wind-infused kick sends {tn}{color} tumbling, leaves swirling around them.",
                f"{color}$You() $conj(blow) {tn}{color} away with the force of a hurricane!",
                f"{color}$You() $conj(sweep) {tn}{color}'s limbs with a vortex of air!!",
                f"{color}$You() $conj(whirl) {tn}{color} around in a cyclone of wind!!",
                f"{color}$You() $conj(engulf) {tn}{color} in a tornado, leaving them breathless!!!",
                f"{color}$You() $conj(scatter) {tn}{color} with a tempest of wind, reducing them to a disheveled heap!!!"
            ]

        



                