class Enemy:

    def __init__(self, health=0, mana=0, damage=0):
        self.__health = health
        self.__mana = mana
        self.__damage = damage
        self.__initial_health = health
        self.__initial_mana = mana


    def __str__(self):
        return "Enemey(health={}, mana={}, damage={})".format(self.get_health(),\
            self.get_mana(), self.get_damage())


    def __repr__(self):
        return self.__str__()

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

    def get_damage(self):
        return self.__damage

    def is_alive(self):
        return self.get_health() > 0

    # def can_cast(self):
    #     return self.get_mana >= self.spell.mana_cost # mana_cost is public or private ?

    def take_damage(self, damage_points):
        if type(damage_points) not in (int, float):
            raise TypeError("The damage points should be integer or float number")

        self.set_health(-damage_points)

def main():
    ana = Enemy(health=50, mana=30, damage=7)
    print(ana.get_health())
    print(ana.get_mana())
    print(ana.is_alive())
    ana.take_damage(30)
    print(ana.get_health())
#    print(ana.take_healing(10))
#    print(ana.get_health())

if __name__ == '__main__':
    main()
