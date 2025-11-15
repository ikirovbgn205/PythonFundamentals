start_text = input()

rage_quit = ""
sub_string = ""
repetition = ""

for index in range(len(start_text)):

    if not start_text[index].isdigit():
        sub_string += start_text[index]

    else:
        repetition += start_text[index]

        if index + 1 < len(start_text):

            if start_text[index + 1].isdigit():
                repetition += start_text[index + 1]

        rage_quit += sub_string.upper() * int(repetition)
        sub_string = ""
        repetition = ""

print(f"Unique symbols used: {len(set(rage_quit))}")
print(rage_quit)

