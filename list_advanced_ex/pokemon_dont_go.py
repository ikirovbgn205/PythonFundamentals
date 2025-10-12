distances_to_the_pokemon = [int(number) for number in input().split()]

removed_elements_sum = 0

while distances_to_the_pokemon:
    command = int(input())

    if command < 0:
        removed_element = distances_to_the_pokemon[0]
        distances_to_the_pokemon[0] = distances_to_the_pokemon[-1]
    elif command > len(distances_to_the_pokemon) - 1:
        removed_element = distances_to_the_pokemon[-1]
        distances_to_the_pokemon[-1] = distances_to_the_pokemon[0]
    else:
        removed_element = distances_to_the_pokemon.pop(command)

    removed_elements_sum += removed_element

    for index in range(len(distances_to_the_pokemon)):
        if distances_to_the_pokemon[index] <= removed_element:
             distances_to_the_pokemon[index] += removed_element
        else:
            distances_to_the_pokemon[index] -= removed_element

print(removed_elements_sum)
