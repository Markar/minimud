def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"


def get_display_name(self, looker, **kwargs):
    """
    Adds color to the display name.
    """
    name = super().get_display_name(looker, **kwargs)
    if looker == self:
        # special color for our own name
        return f"|c{name}|n"
    return f"|g{name}|n"
