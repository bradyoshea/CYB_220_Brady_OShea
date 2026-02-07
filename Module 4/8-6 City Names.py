def city_country(city, country):
    value = f"{city.title()}, {country.title()}"
    return value

print(city_country("New York", "United States"))
print(city_country("Paris", "France"))
print(city_country("London", "United Kingdom"))

