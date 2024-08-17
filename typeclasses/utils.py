def adjust_hp(self, amount):
    hp = self.db.hp
    hpmax = self.db.hpmax
    
    if hp + amount > hpmax:
        amt = hpmax - hp
        self.db.hp += max(amt, 0)
        return
    else: 
        self.db.hp += max(amount, 0)

def adjust_fp(self, amount):
    fp = self.db.fp
    fpmax = self.db.fpmax
    
    if fp + amount > fpmax:
        amt = fpmax - fp
        self.db.fp += max(amt, 0)
        return
    else:
        self.db.fp += max(amount, 0)

def adjust_ep(self, amount):
    ep = self.db.ep
    epmax = self.db.epmax
    
    if ep + amount > epmax:
        amt = epmax - ep
        self.db.ep += max(amt, 0)
        return
    if ep < epmax + amount:
        self.db.ep += max(amount, 0)
        
def get_article(word):
    vowels = "aeiou"
    return "an" if word[0].lower() in vowels else "a"