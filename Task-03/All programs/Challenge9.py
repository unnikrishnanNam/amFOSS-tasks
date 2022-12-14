def check(portal_key,portal_list,count):
        if portal_list[portal_key] != 0:
            x = portal_list[portal_key] - 1
            count += 1
            check(x,portal_list,count)
        elif count ==2:
            print("YES")
            return
        elif count != 2:
            print("NO")
            return

testcase = int(input())
for null in range(testcase):
    portal_key = int(input())-1
    portal_list = list(map(int, input().split()))
    count = 0
    check(portal_key,portal_list,count)
