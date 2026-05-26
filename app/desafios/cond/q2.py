import os
age = None
while not age:
    os.system('cls')
    try:
        age = int(input('idade: '))
    except ValueError:
        pass
if age >= 18:
    print('acesso liberado ao sistema')
else:
    print('acesso negado')