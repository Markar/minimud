class AttackEmotes:
    """
    Get the right attack emotes
    """

    def get_emote(attacker, emote, tn, which):
        color = "|r"

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
