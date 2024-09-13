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
        if emote == "nano_blade":
            return [
                f"{color}$You() swipe at {tn}{color} with your nano blade, but miss.",
                f"{color}$You() graze {tn}{color} with your nano blade.",
                f"{color}$You() nick {tn}{color} with your nano blade, drawing blood.",
                f"{color}$You() cut {tn}{color} with your nano blade, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your nano blade, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your nano blade, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your nano blade, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your nano blade, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your nano blade, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your nano blade, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your nano blade, causing a catastrophic wound.",
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
                f"{color}$You() fire at {tn}{color} with your tactical shotgun, but miss.",
                f"{color}$You() graze {tn}{color} with your tactical shotgun.",
                f"{color}$You() hit {tn}{color} with your tactical shotgun, causing a wound.",
                f"{color}$You() blast {tn}{color} with your tactical shotgun, causing a gash.",
                f"{color}$You() shoot {tn}{color} with your tactical shotgun, causing a deep wound.",
                f"{color}$You() blast {tn}{color} with your tactical shotgun, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with your tactical shotgun, causing a mortal wound.",
                f"{color}$You() blast {tn}{color} with your tactical shotgun, causing a fatal wound.",
                f"{color}$You() shoot {tn}{color} with your tactical shotgun, causing a massive wound.",
                f"{color}$You() blast {tn}{color} with your tactical shotgun, causing a catastrophic wound.",
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
                f"{color}$You() swipe at {tn}{color} with your shock hand, but miss.",
                f"{color}$You() graze {tn}{color} with your shock hand.",
                f"{color}$You() hit {tn}{color} with your shock hand, causing a wound.",
                f"{color}$You() blast {tn}{color} with your shock hand, causing a gash.",
                f"{color}$You() shoot {tn}{color} with your shock hand, causing a deep wound.",
                f"{color}$You() blast {tn}{color} with your shock hand, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with your shock hand, causing a mortal wound.",
                f"{color}$You() blast {tn}{color} with your shock hand, causing a fatal wound.",
                f"{color}$You() shoot {tn}{color} with your shock hand, causing a massive wound.",
                f"{color}$You() blast {tn}{color} with your shock hand, causing a catastrophic wound.",
            ]
        if emote == "energy_sword":
            return [
                f"{color}$You() swipe at {tn}{color} with your energy sword, but miss.",
                f"{color}$You() graze {tn}{color} with your energy sword.",
                f"{color}$You() hit {tn}{color} with your energy sword, causing a wound.",
                f"{color}$You() blast {tn}{color} with your energy sword, causing a gash.",
                f"{color}$You() shoot {tn}{color} with your energy sword, causing a deep wound.",
                f"{color}$You() blast {tn}{color} with your energy sword, causing a critical wound.",
                f"{color}$You() hit {tn}{color} with your energy sword, causing a mortal wound.",
                f"{color}$You() blast {tn}{color} with your energy sword, causing a fatal wound.",
                f"{color}$You() shoot {tn}{color} with your energy sword, causing a massive wound.",
                f"{color}$You() blast {tn}{color} with your energy sword, causing a catastrophic wound.",
            ]
