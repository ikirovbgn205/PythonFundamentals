devisor = int(input())
boundary = int(input())

for current_number in range(boundary, devisor, -1):
    if  current_number % devisor  == 0:
        print(current_number)
        break