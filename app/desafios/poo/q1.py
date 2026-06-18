class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Pão',27)

print(f'''
nome: {p1.name}
idade: {p1.age}
''')