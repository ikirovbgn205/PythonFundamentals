text = input()

lower_text = text.lower()
vowels = ['a', 'e', 'i', 'o', 'u',]

text_no_vowels = [char for char in text if char.lower() not in vowels]
print("".join(text_no_vowels))