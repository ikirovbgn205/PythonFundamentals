import re

initial_artefacts = input()

pattern = r"(\*|\^)([A-Z][a-z]+ [A-Z][a-z]+)(\*|\^)*(\+|!)+([0-9]+.[0-9]+,-*[0-9]+.[0-9]+)(\4)+"

matches = re.findall(pattern, initial_artefacts)

if matches:
    for match in matches:
        print(f"Found {match[1]} at coordinates {match[4]}.")
else:
    print("No valid artifacts found.")