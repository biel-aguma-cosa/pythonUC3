colors = [
    'vermelho', 'azul', 'verde', 'amarelo']
print(f'1. cores: {colors}')
ten_50 = [i for i in range (10,60,10)]
print(ten_50[0],ten_50[1])
names = ['nome1', 'nome2', 'nome3']
names.append('nome4')
print(f'2. adicionar nome: {names}')
langs = ["Python", "Java", "C#", "PHP"] 
langs[3] = 'javascript'
print(f'3. trocar linguagem: {names}')
five_25 = [i for i in range (5,30,5)]
five_25.remove(five_25[2])
print(print(f'4. remover número: {five_25}'))
for_thing = [i for i in range (1,6,1)]
print('4. loop:')
for i in for_thing:
    print(f'- {i}')
print('\n')
if_in = ["Ana", "Carlos", "Maria", "João"]
ansdict = {True:'Nome encontrado!',False:'Nome não encontrado...'}
print(f'5. if in: {ansdict['Maria' in if_in]}')
order = [50, 10, 80, 20, 40]
order.sort()
print(f'6. ordenar: {order}')
cut = [100, 200, 300, 400, 500] 
print(f'7. cortar: {cut[:3]}')

addition = []
while len(addition) < 5:
    num = input('8. insira um número:')
    try:
        addition.append(int(num))
    except:
        print('8. erro, tente novamente')
r = 0
for i in addition:
    r += i
print(f'8. resultado da adição: {r}')