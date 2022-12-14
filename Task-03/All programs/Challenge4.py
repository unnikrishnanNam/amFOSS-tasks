facility = int(input())
tanks = 0
tankCapacities = ''

for facilityNumber in range(1, facility + 1):
    tanks = int(input())
    tankCapacities = input()
    tankCapacityList = []

    primaryZeroCount = 0
    sum = 0

    for eachTank in tankCapacities.split():
        tankCapacityList.append(int(eachTank))

    for i in tankCapacityList:
        if i == 0:
            primaryZeroCount += 1
        else:
            break
    for j in tankCapacityList[0:-1]:
        sum += j

    print(sum+(tankCapacityList.count(0)-primaryZeroCount))