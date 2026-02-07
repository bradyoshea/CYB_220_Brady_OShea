def car_info(manufacturer, model, **features):
    features["manufacturer"] = manufacturer
    features["model"] = model
    return features
print(car_info("Honda", "Civic", year = "2005", color = "blue"))