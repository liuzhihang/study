# 循环语句

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum_x = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum_x = sum_x + x
print(sum_x)

var = 0
while var < 100:
    num = int(input(f'当前 var {var}, 请再输入一个数字:'))
    print('输入的数字是:', num)
    var = num

print(f'{var} >= 100 退出循环')
