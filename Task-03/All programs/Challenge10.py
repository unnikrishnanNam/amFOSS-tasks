n = int(input(""))

s = []
s = map(int, input("").split(" ", (n-1)))
group = list(s)

one = group.count(1)
two = group.count(2)
three = group.count(3)
four = group.count(4)

if three == one:
    if two%2 == 0:
        print(int(four+three+two/2))
    elif two%2 != 0:
        print(int(four + three + (two//2) + 1))
        
elif three<one:
    if two%2==0:
        print(int(four + three + two/2 + (one-three)//4+(one-three)%4))
    elif two%2 != 0:
        print(int(four + three + two // 2 + (one - three -1 ) // 4+(one-three-1)%4 ))

elif three>one:
    if two%2==0:
        print(int(four + one + two/2 + (three-one)))
    elif two%2 != 0:
        print(int(four + one + two // 2 + (three - one) + 1))
        
else:
    exit()

