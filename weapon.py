class Weapon:


    def __init__(self, name="", damage=0):

        if type(damage) not in (int, float):
            raise TypeError("Bad values for weapon damage")

        self.name = str(name)
        self.damage = damage


def main():
    lyk = Weapon(name="Lyk", damage=5)

if __name__ == '__main__':
    main()
