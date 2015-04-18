class Hero:


    def __init__(self, name="", title="", health=0, mana=0, mana_regeneration_rate=0):

        if type(health) is not int or type(mana) is not int or type(mana_regeneration_rate) is not int:
            raise TypeError("Bad values for health, mana or mana regeneration rate")

        self.name = str(name)
        self.title = str(title)
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.spell = None
        self.weapon = None
        self.__initial_health = health
        self.__initial_mana = mana

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.__health

    def set_health(self, points):
        self.__health = self.__health + points

        if self.__health < 0:
            self.__health = 0

        elif self.__health > self.__initial_health:
            self.__health = self.__initial_health

        return self.__health

    def set_mana(self, points):
        self.__mana = self.__mana + points

        if self.__mana < 0:
            self._mana = 0

        if self.__mana > self.__initial_mana:
            self.__mana = self.__initial_mana

        return self.__mana

    def get_mana(self):
        return self.__mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana >= 90#self.spell.mana_cost# mana_cost is public or private ?

    def take_damage(self, damage_points):
        if type(damage_points) not in (int, float):
            raise TypeError("The damage points should be integer or float number")

        self.set_health(-damage_points)

    def take_healing(self, healing_points):
        if type(healing_points) not in (int, float):
            raise TypeError("The healing points should be integer or float number")

        if self.get_health() == self.__initial_health:
            raise Exception("{} is in good health!".format(self.known_as()))

        if self.is_alive():
            self.set_health(healing_points)
            return True

        return False

    def take_mana(self, mana_points): # ??? kakwo e mana moje li na umrql hero da davame mana
        if not self.is_alive():
            return False
        if self.has_moved():
            self.set_mana(self.mana_regeneration_rate)
        self.set_mana(mana_points)
        return True

    def equip(weapon):
        self.weapon = weapon

    def learn(spell):
        self.spell = spell

    def attack(by = ""):# weapon or spell
        if by not in ("weapon", "spell"):
            raise ValueError("Bad input for attack parameter")

        if self.weapon is None or self.spell is None:
            return 0

        if by == "weapon":
            return self.weapon.damage

        if by == "spell":
            return self.spell.damage





def main():
    ana = Hero (name="Ana", title="Cloud", health=5000, mana=330, mana_regeneration_rate=7)
    print(ana.known_as())
    print(ana.get_health())
    print(ana.get_mana())
    print(ana.is_alive())
    ana.take_damage(90)
    print(ana.get_health())
    print(ana.take_healing(10))
    print(ana.get_health())

if __name__ == '__main__':
    main()
