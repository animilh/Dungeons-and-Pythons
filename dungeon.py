from hero import Hero
from enemy import Enemy
from fight import Fight
from weapon import Weapon
from spell import Spell
from random import choice

class Dungeon:

    TREASURES = ['mana', 'health potion', 'weapon', 'spell']
    OBSATCLE = '#'
    SPAWNING_POINT = 'S'
    ENEMY = 'E'
    EXIT = 'G'
    TREASURE = 'T'
    WALKABLE_PATH = '.'
    HERO = 'H'


    def __init__(self, filename):
        self.map = self.load_from_file(filename)
        self.__current_position = None
        self.__coords = []
        self.__path = []
        self.__ROWS = sum(1 for row in self.map)
        self.__COLS=sum(1 for num in self.map[0])
        self.hero = None
        self.enemy = None

    def get_curnt_position(self):
        return self.__current_position

    def set_curnt_position(self, i, j):
        self.__current_position = self.map[i][j]
        self.__coords = [i, j]

    def get_path(self):
        return self.__path

    def save_to_file(self, map):
        pass

    def load_from_file(self, filename):
        try:
            ret = open(filename, 'r').read().split('\n')
            lines = [line for line in ret if line.strip() != '']
            mapa = [list(line) for line in lines]

            return mapa

        except IOError("File is not found") as e:
            print(e)

    def print_map(self):
        for row in self.map:
            print(','.join(row).replace(',', ''))

    def get_spawning_points(self):
        points = []
        for i in range(self.__ROWS):
            for j in range(self.__COLS):
                if self.map[i][j] == Dungeon.SPAWNING_POINT:
                    points.append((i, j))

        return points

    def spawn(self, some_hero):
        if self.get_spawning_points == []:
            print("{} cannot be spawned.".format(str(some_hero)))

        self.hero = some_hero
        i = self.get_spawning_points().pop(0)[0]
        j = self.get_spawning_points().pop(0)[1]
        self.set_curnt_position(i, j)
        self.__path.append([i, j])


    def move_hero(self, direction):

        if direction not in ('up', 'down', 'left', 'right'):
            raise ValueError("Bad input for move direction")

        if direction == 'up':
            self.set_curnt_position(self.__coords[0]-1, self.__coords[1])

        if direction == 'down':
            self.set_curnt_position(self.__coords[0]+1, self.__coords[1])

        if direction == 'left':
            self.set_curnt_position(self.__coords[0], self.__coords[1]-1)

        if direction == 'right':
            self.set_curnt_position(self.__coords[0], self.__coords[1]+1)

        if not self.__hero_in_map() or self.get_curnt_position() == Dungeon.OBSATCLE:
            self.set_curnt_position(self.__path[len(self.__path)-1][0],self.__path[len(self.__path)-1][1])
            return False

        if self.get_curnt_position() == Dungeon.WALKABLE_PATH:
            self.__update_map()
            self.hero.set_mana(self.hero.mana_regeneration_rate)
            return True

        if self.get_curnt_position() == Dungeon.EXIT:
            print("Bravo, Hero! You've just got out of the dungeon!")

        if self.get_curnt_position() == Dungeon.TREASURE:
            found_tresure = self.pick_treasure()
            print("Found treasure {}!".format(found_tresure))

        if self.get_curnt_position() == Dungeon.ENEMY:
            print("A fight was started between our {} and {}".format(\
                repr(self.hero), repr(self.enemy)))
            Fight(self.hero, self.enemy).fight(self.hero.weapon_to_fight())

        self.hero.set_mana(self.hero.mana_regeneration_rate)
        self.__update_map()

    def pick_treasure(self):
        dice = choice(['mana or health potion', 'weapon or spell'])
        if dice == 'mana or health potion':
            self.hero.treasure_health_mana = choice(Dungeon.TREASURES[:2])
            return self.hero.treasure_health_mana
        self.hero.treasure_spell = choice(Dungeon.TREASURES[2:])
        return self.hero.treasure_spell

    def __hero_in_map(self):
        return self.__coords[0] <= self.__ROWS - 1 and \
            self.__coords[1] <= self.__COLS - 1

    def __update_map(self):
        self.map[self.__coords[0]][self.__coords[1]] = Dungeon.HERO
        self.map[self.__path[len(self.__path) - 1][0]][self.__path[len(self.__path) - 1][1]] = '.'
        self.__path.append(self.__coords)

    def hero_attack(self, by=""):
        if by == 'weapon' and self.hero.weapon is None:
            raise Exception("Hero cannot attack by weapon")

        if by == 'spell' and self.hero.spell is None:
            raise Exception("Hero cannot attack by spell")

        if by == 'spell' and self.hero.spell is not None:
            for i in range(self.__coords[1]+1, self.__coords[1]+1+self.hero.spell.cast_range**2):
                try:
                    print(self.map[self.__coords[0]][i], self.__coords[1], self.__coords[1]+1+self.hero.spell.cast_range**2)
                    if self.map[self.__coords[0]][i] == Dungeon.WALKABLE_PATH:
                        continue

                    elif self.map[self.__coords[0]][i] == Dungeon.ENEMY:
                        print("A fight is started between our {} and {}".format(repr(self.hero), repr(self.enemy)))
                        f = Fight(self.hero, self.enemy)
                        f.fight(self.hero.weapon_to_fight())
                        break
                    print("Nothing in casting range {}".format(self.hero.spell.cast_range))
                    return False
                except IndexError:
                    break

        if by == 'weapon' and self.hero.weapon is not None:
            print("A fight is started between our {} and {}".format(repr(self.hero), repr(self.enemy)))
            Fight(self.hero, self.enemy).fight(self.hero.weapon_to_fight())
            return True


def main():
    m = Dungeon('level1.txt')
    ana = Hero (name="Ana", title="Cloud", health=100, mana=330, mana_regeneration_rate=7)
    enemy = Enemy(health = 160, mana=100, damage=20)
    w = Weapon(name="The Axe of Destiny", damage=20)
    s = Spell(name="Fireball", damage=20, mana_cost=10, cast_range=3)
    ana.equip(w)
    ana.learn(s)
    m.spawn(ana)
    m.hero = ana
    m.enemy = enemy
    m.move_hero('right')

    m.print_map()
    m.move_hero('down')
    m.print_map()
    m.move_hero('down')
    m.print_map()
    m.move_hero('down')
    m.print_map()
    m.hero_attack(by='spell')


if __name__ == '__main__':
    main()
