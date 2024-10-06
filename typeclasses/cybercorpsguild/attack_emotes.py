class AttackEmotes:
    """
    Get the right attack emotes
    """

    def get_emote(attacker, emote, tn, which):
        color = "|300"

        if emote == "hand_razors":
            return [
                f"{color}$You() swipe at {tn}{color} with your hand razors, but miss.",
                f"{color}$You() graze {tn}{color} with your hand razors.",
                f"{color}$You() nick {tn}{color} with your hand razors, drawing blood.",
                f"{color}$You() cut {tn}{color} with your hand razors, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your hand razors, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your hand razors, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your hand razors, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your hand razors, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your hand razors, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your hand razors, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your hand razors, causing a catastrophic wound.",
            ]
        if emote == "nanoblade":
            return [
                f"{color}$You() swipe at {tn}{color} with your nanoblade, but miss.",
                f"{color}$You() graze {tn}{color} with your nanoblade.",
                f"{color}$You() nick {tn}{color} with your nanoblade, drawing blood.",
                f"{color}$You() cut {tn}{color} with your nanoblade, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your nanoblade, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your nanoblade, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your nanoblade, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your nanoblade, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your nanoblade, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your nanoblade, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your nanoblade, causing a catastrophic wound.",
            ]
        if emote == "stealth_blade":
            return [
                f"{color}$You() swipe at {tn}{color} with your stealth blade, but miss.",
                f"{color}$You() graze {tn}{color} with your stealth blade.",
                f"{color}$You() nick {tn}{color} with your stealth blade, drawing blood.",
                f"{color}$You() cut {tn}{color} with your stealth blade, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your stealth blade, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your stealth blade, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your stealth blade, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your stealth blade, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your stealth blade, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your stealth blade, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your stealth blade, causing a catastrophic wound.",
            ]
        if emote == "tactical_shotgun":
            return [
                f"{color}$You() fire at {tn}{color} with your tactical shotgun, but the spread misses.",
                f"{color}$You() pepper {tn}{color} with buckshot, grazing them.",
                f"{color}$You() hit {tn}{color} with a blast from your tactical shotgun, causing a flesh wound.",
                f"{color}$You() unleash a close-range blast at {tn}{color}, causing a deep gash.",
                f"{color}$You() fire a shell at {tn}{color}, causing a severe wound.",
                f"{color}$You() blast {tn}{color} with your tactical shotgun, causing a critical injury.",
                f"{color}$You() hit {tn}{color} with a direct shotgun blast, causing a mortal wound.",
                f"{color}$You() fire point-blank at {tn}{color}, causing a fatal wound.",
                f"{color}$You() unload a shell into {tn}{color}, causing a massive wound.",
                f"{color}$You() blast {tn}{color} with a devastating shotgun blast, causing catastrophic damage.",
            ]
        if emote == "smart_gun":
            return [
                f"{color}$You() fire at {tn}{color} with your smart gun, but miss.",
                f"{color}$You() graze {tn}{color} with your smart gun.",
                f"{color}$You() hit {tn}{color} with your smart gun, causing a wound.",
                f"{color}$You() blast {tn}{color} with your smart gun, causing a gash.",
                f"{color}$You() shoot {tn}{color} with your smart gun, causing a deep wound.",
                f"{color}$You() blast {tn}{color} with your smart gun, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with your smart gun, causing a mortal wound.",
                f"{color}$You() blast {tn}{color} with your smart gun, causing a fatal wound.",
                f"{color}$You() shoot {tn}{color} with your smart gun, causing a massive wound.",
                f"{color}$You() blast {tn}{color} with your smart gun, causing a catastrophic wound.",
            ]
        if emote == "shock_hand":
            return [
                f"{color}$You() swipe at {tn}{color} with your shock hand, but miss, the air crackling with electricity.",
                f"{color}$You() graze {tn}{color} with your shock hand, sending a jolt through them.",
                f"{color}$You() jab {tn}{color} with your shock hand, causing a minor shock.",
                f"{color}$You() punch {tn}{color} with your shock hand, leaving a stinging burn.",
                f"{color}$You() strike {tn}{color} with your shock hand, causing a deep, electrified wound.",
                f"{color}$You() slam {tn}{color} with your shock hand, causing a critical shock.",
                f"{color}$You() hit {tn}{color} with your shock hand, causing a mortal jolt.",
                f"{color}$You() crush {tn}{color} with your shock hand, causing a fatal surge.",
                f"{color}$You() pummel {tn}{color} with your shock hand, causing a massive electric burn.",
                f"{color}$You() obliterate {tn}{color} with your shock hand, causing a catastrophic shock.",
            ]
        if emote == "energy_sword":
            return [
                f"{color}$You() swing at {tn}{color} with your energy sword, but miss, the blade humming ominously.",
                f"{color}$You() graze {tn}{color} with your energy sword, leaving a faint scorch mark.",
                f"{color}$You() strike {tn}{color} with your energy sword, causing a minor burn.",
                f"{color}$You() slash {tn}{color} with your energy sword, leaving a glowing gash.",
                f"{color}$You() cut deep into {tn}{color} with your energy sword, causing a severe burn.",
                f"{color}$You() cleave {tn}{color} with your energy sword, causing a critical wound.",
                f"{color}$You() pierce {tn}{color} with your energy sword, causing a mortal wound.",
                f"{color}$You() slice through {tn}{color} with your energy sword, causing a fatal wound.",
                f"{color}$You() carve into {tn}{color} with your energy sword, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your energy sword, leaving a catastrophic wound.",
            ]
        if emote == "flame_thrower":
            return [
                f"{color}$You() fire at {tn}{color} with your flame thrower, but the flames miss.",
                f"{color}$You() scorch {tn}{color} with your flame thrower, causing a minor burn.",
                f"{color}$You() hit {tn}{color} with your flame thrower, causing a severe burn.",
                f"{color}$You() blast {tn}{color} with your flame thrower, causing a critical burn.",
                f"{color}$You() unleash a torrent of flames at {tn}{color}, causing a mortal burn.",
                f"{color}$You() engulf {tn}{color} in flames, causing a fatal burn.",
                f"{color}$You() incinerate {tn}{color} with your flame thrower, causing a massive burn.",
                f"{color}$You() immolate {tn}{color} with your flame thrower, causing a catastrophic burn.",
            ]
        if emote == "laser_pistol":
            return [
                f"{color}$You() fire at {tn}{color} with your laser pistol, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your laser pistol, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your laser pistol, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your laser pistol, causing a severe burn.",
                f"{color}$You() fire a laser bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a laser blast, causing a mortal wound.",
                f"{color}$You() fire a laser bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your laser pistol, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your laser pistol, causing a catastrophic wound.",
            ]
        if emote == "photon_blaster":
            return [
                f"{color}$You() fire at {tn}{color} with your photon blaster, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your photon blaster, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your photon blaster, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your photon blaster, causing a severe burn.",
                f"{color}$You() fire a photon bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a photon blast, causing a mortal wound.",
                f"{color}$You() fire a photon bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your photon blaster, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your photon blaster, causing a catastrophic wound.",
            ]
        if emote == "plasma_cannon":
            return [
                f"{color}$You() fire at {tn}{color} with your plasma cannon, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your plasma cannon, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your plasma cannon, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your plasma cannon, causing a severe burn.",
                f"{color}$You() fire a plasma bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a plasma blast, causing a mortal wound.",
                f"{color}$You() fire a plasma bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your plasma cannon, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your plasma cannon, causing a catastrophic wound.",
                f"{color}$You() EVAPORATE {tn}{color} with a plasma bolt.",
                f"{color}$You() OBLITERATE {tn}{color} with your plasma cannon.",
            ]
        if emote == "gauss_cannon":
            return [
                f"{color}$You() fire at {tn}{color} with your gauss cannon, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your gauss cannon, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your gauss cannon, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your gauss cannon, causing a severe burn.",
                f"{color}$You() fire a gauss bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a gauss blast, causing a mortal wound.",
                f"{color}$You() fire a gauss bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your gauss cannon, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your gauss cannon, causing a catastrophic wound.",
            ]
        if emote == "pulse_rifle":
            return [
                f"{color}$You() fire at {tn}{color} with your pulse rifle, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your pulse rifle, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your pulse rifle, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your pulse rifle, causing a severe burn.",
                f"{color}$You() fire a pulse bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a pulse blast, causing a mortal wound.",
                f"{color}$You() fire a pulse bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your pulse rifle, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your pulse rifle, causing a catastrophic wound.",
            ]
        if emote == "plasma_rifle":
            return [
                f"{color}$You() fire at {tn}{color} with your plasma rifle, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your plasma rifle, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your plasma rifle, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your plasma rifle, causing a severe burn.",
                f"{color}$You() fire a plasma bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a plasma blast, causing a mortal wound.",
                f"{color}$You() fire a plasma bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your plasma rifle, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your plasma rifle, causing a catastrophic wound.",
            ]
        if emote == "laser_sniper_rifle":
            return [
                f"{color}$You() fire at {tn}{color} with your laser sniper rifle, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your laser sniper rifle, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your laser sniper rifle, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your laser sniper rifle, causing a severe burn.",
                f"{color}$You() fire a laser bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a laser blast, causing a mortal wound.",
                f"{color}$You() fire a laser bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your laser sniper rifle, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your laser sniper rifle, causing a catastrophic wound.",
                f"{color}$You() EVAPORATE {tn}{color} with a laser bolt.",
                f"{color}$You() OBLITERATE {tn}{color} with your laser sniper rifle.",
                f"{color}$You() DESTROY {tn}{color} with a laser blast.",
            ]
        if emote == "rocket_launcher":
            return [
                f"{color}$You() fire at {tn}{color} with your rocket launcher, but the rocket goes wide.",
                f"{color}$You() graze {tn}{color} with your rocket launcher, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your rocket launcher, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your rocket launcher, causing a severe burn.",
                f"{color}$You() fire a rocket at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a rocket blast, causing a mortal wound.",
                f"{color}$You() fire a rocket at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your rocket launcher, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your rocket launcher, causing a catastrophic wound.",
            ]
        if emote == "rocket_launcher_hit":
            return [
                f"{color}$You() fire at {tn}{color} with your rocket launcher, but the rocket goes wide, missing the target.",
                f"{color}$You() graze {tn}{color} with your rocket launcher, leaving a deep scorch mark.",
                f"{color}$You() hit {tn}{color} with your rocket launcher, causing significant burns and trauma.",
                f"{color}$You() fire a rocket at {tn}{color}, engulfing them in a severe blast.",
                f"{color}$You() hit {tn}{color} with a rocket blast, causing catastrophic destruction.",
                f"{color}$You() fire a rocket at {tn}{color}, resulting in a fatal impact.",
                f"{color}$You() blast {tn}{color} with your rocket launcher, causing a mortal wound.",
                f"{color}$You() obliterate {tn}{color} with your rocket launcher, causing critical damage.",
                f"{color}$You() fire a rocket at {tn}{color}, causing a massive explosion and devastating damage.",
            ]

        if emote == "rail_pistol":
            return [
                f"{color}$You() fire at {tn}{color} with your rail pistol, but the shot goes wide.",
                f"{color}$You() graze {tn}{color} with your rail pistol, leaving a scorch mark.",
                f"{color}$You() hit {tn}{color} with your rail pistol, causing a minor burn.",
                f"{color}$You() blast {tn}{color} with your rail pistol, causing a severe burn.",
                f"{color}$You() fire a rail bolt at {tn}{color}, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with a rail blast, causing a mortal wound.",
                f"{color}$You() fire a rail bolt at {tn}{color}, causing a fatal wound.",
                f"{color}$You() blast {tn}{color} with your rail pistol, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your rail pistol, causing a catastrophic wound.",
            ]
        if emote == "chain_blade":
            return [
                f"{color}$You() swing at {tn}{color} with your chainblade, but miss.",
                f"{color}$You() graze {tn}{color} with your chainblade.",
                f"{color}$You() nick {tn}{color} with your chainblade, drawing blood.",
                f"{color}$You() cut {tn}{color} with your chainblade, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your chainblade, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your chainblade, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your chainblade, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your chainblade, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your chainblade, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your chainblade, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your chainblade, causing a catastrophic wound.",
            ]
        if emote == "graviton_hammer":
            return [
                f"{color}$You() swing at {tn}{color} with your graviton hammer, but miss.",
                f"{color}$You() graze {tn}{color} with your graviton hammer.",
                f"{color}$You() nick {tn}{color} with your graviton hammer, drawing blood.",
                f"{color}$You() hit {tn}{color} with your graviton hammer, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your graviton hammer, leaving a gash.",
                f"{color}$You() strike {tn}{color} with your graviton hammer, causing a deep wound.",
                f"{color}$You() crush {tn}{color} with your graviton hammer, causing a critical wound.",
                f"{color}$You() smash {tn}{color} with your graviton hammer, causing a mortal wound.",
                f"{color}$You() pulverize {tn}{color} with your graviton hammer, causing a fatal wound.",
                f"{color}$You() shatter {tn}{color} with your graviton hammer, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your graviton hammer, causing a catastrophic wound.",
            ]
        if emote == "graviton_hammer_hit":
            return [
                f"{color}$You() swing at {tn}{color} with your graviton hammer, but miss, the energy dissipating harmlessly.",
                f"{color}$You() graze {tn}{color} with your graviton hammer, the energy causing a minor shock.",
                f"{color}$You() hit {tn}{color} with your graviton hammer, the energy causing a jolt.",
                f"{color}$You() strike {tn}{color} with your graviton hammer, the energy causing a severe shock.",
                f"{color}$You() crush {tn}{color} with your graviton hammer, the energy causing a critical shock.",
                f"{color}$You() smash {tn}{color} with your graviton hammer, the energy causing a mortal shock.",
                f"{color}$You() pulverize {tn}{color} with your graviton hammer, the energy causing a fatal shock.",
                f"{color}$You() shatter {tn}{color} with your graviton hammer, the energy causing a massive shock.",
                f"{color}$You() obliterate {tn}{color} with your graviton hammer, the energy causing a catastrophic shock.",
            ]

        if emote == "vortex_ar9":
            return [
                f"{color}$You() fire at {tn}{color} with your Vortex AR-9, but the shot misses its mark.",
                f"{color}$You() clip {tn}{color} with your Vortex AR-9, leaving a superficial wound.",
                f"{color}$You() strike {tn}{color} with your Vortex AR-9, causing a moderate injury.",
                f"{color}$You() hit {tn}{color} with your Vortex AR-9, inflicting a serious wound.",
                f"{color}$You() land a precise shot on {tn}{color}, causing significant damage.",
                f"{color}$You() unleash a burst at {tn}{color}, resulting in a grievous wound.",
                f"{color}$You() fire a well-aimed shot at {tn}{color}, causing a critical injury.",
                f"{color}$You() unload a powerful volley at {tn}{color}, causing devastating damage.",
                f"{color}$You() decimate {tn}{color} with your Vortex AR-9, causing catastrophic damage.",
            ]

        if emote == "shockwave_hammer":
            return [
                f"{color}$You() swing at {tn}{color} with your shockwave hammer, but miss.",
                f"{color}$You() graze {tn}{color} with your shockwave hammer.",
                f"{color}$You() nick {tn}{color} with your shockwave hammer, drawing blood.",
                f"{color}$You() hit {tn}{color} with your shockwave hammer, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your shockwave hammer, leaving a gash.",
                f"{color}$You() strike {tn}{color} with your shockwave hammer, causing a deep wound.",
                f"{color}$You() crush {tn}{color} with your shockwave hammer, causing a critical wound.",
                f"{color}$You() smash {tn}{color} with your shockwave hammer, causing a mortal wound.",
                f"{color}$You() pulverize {tn}{color} with your shockwave hammer, causing a fatal wound.",
                f"{color}$You() shatter {tn}{color} with your shockwave hammer, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your shockwave hammer, causing a catastrophic wound.",
            ]
