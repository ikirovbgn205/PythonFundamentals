# Make a lists for two teams
team_a_lst = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11',]
team_b_lst = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11',]

cards = input().split() # Read and split the input
game_was_terminated = False # For checking if players in any team are below 7

# Start sending off players
for player in cards:
    if player in team_a_lst: # Check if the player is in team A
        team_a_lst.remove(player)

    elif player in team_b_lst: # Check if the player is in team B
        team_b_lst.remove(player)

    if  len(team_a_lst) < 7 or len(team_b_lst) < 7: # Check if the game is terminated
        game_was_terminated = True
        break

# Print count of each team
print(f'Team A - {len(team_a_lst)}; Team B - {len(team_b_lst)}')
if game_was_terminated: # If game is terminated, print it
    print(f'Game was terminated')
