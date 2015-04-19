from hero import Hero
from random import choice
class Dungeon:
    TREASURES = ['mana', 'health potion', 'weapon', 'spell']

    def __init__(self, filename):
        self.map = self.load_from_file(filename)
        self.__current_position = None# the current position of the hero
        self.__coords = []
        self.__path = []
        self.ROWS = sum(1 for row in self.map)
        self.COLS=sum(1 for num in self.map[0])
        self.treasure_spell = []

    def get_curnt_position(self):
        return self.__current_position

    def set_curnt_position(self, i, j):
        self.__current_position = self.map[i][j]
        self.__coords = [i, j]

    def get_path(self):
        return self.__path


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

    def spawn(self, some_hero):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                    if self.map[i][j] in ('S', '.'): # the start point
                        self.map[i][j] = 'H'# position the hero at the start point
                        self.set_curnt_position(i, j)
                        self.__path.append([i, j])
                        break

            break

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

        if not self.__hero_in_map() or self.get_curnt_position() == '#':
            self.set_curnt_position(self.__path[len(self.__path)-1][0],self.__path[len(self.__path)-1][1])
            return False

        if self.get_curnt_position() == '.':
            self.__update_map()
            return True

        if self.get_curnt_position() == 'T':
            found_tresure = self.pick_treasure()
            print("Found treasure {}!".format(found_tresure))

        if self.get_curnt_position() == 'E':
            print("Enemy! Start fight")

        self.__update_map()

    def pick_treasure(self):
        dice = choice(['mana or health potion', 'weapon or spell'])
        if dice == 'mana or health potion':
            self.treasure_spell.insert(0, choice(Dungeon.TREASURES[:2]))
            return self.treasure_spell[0]
        self.treasure_spell.insert(1, choice(Dungeon.TREASURES[2:]))
        return self.treasure_spell[1]





#            self.map[self.__coords[0]][self.__coords[1]] = 'H'

    def __hero_in_map(self):
        return self.__coords[0] <= self.ROWS - 1 and \
            self.__coords[1] <= self.COLS - 1

    def __update_map(self):
        self.map[self.__coords[0]][self.__coords[1]] = 'H'
        self.map[self.__path[len(self.__path) - 1][0]][self.__path[len(self.__path) - 1][1]] = '.'
        self.__path.append(self.__coords)




def main():
    m = Dungeon('level1.txt')
    ana = Hero (name="Ana", title="Cloud", health=5000, mana=330, mana_regeneration_rate=7)
    m.spawn(ana)
    m.print_map()
    m.move_hero('right')
    print(m.move_hero('down'))
    m.print_map()
    print(m.get_path())
    # TREASURES = ['mana', 'health potion', 'weapon', 'spell']
    # treasure_spell = []
    # print(choice(Dungeon.TREASURES[:2]))
    # treasure_spell.insert(0, choice(Dungeon.TREASURES[:2]))#choice(Dungeon.TREASURES[:2])
    # print treasure_spell
if __name__ == '__main__':
    main()
