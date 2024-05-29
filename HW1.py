class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        married_status = 'married' if self.is_married else 'not married'
        print(f'Full name :{self.fullname}\nAge: {self.age}\nMarried status: {married_status}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average(self):
        marks = []
        for mark in self.marks.values():
            marks.append(mark)
        average_mark = sum(self.marks.values()) / len(self.marks)
        return average_mark


class Teacher(Person):
    base_salary = 20000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)
        bonus = 0.05 * bonus_years * Teacher.base_salary
        return Teacher.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Experience: {self.experience} years')
        print(f'Salary: {self.calculate_salary()}')


def create_students():
    list_of_students = [
        Student("Alice Smith", 20, False, {"Math": 90, "English": 85, "History": 78}),
        Student("Bob Johnson", 22, True, {"Math": 75, "English": 80, "History": 82}),
        Student("Charlie Brown", 19, False, {"Math": 88, "English": 92, "History": 80})
    ]
    return list_of_students


if __name__ == '__main__':
    teacher = Teacher("John Doe", 40, True, 10)
    teacher.introduce_myself()
    print("---")

    students = create_students()
    for student in students:
        student.introduce_myself()
        student.calculate_average()
        print("---")
