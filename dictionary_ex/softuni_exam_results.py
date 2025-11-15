exam_results = {}
submissions = {}

command = input()

while command != "exam finished":
    action = command.split("-")
    if len(action) > 2:
        username, language, points = action[0], action[1], int(action[2])
        if username not in exam_results.keys():
            exam_results[username] = 0
        if points > exam_results[username]:
            exam_results[username] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
    else:
        username = action[0]
        del exam_results[username]

    command = input()

print("Results:")
for username, points in exam_results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")