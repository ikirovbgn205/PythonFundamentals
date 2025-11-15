import re

dates = input()

pattern = r"(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"

match_date = re.findall(pattern, dates)

for date in match_date:
    day, month, year = date[0], date[2], date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")