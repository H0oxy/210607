class Student:

    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address



class Group:

    def __init__(self, name):
        self.name = name
        self.students = []


student_1 = Student('Моргенштерн Алишер Тагирович', '17.02.1998', 'г.Курган, центр')
student_2 = Student('Королёв Дмитрий Олегович', '10.10.1997', 'г.Курган, центр')
group_1 = ('ИТ-33')
print('student_2.__dict__=', student_2.__dict__)
