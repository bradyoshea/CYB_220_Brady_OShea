def describe_city(city, country="United States"):
    """Describes a city in format city, country"""
    print(f"{city.title()} is in {country.title()}")

describe_city("New York")
describe_city("North Augusta")
describe_city("Paris", "France")