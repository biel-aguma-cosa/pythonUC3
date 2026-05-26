import os
nums = []
result = 0

while True:
    os.system('cls')
    print('insíra quantos números desejar, case esteja satisfeito, insira 0:')
    print()
    for n in nums:
        print(n)
    try:
        nums.append(int(input('próximo número: ')))
    except:
        pass
    if nums[len(nums)-1] == 0:
        break


for n in nums:
    result += n
os.system('cls')
print(f'resultado: {result}')