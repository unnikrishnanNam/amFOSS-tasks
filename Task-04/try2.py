'''
n = int(input("Enter the value of k: "))
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

sum = a + b

print(a)
print(b)
for i in range(n-2):
    newNum = (sum) % 10
    sum += newNum
    print(newNum)
'''

guard = None
t = int(input('t:'))
s = int(input('s:'))
x = int(input('x:'))
for i in range(s+1):
    a = t + i*s
    b = t + i*s + 1
    if x != a and x != b:
        guard = True
    else:
        guard = False
if guard == True:
    print('YES')
else:
    print('NO')
