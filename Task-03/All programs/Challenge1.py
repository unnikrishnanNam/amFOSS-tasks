city = int(input())
heros = 0
heroLvs = ''

# For loop for iterating over the city
for cityNumber in range(1, city + 1):

    heros = int(input())

    heroLv = input()
    heroLst = []

    # For iterating over each and adding to the list
    for eachHero in heroLv.split():
        heroLst.append(int(eachHero))

    heroSet = set(heroLst)
    if 0 in heroLst:
        print(len(heroLst) - heroLst.count(0))
    elif len(heroLst) != len(heroSet):
        print(len(heroLst))
    else:
        print(len(heroLst) + 1)

