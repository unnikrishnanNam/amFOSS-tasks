num = int(input("Enter a number: "))
tempNum = num
reverse = 0

while num != 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

if reverse == tempNum:
    print(tempNum, "is a palindrome")
else:
    print("Not a palindrome")