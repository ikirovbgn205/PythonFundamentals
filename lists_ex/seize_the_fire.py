level_of_fire = input().split('#')
amount_of_water = int(input())
effort = 0
total_fire = 0
number_of_cells =[]

for cells in level_of_fire:
    cell = cells.split(' = ')
    type_fire, cell_value  = cell[0], int(cell[1])

    if type_fire == "High" and 81 <= cell_value <= 125:
        if amount_of_water < cell_value:
            continue
        amount_of_water -= cell_value
        effort += cell_value * 0.25
        total_fire += cell_value
        number_of_cells.append(str(cell_value))
    elif type_fire == "Medium" and 51 <= cell_value <= 80:
        if amount_of_water < cell_value:
            continue
        amount_of_water -= cell_value
        effort += cell_value * 0.25
        total_fire += cell_value
        number_of_cells.append(str(cell_value))
    elif type_fire == "Low" and 1 <= cell_value <= 50:
        if amount_of_water < cell_value:
            continue
        amount_of_water -= cell_value
        effort += cell_value * 0.25
        total_fire += cell_value
        number_of_cells.append(str(cell_value))

print(f"Cells: ")
for final_cell in number_of_cells:
    print(f' - {final_cell}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
