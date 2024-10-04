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
        if emote == "general_weapon":
            return [
                f"{color}$You() $conj(swing) {tn}{color}, but $pron(it) $conj(miss)!",
                f"{color}$pron(Your) attack $conj(graze) {tn}{color} for a minor wound.",
                f"{color}$pron(Your) attack $conj(hit) {tn}{color} for a small wound.",
                f"{color}$pron(Your) attack $conj(slam) into {tn}{color}, causing a deep wound!",
                f"{color}$pron(Your) attack $conj(crack) {tn}{color}'s armor, causing them to bleed!",
                f"{color}$pron(Your) attack $conj(crush) {tn}{color} with a mighty blow!",
                f"{color}$You() $conj(pummel) {tn}{color} with a series of strikes!",
                f"{color}$You() $conj(smash) {tn}{color} with a powerful blow!",
                f"{color}$You() $conj(grind) {tn}{color} into the ground with a fierce attack!",
                f"{color}$You() $conj(crush) {tn}{color} so hard that dust and debris fly everywhere!",
                f"{color}$You() $conj(shatter) {tn}{color} with a devastating attack!",
            ]
        if emote == "bash":
            return [
                f"{color}$You() charge at {tn}{color} with your shield, but miss.",
                f"{color}$You() graze {tn}{color} with the edge of your shield.",
                f"{color}$You() strike {tn}{color} with your shield, causing a minor bruise.",
                f"{color}$You() hit {tn}{color} with your shield, causing a small dent.",
                f"{color}$You() slam into {tn}{color} with your shield, causing a deep bruise.",
                f"{color}$You() crack {tn}{color}'s armor with your shield, causing them to stagger.",
                f"{color}$You() crush {tn}{color} with a mighty shield bash.",
                f"{color}$You() pummel {tn}{color} with a series of shield strikes.",
                f"{color}$You() smash {tn}{color} with a powerful shield blow.",
                f"{color}$You() grind into {tn}{color} with a fierce shield attack.",
                f"{color}$You() crush {tn}{color} so hard with your shield that dust and debris fly everywhere.",
                f"{color}$You() shatter {tn}{color} with a devastating shield bash.",
            ]
