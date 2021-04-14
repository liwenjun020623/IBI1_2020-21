class Student:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.programme = None

    def set_first_name(self, a):
        self.first_name = a

    def set_last_name(self, b):
        self.last_name = b

    def set_programme(self, c):
        if c in ["BMI", "BMS"]:
            self.programme = c
        else:
            raise ValueError("Programme can only be 'BMI' or 'BMS'")

    def print_data(self):
        print("The student's name is " + self.first_name + " " +
              self.last_name + ", the undergraduate programme is " + self.programme)

# example
student1 = Student()
student1.set_first_name("Wenjun")
student1.set_last_name("Li")
student1.set_programme("BMI")
student1.print_data()