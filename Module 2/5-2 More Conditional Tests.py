name = "Brady"
print("Does name == brady? I predict false because it is case sensitive.")
print(name == "brady")

print("Does name == Brady? I predict true")
print(name == "Brady")

num = 5

print(num > 6)
print(num < 7)
print(num > 5)
print(num >= 5)
num_string = "5"
print(num_string == num)
print(num_string == "5")
print(num_string == name)
print(num == 5)
print(name.lower() == "brady")
print(name.lower() == "Brady")
print(name == "Brady" and name == "brady")
print(name == "Brady" or name == "brady")
namelist = ["brady", "Brady"]
print("Brady" in namelist)
print("BRADY" in namelist)
print("Brady" not in namelist)
print("BRADY" not in namelist)