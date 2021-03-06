class Spell:

    def __init__(self, name="", damage=0, mana_cost=0, cast_range=0):
        if (type(damage), type(mana_cost), type(cast_range)) != (int, int, int):
            raise TypeError("Bad values for spell damage, mana_cost, cast_range")

        self.name = str(name)
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
