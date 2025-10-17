people = int(input())
wagons = list(map(int, input().split()))
max_capacity = 4

for i in range(len(wagons)):
    free = max_capacity - wagons[i]

    if free > 0 and people > 0:
        to_be_boarded = min(free, people)
        wagons[i] += to_be_boarded
        people -= to_be_boarded

if people == 0 and any(w < max_capacity for w in wagons):
    print(f"The lift has empty spots!")
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")


print(" ".join(map(str, wagons)))
