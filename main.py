class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.new_cip = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашнее задание:{self.grades}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress}'
                f'\nЗавершенные курсы: {self.finished_courses} \n')

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_attached and course in lecture.courses_in_progress:
            if course in lecture.grades_lecture:
                lecture.grades_lecture[course] += [grade]
            else:
                lecture.grades_lecture[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades_lecture = {}
        self.average_grades_lectures = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = {}


    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {sum(self.grades_lecture.values())} \n')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'


# Студент который закончил курс
some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses = 'Введение в программирование'

# Эксперт который проверяет только по питону
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

# Оценку которую выставил эксперт за обучение
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)

# Лектор
some_lecture = Lecture('Some', 'Buddy')
some_lecture.courses_in_progress += ['Python', 'Git']
some_student.courses_attached += ['Python', 'Git']
some_student.rate_lecture(some_lecture, 'Python', 9)
some_student.rate_lecture(some_lecture, 'Git', 9)

print(some_reviewer)
print(some_lecture)
print(some_student)
