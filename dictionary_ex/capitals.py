
countries = input().split(", ")
capitals = input().split(", ")

capitals_book = {country:capital for country, capital in zip(countries, capitals)}


for country, capital in capitals_book.items():
    print(f'{country} -> {capital}')