class Human:
    # человек
    def __init__(self, name: str, pol: str):
        self.name = name
        self.pol = pol

    @property
    def name(self):
        print(self.__name)

    @name.setter
    def name(self, name):
        if len(name) < 2:
            print("Слишком короткое имя")
        else:
            self.__name = name

    @property
    def pol(self):
        print(self.__pol)

    @pol.setter
    def pol(self, pol):
        if pol == "мужчина" or pol == "женщина":
            self.__pol = pol
        else:
            print("Такого пола нет")

    def introduce(self):
        print("Привет, я " + str(self.__pol) + ", меня зовут " + str(self.__name) + ".")


user = Human("Женщина", "Яна")
user.introduce()

# Тест
# Petr = Human("Петр", "мужчина")
# print(Petr.pol)
# Petr.introduce()
