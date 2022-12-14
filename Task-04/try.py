finalCount = 0
for j in range(3):
    numbers = int(input("Enter any four digit number: "))
    temp = 0
    evenCount = 0
    for i in range(4):
        temp = numbers % 10
        numbers = numbers // 10
        if temp % 2 == 0:
            evenCount += 1
    if evenCount == 4:
        finalCount += 1

if finalCount >= 2:
    print("Bean won the game")
else:
    print("Bean lost the game")