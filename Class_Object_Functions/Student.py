class Student:
    def __init__(self, name, standard, percent):
        self.name = name
        self.standard = standard
        self.percent = percent   # Boolean variable

    def is_intellegent(self):
        if self.percent >= 90:
            return True
        else:
            return False

