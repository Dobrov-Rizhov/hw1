class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def say_mentor(self):
        print(f'Привет всем меня зовут {self.surname} {self.name}, и я Наставник Ха-ха-ха')


class Lecture(Mentor):
    def say_lecture(self):
        print(f'Привет меня зовут {self.surname} {self.name} и я Лектор')


class Reviewer(Mentor):
    def say_reviewer(self):
        print(f'Привет меня зовут {self.surname} {self.name} и я Эксперт в области программирования')


mentors = Mentor("Никита", "Добров-Рыжов")
lectures = Lecture("Анна", "Доброва-Рыжова")
reviewers = Reviewer("Марк", "Добров-Рыжов")

mentors.say_mentor()
lectures.say_lecture()
reviewers.say_reviewer()
