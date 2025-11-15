sequence = input()

unique_chrs = []

for char in sequence:
    if char not in unique_chrs or char != unique_chrs[-1]:
        unique_chrs.append(char)

print("".join(unique_chrs))