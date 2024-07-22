class Student:
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.courses = courses
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grades} '
                f'\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: Введение в программирование')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades} \n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n'


# Оценка для студента
some_student = Student('Ruoy', 'Eman', 'Python')
some_student.courses_in_progress += ['Python', 'Git']
# Кто ставитоценку Эксперт
best_reviewer = Reviewer('Some', 'Buddy')
best_reviewer.courses_attached += ['Python', 'Git']
best_reviewer.rate_hw(some_student, 'Python', 9)
best_reviewer.rate_hw(some_student, 'Python', 8)
best_reviewer.rate_hw(some_student, 'Git', 10)

# Оценка для препода
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_in_progress += ['Python']
# Кто ставит оценку Студент
best_student = Student('Ruoy', 'Eman', 'Python')
best_student.courses_attached += ['Python']
best_student.rate_hw(some_lecturer, 'Python', 10)

some_reviewer = Reviewer('Some', 'Buddy')

print(some_reviewer)
print(some_lecturer)
print(some_student)