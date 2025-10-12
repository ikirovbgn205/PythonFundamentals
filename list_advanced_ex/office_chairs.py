number_of_rooms = int(input())
free_chairs = 0

for room in range(1,number_of_rooms + 1):
    chairs_and_visitors = input().split(" ")
    chairs, visitors = chairs_and_visitors[0], int(chairs_and_visitors[1])
    difference = len(chairs) - visitors
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    free_chairs += difference

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")