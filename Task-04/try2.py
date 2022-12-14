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

