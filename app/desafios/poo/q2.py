class Student():
    def __init__(self,name):
        self.name = name
    def study(self):
        print(f'{self.name} estudou!')

s1 = Student('Pizza')

s1.study()