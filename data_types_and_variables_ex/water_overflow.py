number_of_lines = int(input())

tank_capacity = 255

for _ in range(number_of_lines):
    water_flow = int(input())

    if water_flow > tank_capacity:
        print('Insufficient capacity!')
        continue

    tank_capacity -= water_flow

print(255 - tank_capacity)