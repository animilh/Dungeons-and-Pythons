import re


class Panda:
    GENDERS = ['male','female']
    def __init__(self, name, email, gender):
        self.__name = str(name)

        if not re.search(r'[\w.-]+@[\w.-]+.\w+', email):
            raise ValueError("Invalid email")
        self.__email = email

        if gender not in self.GENDERS:
            raise ValueError ("The gener of panda is invalid")
        self.__gender = gender


    def __str__(self):
        return "Panda {}, email {}, gender {}".format(self.name(), self.email(), self.gender())


    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name(), self.email(), self.gender())

    def __eq__(self, other):
        return self.name() == other.name() and self.email() == other.email() and self.gender() == other.gender()


    def __hash__(self):
        return hash(self.__str__())

    def __iter__(self):
        return iter(self.__str__())

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def email(self):
        return self.__email
