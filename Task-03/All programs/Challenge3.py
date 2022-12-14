commands = input()
target, amount = commands.split()

target = int(target)
amount = int(amount)

a = amount/target

def compute_lcm(a):
    count = 0
    while True:
        if a%2 == 0:
            a = a//2
        elif a%3 == 0:
            a = a//3
        elif a == 1:
            break
        else:
            count = -1
            break
        count += 1
    return count

print(compute_lcm(a))
