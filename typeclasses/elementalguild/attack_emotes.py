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

        



                