class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        total_grades = []
        for i in self.grades:
            total_grades.extend(self.grades[i])
        avg_r = round((sum(total_grades) / len(total_grades)), 1)
        return avg_r

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rating()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress != [] else "Нет"}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses) if self.finished_courses != [] else "Нет"}')

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if self.average_rating() > other.average_rating():
                return f'У студента "{self.name} {self.surname}" средняя оценка выше чем у студента "{other.name} {other.surname}".'
            elif self.average_rating() < other.average_rating():
                return f'У студента "{other.name} {other.surname}" средняя оценка  выше чем у студента "{self.name} {self.surname}".'
            else:
                return f'Студент "{self.name} {self.surname}" и студент "{other.name} {other.surname}" имеют равную среднюю оценку.'
        if isinstance(self, Student):
            return f'{other.name} {other.surname} не является студентом.'
        else:
            return f'{self.name} {self.surname} не является студентом.'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        total_grades = []
        for i in self.grades:
            total_grades.extend(self.grades[i])
        avg_r = round((sum(total_grades) / len(total_grades)), 1)
        return avg_r

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_rating()}')

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if self.average_rating() > other.average_rating():
                return f'У лектора "{self.name} {self.surname}" средняя оценка за лекции выше чем у лектора "{other.name} {other.surname}".'
            elif self.average_rating() < other.average_rating():
                return f'У лектора "{other.name} {other.surname}" средняя оценка за лекции выше чем у лектора "{self.name} {self.surname}".'
            else:
                return f'Лектор "{self.name} {self.surname}" и лектор "{other.name} {other.surname}" имеют равную среднюю оценку.'
        else:
            if isinstance(self, Lecturer):
                return f'{other.name} {other.surname} не является лектором.'
            else:
                return f'{self.name} {self.surname} не является лектором.'


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
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_lecturer = Lecturer('Alex', 'Ivanov')
cool_lecturer.courses_attached += ['Python']
lecturer_2 = Lecturer('Stepan', 'Petrov')
lecturer_2.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 5)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

best_student.rate_lecturer(lecturer_2, 'Python', 4)
best_student.rate_lecturer(lecturer_2, 'Python', 5)
best_student.rate_lecturer(lecturer_2, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)
print(cool_mentor)
print(cool_lecturer)
print(best_student)

print(lecturer_2 < cool_lecturer)
