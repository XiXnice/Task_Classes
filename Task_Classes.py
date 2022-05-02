class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nС\о за д\з: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        else:
            if self.average_grade() > other.average_grade():
                return f'{self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'{other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nС\о за лекции: {self.average_rate()}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        else:
            if self.average_rate() > other.average_rate():
                return f'{self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'{other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'

student_osipov = Student('Игорь', 'Осипов', 'male')
student_osipov.courses_in_progress += ['Python', 'Git']

student_maymi = Student('Олег', 'Маями', 'male')
student_maymi.courses_in_progress += ['Python']
student_maymi.finished_courses += ['Git']

reviewer_vtoray = Reviewer('Елизавета', 'Вторая')
reviewer_vtoray.courses_attached += ['Python']

reviewer_tinkof = Reviewer('Олег', 'Тинькоф')
reviewer_tinkof.courses_attached += ['Git']

lecturer_potapova = Lecturer('Елена', 'Потапова')
lecturer_potapova.courses_attached += ['Python']

lecturer_tinkof = Lecturer('Олег', 'Тинькоф')
lecturer_tinkof.courses_attached += ['Git']

reviewer_vtoray.rate_hw(student_osipov, 'Python', 7)
reviewer_tinkof.rate_hw(student_osipov, 'Git', 6)
reviewer_vtoray.rate_hw(student_maymi, 'Python', 9)
student_osipov.rate_lecturer(lecturer_potapova, 'Python', 8)
student_osipov.rate_lecturer(lecturer_tinkof, 'Git', 6)
student_maymi.rate_lecturer(lecturer_potapova, 'Python', 9)

print(student_osipov)
print(student_maymi)
print(reviewer_vtoray)
print(reviewer_tinkof)
print(lecturer_potapova)
print(lecturer_tinkof)
print(student_osipov > student_maymi)
print(lecturer_potapova > lecturer_tinkof)

def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
    all_grades_avg = str(sum(all_grades_list) / len(all_grades_list))
    print(f'С\о студентов за д\з курса {course}: {all_grades_avg}')

def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = str(sum(all_rates_list) / len(all_rates_list))
    print(f'С\о лекторов курса {course}: {all_rates_avg}')

avg_grades_all([student_osipov, student_maymi], 'Python')
avg_grades_all([student_osipov, student_maymi], 'Git')

avg_rates_all([lecturer_potapova, lecturer_tinkof], 'Python')
avg_rates_all([lecturer_potapova, lecturer_tinkof], 'Git')
