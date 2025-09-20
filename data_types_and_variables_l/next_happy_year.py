# Read the input
year = int(input())

# Searching for a happy year
while True :
    year += 1 # Next year
    year_str = str(year) # Turn the int to a str

    if len(set(year_str)) == len(year_str): # Checking if all the numbers are unique
        break

# Print the next happy year
print(year)
