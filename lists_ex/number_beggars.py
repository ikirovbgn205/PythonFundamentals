money_as_string = input().split(", ") # Read and split the input
count_beggars = int(input())

money_as_integer = [] # Transform and keep string to integers
for money in money_as_string:
    money_as_integer.append(int(money))

collected_money = [] # Saving the collected sums
start_index = 0 # Index for start for every beggar

for beggar in range(count_beggars): # Start iterating beggars
    current_beggar_sum = 0
    for collecting_money in range(start_index, len(money_as_integer), count_beggars): # Collecting the right sum
        current_beggar_sum += money_as_integer[collecting_money] # Add to the current beggar sum
    collected_money.append(current_beggar_sum)
    start_index += 1 # Increasing with 1 for the next beggar

print(collected_money)




