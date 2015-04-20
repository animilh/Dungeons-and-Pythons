from hero import Hero
class Dungeon:

    def __init__(self, filename):
        self.map = self.load_from_file(filename)

    def load_from_file(self, filename):
        try:
            ret = open(filename, 'r').read().split('\n')
            lines = [line for line in ret if line.strip() != '']
            mapa = [list(line) for line in lines]

            return mapa

        except IOError("File is not found"), e:
            print(e)

    def print_map(self):
        for row in self.map:
            print(','.join(row).replace(',', ''))

    def spawn(self, some_hero):
        rows=sum(1 for row in self.map)
        cols=sum(1 for num in self.map[0])

        for i in range(rows):
            for j in range(cols):
                    if self.map[i][j] == 'S': # the start point
                        self.map[i][j] = 'H'# position the hero at the start point
                        break
                    if self.map[i][j] == '.':#spawing point
                        self.map[i][j] = 'H'# position the hero at the spawing point
                        break
            break

def main():
    m = Dungeon('level1.txt')
#    print(m.map)
    #print(read_file('level1.txt'))
    m.print_map()
    ana = Hero (name="Ana", title="Cloud", health=5000, mana=330, mana_regeneration_rate=7)
    m.spawn(ana)
    m.print_map()

if __name__ == '__main__':
    main()
