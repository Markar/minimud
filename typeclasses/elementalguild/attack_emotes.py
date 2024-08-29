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
                f"{color}$You() $conj(shatter) {tn}{color} with $pron(your) immense strength, leaving them in ruins!!!",
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
                f"{color}$You() $conj(consume) {tn}{color} in a whirlwind of flames, reducing them to cinders!!!",
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
                f"{color}$You() $conj(consume) {tn}{color} in a maelstrom of water, reducing them to a soaked heap!!!",
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
                f"{color}$You() $conj(scatter) {tn}{color} with a tempest of wind, reducing them to a disheveled heap!!!",
            ]
        if emote == "rock_throw":
            return [
                f"{color}$You() hurl a rock at {tn}{color}, but it misses.",
                f"{color}$pron(Your) rock hits {tn}{color} with a dull thud.",
                f"{color}$You() $conj(pelt) {tn}{color} with stones.",
                f"{color}$pron(Your) rock smashes into {tn}{color}, leaving them bruised.",
                f"{color}$You() $conj(hurl) a boulder at {tn}{color}, knocking them down.",
                f"{color}$pron(Your) rock strikes {tn}{color} with a loud crack!",
                f"{color}$You() $conj(slam) {tn}{color} with a massive stone!",
                f"{color}$You() $conj(crush) {tn}{color} with a boulder!!",
                f"{color}$You() $conj(pummel) {tn}{color} with rocks!!!",
                f"{color}$You() $conj(smash) {tn}{color} with a massive stone, leaving them in ruins!!!",
                f"{color}$You() $conj(destroy) {tn}{color} with a massive boulder, leaving them in pieces!!!",
            ]
        if emote == "earthquake":
            return [
                f"{color}$You() stomp the ground, but nothing happens.",
                f"{color}$pron(Your) stomp causes a faint tremor.",
                f"{color}$You() $conj(shake) the earth, causing {tn}{color} to lose balance.",
                f"{color}$pron(Your) stomp triggers a minor quake, making {tn}{color} stagger.",
                f"{color}$You() $conj(rock) the ground, causing {tn}{color} to trip.",
                f"{color}$pron(Your) stomp unleashes a powerful quake, toppling {tn}{color}.",
                f"{color}$You() $conj(shatter) the ground beneath {tn}{color}, sending them sprawling.",
                f"{color}$You() $conj(crush) {tn}{color} with a devastating quake!!!",
                f"{color}$You() $conj(pummel) {tn}{color} with an earth-shattering tremor!!!",
                f"{color}$You() $conj(smash) {tn}{color} with a colossal quake!!!",
                f"{color}$You() $conj(annihilate) {tn}{color} with a cataclysmic tremor!!!",
            ]
        if emote == "tremor":
            return [
                f"{color}$You() stomp the ground, but nothing happens.",
                f"{color}$pron(Your) stomp causes a faint vibration.",
                f"{color}$You() $conj(shake) the earth, causing {tn}{color} to lose balance.",
                f"{color}$pron(Your) stomp triggers a small tremor, making {tn}{color} stagger.",
                f"{color}$You() $conj(rock) the ground, causing {tn}{color} to trip.",
                f"{color}$pron(Your) stomp unleashes a powerful quake, toppling {tn}{color}.",
                f"{color}$You() $conj(shatter) the ground beneath {tn}{color}, sending them sprawling.",
                f"{color}$You() $conj(crush) {tn}{color} with a devastating quake!!!",
                f"{color}$You() $conj(pummel) {tn}{color} with an earth-shattering tremor!!!",
                f"{color}$You() $conj(smash) {tn}{color} with a colossal quake!!!",
                f"{color}$You() $conj(destroy) {tn}{color} with a cataclysmic tremor!!!",
            ]
        if emote == "quicksand":
            return [
                f"{color}$You() try to create quicksand, but nothing happens.",
                f"{color}$pron(Your) quicksand begins to form beneath {tn}{color}.",
                f"{color}$You() $conj(sink) {tn}{color} into the quicksand.",
                f"{color}$pron(Your) quicksand pulls {tn}{color} under.",
                f"{color}$You() $conj(drown) {tn}{color} in the quicksand.",
                f"{color}$pron(Your) quicksand engulfs {tn}{color}, trapping them.",
                f"{color}$You() $conj(submerge) {tn}{color} in the quicksand.",
                f"{color}$You() $conj(entrap) {tn}{color} with the quicksand!!!",
                f"{color}$You() $conj(suffocate) {tn}{color} with the quicksand!!!",
                f"{color}$You() $conj(devour) {tn}{color} with the quicksand!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with the quicksand!!!",
            ]
