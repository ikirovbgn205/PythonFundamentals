# Input
snowballs_made = int(input())

# Saving the max values
max_weight = 0
max_hit_time = 0
max_quality = 0
highest_value_ball = 0

# Iterate Snowballs
for _ in range(snowballs_made):

    snowball_weight = int(input())
    hit_time_needed = int(input())
    quality = int(input())

    value_snowball = (snowball_weight // hit_time_needed) ** quality # Calculate the snowball value

    if value_snowball > highest_value_ball: # Check if snowball value is max
        max_weight = snowball_weight
        max_hit_time = hit_time_needed
        max_quality = quality
        highest_value_ball = value_snowball

print(f'{max_weight} : {max_hit_time} = {highest_value_ball} ({max_quality})')



