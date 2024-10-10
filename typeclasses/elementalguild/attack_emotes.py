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
        if emote == "earth_elemental_melee_fury":
            return [
                f"{color}$You() conjure a storm of dirt that blinds {tn}{color} momentarily.",
                f"{color}$pron(Your) rocky fist now channels elemental energy, causing {tn}{color} to reel from the impact.",
                f"{color}$pron(Your) stone punch sends shockwaves, leaving {tn}{color} with deep bruises.",
                f"{color}$You() $conj(slam) into {tn}{color} with the force of an avalanche, leaving a crater!",
                f"{color}$pron(Your) crushing blow radiates energy, causing {tn}{color} to stagger and bleed profusely.",
                f"{color}$pron(Your) mighty strike cracks {tn}{color}'s bones and sends shards flying!",
                f"{color}$You() $conj(pummel) {tn}{color} with chunks of earth, each hit echoing like thunder!",
                f"{color}$You() $conj(smash) {tn}{color}'s limbs with a boulder, the impact resembling a meteor strike!!",
                f"{color}$You() $conj(grind) {tn}{color} into the ground like gravel, the earth trembling under the force!!",
                f"{color}$You() $conj(crush) {tn}{color} so hard that a cloud of dust and debris engulfs the battlefield!!!",
                f"{color}$You() $conj(shatter) {tn}{color} with $pron(your) immense strength, leaving them in ruins and the air crackling with energy!!!",
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
        if emote == "landslide":
            return [
                f"{color}$You() try to create a landslide, but nothing happens.",
                f"{color}$pron(Your) landslide begins to form around {tn}{color}.",
                f"{color}$You() $conj(suck) {tn}{color} into the landslide.",
                f"{color}$pron(Your) landslide pulls {tn}{color} in.",
                f"{color}$You() $conj(drown) {tn}{color} in the landslide.",
                f"{color}$pron(Your) landslide engulfs {tn}{color}, trapping them.",
                f"{color}$You() $conj(submerge) {tn}{color} in the landslide.",
                f"{color}$You() $conj(entrap) {tn}{color} with the landslide!!!",
                f"{color}$You() $conj(suffocate) {tn}{color} with the landslide!!!",
                f"{color}$You() $conj(devour) {tn}{color} with the landslide!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with the landslide!!!",
            ]
        if emote == "lava_flow":
            return [
                f"{color}$You() try to create a lava flow, but nothing happens.",
                f"{color}$pron(Your) lava flow begins to form around {tn}{color}.",
                f"{color}$You() $conj(suck) {tn}{color} into the lava flow.",
                f"{color}$pron(Your) lava flow pulls {tn}{color} in.",
                f"{color}$You() $conj(drown) {tn}{color} in the lava flow.",
                f"{color}$pron(Your) lava flow engulfs {tn}{color}, trapping them.",
                f"{color}$You() $conj(submerge) {tn}{color} in the lava flow.",
                f"{color}$You() $conj(entrap) {tn}{color} with the lava flow!!!",
                f"{color}$You() $conj(suffocate) {tn}{color} with the lava flow!!!",
                f"{color}$You() $conj(devour) {tn}{color} with the lava flow!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with the lava flow!!!",
            ]
        if emote == "hurl_boulder":
            return [
                f"{color}$You() hurl a boulder at {tn}{color}, but it misses.",
                f"{color}$pron(Your) boulder hits {tn}{color} with a dull thud.",
                f"{color}$You() $conj(pelt) {tn}{color} with stones.",
                f"{color}$pron(Your) boulder smashes into {tn}{color}, leaving them bruised.",
                f"{color}$You() $conj(hurl) a boulder at {tn}{color}, knocking them down.",
                f"{color}$pron(Your) boulder strikes {tn}{color} with a loud crack!",
                f"{color}$You() $conj(slam) {tn}{color} with a massive stone!",
                f"{color}$You() $conj(crush) {tn}{color} with a boulder!!",
                f"{color}$You() $conj(pummel) {tn}{color} with rocks!!!",
                f"{color}$You() $conj(smash) {tn}{color} with a massive stone, leaving them in ruins!!!",
                f"{color}$You() $conj(destroy) {tn}{color} with a massive boulder, leaving them in pieces!!!",
            ]

        #### AIR ELEMENTAL ATTACK EMOTES ####
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
        if emote == "wind_slash":
            return [
                f"{color}$You() slash at {tn}{color} with a blade of wind, but it dissipates harmlessly.",
                f"{color}$pron(Your) wind blade grazes {tn}{color}, leaving a faint mark.",
                f"{color}$You() $conj(slice) into {tn}{color} with a sharp gust of wind.",
                f"{color}$pron(Your) wind slash leaves {tn}{color} with a shallow cut.",
                f"{color}$You() $conj(gash) {tn}{color} with a powerful wind blade.",
                f"{color}$pron(Your) wind blade cuts deep into {tn}{color}'s flesh.",
                f"{color}$You() $conj(lacerate) {tn}{color} with a razor-sharp wind blade.",
                f"{color}$You() $conj(sever) {tn}{color}'s limbs with a gust of wind!!",
                f"{color}$You() $conj(impale) {tn}{color} with a blade of air!!",
                f"{color}$You() $conj(eviscerate) {tn}{color} with a whirlwind of wind!!!",
                f"{color}$You() $conj(annihilate) {tn}{color} with a tempest of wind!!!",
            ]
        if emote == "lightning_strike":
            return [
                f"{color}$You() try to call down lightning, but nothing happens.",
                f"{color}$pron(Your) lightning bolt strikes the ground near {tn}{color}.",
                f"{color}$You() $conj(shock) {tn}{color} with a bolt of lightning.",
                f"{color}$pron(Your) lightning strike leaves {tn}{color} stunned.",
                f"{color}$You() $conj(electrocute) {tn}{color} with a powerful bolt of lightning.",
                f"{color}$pron(Your) lightning bolt strikes {tn}{color} with a deafening crack.",
                f"{color}$You() $conj(fry) {tn}{color} with a bolt of lightning.",
                f"{color}$You() $conj(char) {tn}{color} with a bolt of lightning!!",
                f"{color}$You() $conj(electrify) {tn}{color} with a bolt of lightning!!",
                f"{color}$You() $conj(incinerate) {tn}{color} with a bolt of lightning!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a bolt of lightning!!!",
            ]
        if emote == "zephyr":
            return [
                f"{color}$You() try to create a zephyr, but nothing happens.",
                f"{color}$pron(Your) zephyr gently caresses {tn}{color}.",
                f"{color}$You() $conj(buffet) {tn}{color} with a gentle breeze.",
                f"{color}$pron(Your) zephyr leaves {tn}{color} feeling refreshed.",
                f"{color}$You() $conj(gust) {tn}{color} with a light breeze.",
                f"{color}$pron(Your) zephyr sends {tn}{color} stumbling back.",
                f"{color}$You() $conj(blow) {tn}{color} away with a gust of wind.",
                f"{color}$You() $conj(sweep) {tn}{color} off their feet with a powerful zephyr!!",
                f"{color}$You() $conj(whirl) {tn}{color} around in a cyclone of wind!!",
                f"{color}$You() $conj(engulf) {tn}{color} in a tornado, leaving them breathless!!!",
                f"{color}$You() $conj(scatter) {tn}{color} with a tempest of wind, reducing them to a disheveled heap!!!",
            ]
        if emote == "tornado":
            return [
                f"{color}$You() try to create a tornado, but nothing happens.",
                f"{color}$pron(Your) tornado begins to form around {tn}{color}.",
                f"{color}$You() $conj(suck) {tn}{color} into the tornado.",
                f"{color}$pron(Your) tornado pulls {tn}{color} in.",
                f"{color}$You() $conj(drown) {tn}{color} in the tornado.",
                f"{color}$pron(Your) tornado engulfs {tn}{color}, trapping them.",
                f"{color}$You() $conj(submerge) {tn}{color} in the tornado.",
                f"{color}$You() $conj(entrap) {tn}{color} with the tornado!!!",
                f"{color}$You() $conj(suffocate) {tn}{color} with the tornado!!!",
                f"{color}$You() $conj(devour) {tn}{color} with the tornado!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with the tornado!!!",
            ]
        if emote == "whirlwind":
            return [
                f"{color}$You() try to create a whirlwind, but nothing happens.",
                f"{color}$pron(Your) whirlwind begins to form around {tn}{color}.",
                f"{color}$You() $conj(suck) {tn}{color} into the whirlwind.",
                f"{color}$pron(Your) whirlwind pulls {tn}{color} in.",
                f"{color}$You() $conj(drown) {tn}{color} in the whirlwind.",
                f"{color}$pron(Your) whirlwind engulfs {tn}{color}, trapping them.",
                f"{color}$You() $conj(submerge) {tn}{color} in the whirlwind.",
                f"{color}$You() $conj(entrap) {tn}{color} with the whirlwind!!!",
                f"{color}$You() $conj(suffocate) {tn}{color} with the whirlwind!!!",
                f"{color}$You() $conj(devour) {tn}{color} with the whirlwind!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with the whirlwind!!!",
            ]
        # WATER ELEMENTAL ATTACK EMOTES
        if emote == "tidal_wave":
            return [
                f"{color}$You() summon a massive tidal wave that crashes down on {tn}{color}, drenching them from head to toe!",
                f"{color}$pron(Your) tidal wave swells and surges towards {tn}{color}, sweeping them off their feet!",
                f"{color}$You() conjure a tidal wave that engulfs {tn}{color}, leaving them gasping for air!",
                f"{color}$pron(Your) tidal wave crashes into {tn}{color} with incredible force, leaving them completely submerged!",
                f"{color}$You() create a tidal wave that traps {tn}{color} in a swirling vortex of water, making escape impossible!",
                f"{color}$pron(Your) tidal wave rises higher and higher, swallowing {tn}{color} whole!",
                f"{color}$You() unleash a tidal wave that crashes down on {tn}{color}, obliterating everything in its path!",
                f"{color}$You() summon a tidal wave so powerful that it lifts {tn}{color} high into the air before crashing them back down!",
                f"{color}$You() conjure a tidal wave that spins {tn}{color} around in a whirlpool of water, disorienting them!",
                f"{color}$You() create a tidal wave that crashes into {tn}{color} with such force that it shatters the ground beneath them!",
                f"{color}$You() summon a tidal wave that engulfs {tn}{color}, leaving them helpless against the overwhelming force of water!",
            ]
        if emote == "water_jet":
            return [
                f"{color}$You() unleash a torrential downpour, summoning a colossal water spout that crashes into {tn}{color}, drenching them from head to toe!",
                f"{color}$pron(Your) water jet transforms into a mighty tidal wave, surging towards {tn}{color} with unstoppable force!",
                f"{color}$You() conjure a water jet infused with the power of a raging storm, striking {tn}{color} with a thunderous impact!",
                f"{color}$pron(Your) water jet transforms into a raging waterfall, cascading down upon {tn}{color} with immense power!",
                f"{color}$You() create a water jet that morphs into a colossal tsunami, engulfing {tn}{color} in a swirling vortex of destruction!",
                f"{color}$pron(Your) water jet rises higher and higher, transforming into a towering waterspout that lifts {tn}{color} into the sky!",
                f"{color}$You() unleash a water jet so powerful that it creates a massive whirlpool, sucking {tn}{color} into its watery depths!",
                f"{color}$You() summon a water jet infused with the fury of a hurricane, crashing down on {tn}{color} with devastating force!",
                f"{color}$You() conjure a water jet that transforms into a swirling maelstrom, spinning {tn}{color} around in a vortex of chaos!",
                f"{color}$You() create a water jet that crashes into {tn}{color} with the force of a tidal wave, leaving destruction in its wake!",
                f"{color}$You() summon a water jet that engulfs {tn}{color}, unleashing a deluge of water that leaves them helpless and overwhelmed!",
            ]
        if emote == "maelstrom":
            return [
                f"{color}$You() create a massive maelstrom that engulfs {tn}{color}, trapping them in a swirling vortex of water!",
                f"{color}$pron(Your) maelstrom surges towards {tn}{color}, sweeping them off their feet!",
                f"{color}$You() conjure a maelstrom that crashes into {tn}{color}, leaving them gasping for air!",
                f"{color}$pron(Your) maelstrom crashes into {tn}{color} with incredible force, leaving them completely submerged!",
                f"{color}$You() create a maelstrom that traps {tn}{color} in a swirling vortex of water, making escape impossible!",
                f"{color}$pron(Your) maelstrom rises higher and higher, swallowing {tn}{color} whole!",
                f"{color}$You() unleash a maelstrom that crashes down on {tn}{color}, obliterating everything in its path!",
                f"{color}$You() summon a maelstrom so powerful that it lifts {tn}{color} high into the air before crashing them back down!",
                f"{color}$You() conjure a maelstrom that spins {tn}{color} around in a whirlpool of water, disorienting them!",
                f"{color}$You() create a maelstrom that crashes into {tn}{color} with such force that it shatters the ground beneath them!",
                f"{color}$You() summon a maelstrom that engulfs {tn}{color}, leaving them helpless against the overwhelming force of water!",
            ]
        if emote == "ice_shard":
            return [
                f"{color}$You() hurl a shard of ice at {tn}{color}, but it misses.",
                f"{color}$pron(Your) ice shard grazes {tn}{color}, leaving a frosty mark.",
                f"{color}$You() $conj(pelt) {tn}{color} with shards of ice.",
                f"{color}$pron(Your) ice shard strikes {tn}{color} with a sharp chill.",
                f"{color}$You() $conj(hurl) a shard of ice at {tn}{color}, knocking them back.",
                f"{color}$pron(Your) ice shard pierces {tn}{color} with a cold sting.",
                f"{color}$You() $conj(slam) {tn}{color} with a massive shard of ice.",
                f"{color}$You() $conj(crush) {tn}{color} with a shard of ice!!",
                f"{color}$You() $conj(pummel) {tn}{color} with shards of ice!!!",
                f"{color}$You() $conj(smash) {tn}{color} with a massive shard of ice, leaving them frozen!!!",
                f"{color}$You() $conj(destroy) {tn}{color} with a massive shard of ice, leaving them shattered!!!",
            ]
        # FIRE ELEMENTAL ATTACK EMOTES
        if emote == "fireball":
            return [
                f"{color}$You() hurl a fireball at {tn}{color}, but it fizzles out.",
                f"{color}$pron(Your) fireball singes {tn}{color}, leaving a faint burn.",
                f"{color}$You() $conj(scorch) {tn}{color} with a fiery blast.",
                f"{color}$pron(Your) fireball strikes {tn}{color} with a searing heat.",
                f"{color}$You() $conj(blaze) {tn}{color} with a powerful fireball.",
                f"{color}$pron(Your) fireball engulfs {tn}{color} in flames.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing fireball.",
                f"{color}$You() $conj(char) {tn}{color} with a fireball!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a fireball!!",
                f"{color}$You() $conj(consume) {tn}{color} with a fireball!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a fireball!!!",
            ]
        if emote == "ember_strike":
            return [
                f"{color}$You() lash out at {tn}{color} with a burst of embers, missing entirely.",
                f"{color}$pron(Your) ember strike sears {tn}{color}, leaving a charred mark.",
                f"{color}$You() $conj(scorch) {tn}{color} with a fiery touch, igniting their skin.",
                f"{color}$pron(Your) ember strike leaves {tn}{color} with a blistering heat.",
                f"{color}$You() $conj(ignite) {tn}{color} with a powerful ember strike, setting them ablaze.",
                f"{color}$pron(Your) ember strike engulfs {tn}{color} in a fiery inferno.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing ember strike, reducing them to ashes.",
                f"{color}$You() $conj(char) {tn}{color} with an ember strike, leaving a trail of smoke.",
                f"{color}$You() $conj(immolate) {tn}{color} with an ember strike, consuming them in flames.",
                f"{color}$You() $conj(consume) {tn}{color} with an ember strike, turning them to cinders.",
                f"{color}$You() $conj(obliterate) {tn}{color} with an ember strike, leaving nothing but ash.",
            ]
        if emote == "blazing_maelstrom":
            return [
                f"{color}$You() create a massive blazing maelstrom that engulfs {tn}{color}, trapping them in a swirling vortex of fire!",
                f"{color}$pron(Your) blazing maelstrom surges towards {tn}{color}, engulfing them in a whirlwind of flames!",
                f"{color}$You() conjure a blazing maelstrom that crashes into {tn}{color}, leaving them scorched and smoldering!",
                f"{color}$pron(Your) blazing maelstrom strikes {tn}{color} with incredible force, leaving them consumed by flames!",
                f"{color}$You() create a blazing maelstrom that traps {tn}{color} in a swirling vortex of fire, making escape impossible!",
                f"{color}$pron(Your) blazing maelstrom rises higher and higher, engulfing {tn}{color} in a towering inferno!",
                f"{color}$You() unleash a blazing maelstrom that crashes down on {tn}{color}, obliterating everything in its path!",
                f"{color}$You() summon a blazing maelstrom so powerful that it lifts {tn}{color} high into the air before incinerating them!",
                f"{color}$You() conjure a blazing maelstrom that engulfs {tn}{color}, leaving them helpless against the overwhelming force of fire!",
                f"{color}$You() create a blazing maelstrom that crashes into {tn}{color} with such force that it leaves them consumed by flames!",
                f"{color}$You() summon a blazing maelstrom that engulfs {tn}{color} in a whirlwind of fire, reducing them to a smoldering heap!",
            ]
        if emote == "inferno":
            return [
                f"{color}$You() create a massive inferno that engulfs {tn}{color} in a blazing conflagration!",
                f"{color}$pron(Your) inferno surges towards {tn}{color}, leaving them scorched and smoldering!",
                f"{color}$You() conjure an inferno that crashes into {tn}{color}, leaving them engulfed in a blazing inferno!",
                f"{color}$pron(Your) inferno strikes {tn}{color} with incredible force, leaving them consumed by flames!",
                f"{color}$You() create an inferno that traps {tn}{color} in a swirling vortex of fire, making escape impossible!",
                f"{color}$pron(Your) inferno rises higher and higher, engulfing {tn}{color} in a towering inferno!",
                f"{color}$You() unleash an inferno that crashes down on {tn}{color}, obliterating everything in its path!",
                f"{color}$You() summon an inferno so powerful that it lifts {tn}{color} high into the air before incinerating them!",
                f"{color}$You() conjure an inferno that engulfs {tn}{color}, leaving them helpless against the overwhelming force of fire!",
                f"{color}$You() create an inferno that crashes into {tn}{color} with such force that it leaves them consumed by flames!",
                f"{color}$You() summon an inferno that engulfs {tn}{color} in a whirlwind of fire, reducing them to a smoldering heap!",
            ]
        if emote == "fire_whip":
            return [
                f"{color}$You() lash out at {tn}{color} with a fiery whip, but it misses.",
                f"{color}$pron(Your) fire whip singes {tn}{color}, leaving a faint burn.",
                f"{color}$You() $conj(scorch) {tn}{color} with a fiery lash.",
                f"{color}$pron(Your) fire whip strikes {tn}{color} with a searing heat.",
                f"{color}$You() $conj(blaze) {tn}{color} with a powerful fire whip.",
                f"{color}$pron(Your) fire whip engulfs {tn}{color} in flames.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing fire whip.",
                f"{color}$You() $conj(char) {tn}{color} with a fire whip!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a fire whip!!",
                f"{color}$You() $conj(consume) {tn}{color} with a fire whip!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a fire whip!!!",
            ]
        if emote == "lava_burst":
            return [
                f"{color}$You() hurl a burst of lava at {tn}{color}, but it fizzles out.",
                f"{color}$pron(Your) lava burst singes {tn}{color}, leaving a faint burn.",
                f"{color}$You() $conj(scorch) {tn}{color} with a fiery blast.",
                f"{color}$pron(Your) lava burst strikes {tn}{color} with a searing heat.",
                f"{color}$You() $conj(blaze) {tn}{color} with a powerful lava burst.",
                f"{color}$pron(Your) lava burst engulfs {tn}{color} in flames.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing lava burst.",
                f"{color}$You() $conj(char) {tn}{color} with a lava burst!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a lava burst!!",
                f"{color}$You() $conj(consume) {tn}{color} with a lava burst!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a lava burst!!!",
            ]
        if emote == "fire_punch":
            return [
                f"{color}$You() swipe at {tn}{color} with a fiery fist, but it misses.",
                f"{color}$pron(Your) fire punch singes {tn}{color}, leaving a faint burn.",
                f"{color}$You() $conj(scorch) {tn}{color} with a fiery strike.",
                f"{color}$pron(Your) fire punch strikes {tn}{color} with a searing heat.",
                f"{color}$You() $conj(blaze) {tn}{color} with a powerful fire punch.",
                f"{color}$pron(Your) fire punch engulfs {tn}{color} in flames.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing punch.",
                f"{color}$You() $conj(char) {tn}{color} with a fiery punch!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a fiery punch!!",
                f"{color}$You() $conj(consume) {tn}{color} with a fiery punch!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a fiery punch!!!",
            ]
        if emote == "sunburst":
            return [
                f"{color}$You() try to create a sunburst, but nothing happens.",
                f"{color}$pron(Your) sunburst shines brightly, illuminating the area around {tn}{color}.",
                f"{color}$You() $conj(burn) {tn}{color} with the intense light of a sunburst.",
                f"{color}$pron(Your) sunburst leaves {tn}{color} blinded by the sudden burst of light.",
                f"{color}$You() $conj(scorch) {tn}{color} with the searing heat of a sunburst.",
                f"{color}$pron(Your) sunburst engulfs {tn}{color} in a blinding flash of light.",
                f"{color}$You() $conj(incinerate) {tn}{color} with the intense heat of a sunburst.",
                f"{color}$You() $conj(char) {tn}{color} with a sunburst!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a sunburst!!",
                f"{color}$You() $conj(consume) {tn}{color} with a sunburst!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a sunburst!!!",
            ]
        if emote == "flamestrike":
            return [
                f"{color}$You() try to create a flamestrike, but nothing happens.",
                f"{color}$pron(Your) flamestrike scorches the ground near {tn}{color}.",
                f"{color}$You() $conj(burn) {tn}{color} with a fiery blast.",
                f"{color}$pron(Your) flamestrike leaves {tn}{color} feeling the heat.",
                f"{color}$You() $conj(scorch) {tn}{color} with a powerful flamestrike.",
                f"{color}$pron(Your) flamestrike engulfs {tn}{color} in flames.",
                f"{color}$You() $conj(incinerate) {tn}{color} with a blazing flamestrike.",
                f"{color}$You() $conj(char) {tn}{color} with a flamestrike!!",
                f"{color}$You() $conj(immolate) {tn}{color} with a flamestrike!!",
                f"{color}$You() $conj(consume) {tn}{color} with a flamestrike!!!",
                f"{color}$You() $conj(obliterate) {tn}{color} with a flamestrike!!!",
            ]
