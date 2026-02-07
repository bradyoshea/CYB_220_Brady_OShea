def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user_profile = build_profile("Brady", "O'Shea", major = "Cybersecurity", school = "Anderson University", year = "Freshman")
print(user_profile)
