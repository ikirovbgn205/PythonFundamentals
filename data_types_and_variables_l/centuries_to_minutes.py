# Read the input
centuries = int(input())

# Do the maths
years = centuries * 100
days = years * 365.2422
hours = int(days) * 24
minutes = hours * 60

# Print the result
print(f'{centuries} centuries = {years} years = {int(days)} days = {hours} hours = {minutes} minutes')