def index_checking(index_one:int, index_two:int)-> bool:
    if index_one == index_two:
        return True

    if index_one > len(board_of_elements) or index_two > len(board_of_elements):
        return True

    if index_one < 0 or index_two < 0:
        return True
    else:
        return False

board_of_elements = input().split()
command = input()
number_of_moves = 0
cheating = False


while command != "end":

    action = command.split()

    middle_of_board = len(board_of_elements) // 2

    first_index, second_index = int(action[0]), int(action[1])

    cheating = index_checking(first_index, second_index)

    if not board_of_elements:
        print(f"You have won in {number_of_moves } turns!")
        break

    number_of_moves += 1

    if cheating:
        board_of_elements.insert(middle_of_board , f"{-number_of_moves}a")
        board_of_elements.insert(middle_of_board + 1, f"{-number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif board_of_elements[first_index] == board_of_elements[second_index]:
        element = board_of_elements[first_index]
        print(f"Congrats! You have found matching elements - {element}!")
        board_of_elements = [char for char in board_of_elements if char not in element]

    elif board_of_elements[first_index] != board_of_elements[second_index]:
        print("Try again!")

    command = input()

print(f'Sorry you lose :(\n{" ".join(board_of_elements)}')