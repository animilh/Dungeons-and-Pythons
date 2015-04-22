from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell

class Fight:

    def __init__(self, hero, enemy):
        if not isinstance(hero, Hero) or not isinstance(enemy, Enemy):
            raiseTypeError("Bad types for hero or enemy")

        self.hero = hero
        self.enemy = enemy

#    @staticmethod
    def fight(self, start_weapon):
        if isinstance(start_weapon, Weapon):
            while self.hero.get_health > 0 and self.enemy.get_health >0:
                self.enemy.take_damage(self.hero.attack(by = "weapon"))
                print("Hero hits enemy with {} for {} dmg. Enemy health\
                    is {}".format(self.hero.weapon.name, self.hero.weapon.\
                        damage, self.enemy.get_health()))
                if self.enemy.is_alive():
                    self.hero.take_damage(self.enemy.get_damage())
                    print("Enemy hits hero with {} dmg. Hero health is {}".\
                        format(self.enemy.get_damage(), self.hero.get_health()))
                    if self.hero.is_alive:
                        continue
                    else:
                        print("Hero is dead")
                        break
                else:
                    print("Enemy is dead")
                    break
