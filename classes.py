class Human():
    # человек
    def __init__(self, name, pol):
        self.name = name
        self.pol = pol

    def introduce(self):
        print("Привет, я " + str(self.pol) + ", меня зовут " + str(self.name) + ".")
  

# Тест
# Petr = Human("Петр", "мужчина")
# print(Petr.pol)
# Petr.introduce()



class SoftwareDeveloper(Human):
    """разрабы"""

    def __init__(self, name, pol, language):
       super().__init__(name, pol)
       self.language = language
       """В видео уроке было написанно super().__init__(self.name), вопрос нахуя тут self если с ним не работает
       Возможно видос 2020 года и в этом проблема"""

    def introduce(self):
        print("Привет, я " + str(self.pol) + ", меня зовут " + str(self.name) + ". Я пишу на " + str(self.language) + ".")


# Тест
# Petr2 = SoftwareDeveloper("Петр", "мужчина", "Python")
# Petr2.introduce()


# class DeveloperSchool():
#     def __init__(self, language):
#         self.language = language
#         self.kolvo = 0
#     def teach(hum):

