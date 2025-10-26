queue_of_sheep = list(map(str, input().split(", ")))

# Me going in front of the queue

turned_queue = queue_of_sheep[::-1]
wolfs_index = 0

for index in range(len(turned_queue)):
    if turned_queue[index] == "wolf": # Find the wolf
        wolfs_index = index
        if turned_queue[index] == turned_queue[0]: # Check if the wolf is beside me
            print("Please go away and stop eating my sheep")
        else: # The way if the wolf is not beside me, sorry for the sheep in front of the wolf
            eaten_sheep = wolfs_index
            print(f"Oi! Sheep number {eaten_sheep}! You are about to be eaten by a wolf!")

# Find out thet I didn't have to search for the actual sheep index because,
# the starting index is 0 and the sheep in front of the wolf is the actual wolf's index.


