class Human():
    # человек
    def __init__(self, name, pol):
        self.name = name
        self.pol = pol
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 2:
            raise Exception("Слишком короткое имя")
        else:
            self._name = name
        
    @property
    def pol(self):
        return self._pol

    @pol.setter
    def pol(self, pol):
        if pol not in ["мужчина", "женщина"]:
            raise Exception("Такого пола нет")
        self._pol = pol

    def introduce(self):
        print("Привет, я " + str(self.pol) + ", меня зовут " + str(self.name) + ".")
  
# Тест
# Petr = Human("Петр", "мужчина")
# print(Petr.pol)
# Petr.introduce()



class SoftwareDeveloper(Human):
    #разрабы

    def __init__(self, name, pol, language):
       super().__init__(name, pol)
       self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language not in ["Python", "js"]:
            raise Exception("Такого языка я не знаю")
        self.__language = language

    def introduce(self):
        print("Привет, я " + str(self.pol) + ", меня зовут " + str(self.name) + ". Я пишу на " + str(self.language) + ".")


# Тест
# Petr2 = SoftwareDeveloper("Петр", "мужчина", "Python")
# Petr2.introduce()


class DeveloperSchool:
    def __init__(self, language):
        self._language = language
        self._count = 0

    def teach(self, humans):
        self._count += 1
        name1 =  humans.name
        pol1 =  humans.pol
        return SoftwareDeveloper(name1, pol1, self._language)
    
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language not in ["Python", "js"]:
            raise Exception("Такого языка я не знаю")
        self.__language = language


    def get_stat(self):
        print("Привет, я школа програмирования на языке " + str(self.language) + ", через меня прошло " + str(self.count) + ".")

    @property
    def count(self):
        return self._count

          
class DebugSchool:
    def __init__(self, developerSchool: DeveloperSchool):
        self._developerSchool = developerSchool
    def teach(self, human: Human):
        human.introduce()
        human = self._developerSchool.teach(human)
        human.introduce()

        return human
    
    @property
    def count(self):
        return self._developerSchool.count



"""Тесты"""

Petr = Human("Петр", "мужчина")
# print(Petr.pol)
Petr.introduce()

Allas = Human("Элас", "женщина")
# print(Petr.pol)
Allas.introduce()

Klar = SoftwareDeveloper("Клер", "женщина", "Python")
Klar.introduce()


python_school = DeveloperSchool("Python")
python_debugSchool = DebugSchool(python_school)

Petr = python_debugSchool.teach(Petr)
Allas = python_debugSchool.teach(Allas)
print(python_debugSchool.count)
# print(Petr.language)
# print(Allas.language)
# python_school.get_stat()
