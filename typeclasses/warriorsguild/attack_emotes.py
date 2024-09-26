class AttackEmotes:
    """
    Get the right attack emotes
    """

    def get_emote(attacker, emote, tn, which):
        color = "|300"

        if emote == "edged":
            return [
                f"{color}$You() swing at {tn}{color} with your weapon, but miss.",
                f"{color}$You() graze {tn}{color} with your weapon.",
                f"{color}$You() nick {tn}{color} with your weapon, drawing blood.",
                f"{color}$You() cut {tn}{color} with your weapon, causing a wound.",
                f"{color}$You() carve into {tn}{color} with your weapon, leaving a gash.",
                f"{color}$You() slash {tn}{color} with your weapon, causing a deep wound.",
                f"{color}$You() rend {tn}{color} with your weapon, causing a critical wound.",
                f"{color}$You() cleave {tn}{color} with your weapon, causing a mortal wound.",
                f"{color}$You() eviscerate {tn}{color} with your weapon, causing a fatal wound.",
                f"{color}$You() disembowel {tn}{color} with your weapon, causing a massive wound.",
                f"{color}$You() obliterate {tn}{color} with your weapon, causing a catastrophic wound.",
            ]
        if emote == "blunt":
            return [
                f"{color}$You() swing at {tn}{color} with your weapon, but miss.",
                f"{color}$You() graze {tn}{color} with your weapon.",
                f"{color}$You() strike {tn}{color} with your weapon, causing a minor wound.",
                f"{color}$You() hit {tn}{color} with your weapon, causing a small wound.",
                f"{color}$You() slam into {tn}{color} with your weapon, causing a deep wound.",
                f"{color}$You() crack {tn}{color}'s armor, causing them to bleed.",
                f"{color}$You() crush {tn}{color} with a mighty blow.",
                f"{color}$You() pummel {tn}{color} with a series of strikes.",
                f"{color}$You() smash {tn}{color} with a powerful blow.",
                f"{color}$You() grind into {tn}{color} with a fierce attack.",
                f"{color}$You() crush {tn}{color} so hard that dust and debris fly everywhere.",
                f"{color}$You() shatter {tn}{color} with a devastating attack.",
            ]
