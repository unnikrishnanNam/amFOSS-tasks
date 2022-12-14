lst = []
st = []
ans = input()
rm_space = ans.split()
for k in rm_space:
    lst.append(k)

n = int(lst[0])
m = int(lst[1])

if n < m:
    print(-1)

else:
    mod = n % m
    int_div = n // m
    if int_div % 2 == 0 and mod != 0:
        x = (2 * m) - mod
        a = n + x
        coins = int(a / 2)
        print(coins)
    elif int_div % 2 == 0 and mod == 0:
        coins = int(n/2)
        print(coins)
    else:
        x = m - mod
        a = n + x
        coins = int(a / 2)
        print(coins)
