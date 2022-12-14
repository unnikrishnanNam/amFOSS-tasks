number = int(input("Enter the number: "))
# res = list(map(int, str(number)))
res = []
for i in str(number):
    res.append(int(i))

counter = 0
while len(res) != 1:
    tot = sum(res)
    res = list(map(int, str(tot)))
    # for j in str(tot):
    #     res.append(int(j))
    counter += 1
print(counter)
