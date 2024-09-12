class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.new_cip = []
        self.grades = {}


    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_attached and course in lecture.courses_in_progress:
            if course in lecture.grades_lecture:
                lecture.grades_lecture[course] += [grade]
            else:
                lecture.grades_lecture[course] = [grade]
        else:
            return 'Ошибка'

    def sums_student(self):
        sums_grades = sum(self.grades.values(),[])
        max_grades = len(sums_grades)
        new_sum_grades = 0
        for su in sums_grades:
            new_sum_grades += su / max_grades
        return new_sum_grades

    def __lt__(self, other):
        if self.sums_student() < other.sums_student():
            return 'Upss!'
        else:
            return f'Студент {other.name} {other.surname} хуже всех и его средний бал ДЗ {other.sums_student()}'

    def __gt__(self, other):
        if self.sums_student() > other.sums_student():
            return f'А вот студент {self.name} {self.surname} лучше всех его средний бал за ДЗ {self.sums_student()}'

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашнее задание: {self.sums_student()}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress}'
                f'\nЗавершенные курсы: {self.finished_courses} \n')


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

    def sums_lecture(self):
        sums_grades = sum(self.grades_lecture.values(),[])
        max_grades = len(sums_grades)
        new_sum_grades = 0
        for su in sums_grades:
            new_sum_grades += su / max_grades
        return new_sum_grades

    def __lt__(self, other):
        if self.sums_lecture() < other.sums_lecture():
            return f'Самый лучший преподователь {other.name} {other.surname} так как его средний бал {other.sums_lecture()}'


    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.sums_lecture()} \n')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'


# Студент который закончил курс
some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses = 'Введение в программирование'
some_student1 = Student('Rai', 'Jman')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses = 'Введение в программирование'

# Эксперт который проверяет только по питону
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

# Оценку которую выставил эксперт за обучение
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student1, 'Python', 8)
some_reviewer.rate_hw(some_student1, 'Git', 7)

# Лектор
some_lecture = Lecture('Some', 'Buddy')
some_lecture.courses_in_progress += ['Python', 'Git']
some_lecture1 = Lecture('Nikita', 'Dobrov-Ryzhov')
some_lecture1.courses_in_progress += ['Python', 'Git']
some_student.courses_attached += ['Python', 'Git']
some_student.rate_lecture(some_lecture1, 'Python', 5)
some_student.rate_lecture(some_lecture1, 'Git', 6)
some_student.rate_lecture(some_lecture, 'Python', 4)
some_student.rate_lecture(some_lecture, 'Git', 3)

print(some_reviewer)
print(some_lecture)
print(some_lecture1)
print(some_student)
print(some_student1)
print(some_student<some_student1)
print(some_student>some_student1)
print(some_lecture<some_lecture1)

