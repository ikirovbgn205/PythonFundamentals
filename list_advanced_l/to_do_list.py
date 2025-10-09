notes = [0] * 10

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    index = int(command[0]) - 1
    note = command[1]
    notes.pop(int(index))
    notes.insert(index, note)

print([words for words in notes if words != 0])

