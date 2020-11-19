a = 1234 * 4
b = 13456 / 2

if a > b:
    print('a')
else:
    print('b')

c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')

a = 48
b = 4
if a % b == 0:
   print(f'{a}는 {b}로 나누어 떨어집니다.')
elif a % b != 0:
    print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')