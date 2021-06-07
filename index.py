class Student:

    def __init__(self, name, birth_date, address):
        self.name = name
        self.dateofbirth = birth_date
        self.address = address
        pass



class Group:

    def __init__(self, name):
        self.name = name
        self.students = Student
        pass

