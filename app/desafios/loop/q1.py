import os

num = -9999999999999899999999999999
while num < 0:
    os.system('cls')
    if num != -9999999999999899999999999999:
        print('entrada inválida')
    try:
        num = int(input('insira um número positivo: '))
    except:
        pass
    