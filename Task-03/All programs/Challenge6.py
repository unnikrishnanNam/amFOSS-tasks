num = int(input())
l = []
c = 0
for i in range(num):
    li = []
    temp = input()
    for j in temp.split():
        li.append(int(j))
    l.append(li)
for i in l:
    x, y = i[0], i[1]
    right, left, lower, upper = 0, 0, 0, 0
    for j in l:
        if j[0] == x:
            if j[1] > y and upper == 0:
                upper += 1
            if j[1] < y and lower == 0:
                lower += 1
        elif j[1] == y:
            if j[0] > x and right == 0:
                right += 1
            if j[0] < x and left == 0:
                left += 1
    if right != 0 and left != 0 and lower != 0 and upper != 0:
        c += 1
print(c)
