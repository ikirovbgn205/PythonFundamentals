num = int(input())

flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

print(flag)