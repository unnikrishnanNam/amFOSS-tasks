# Number of monster groups
group = int(input())

# Number of monsters in the nth group
monsterCount = 0

# Monster health count in the nth case
monsterHealth = ''

# For iterating over the group
for group in range(1, group + 1):
    monsterCount = int(input())
    monsterHealth = input()
    monsterHealthLst = []

    for eachMonsterHealth in monsterHealth.split():
        monsterHealthLst.append(int(eachMonsterHealth))

    if sorted(monsterHealthLst) == monsterHealthLst:
        print('YES')
    else:
        print('NO')
