poll = {"User1": "", "User2": "", "User3": "",}
options = ["Edubuntu", "Kubuntu", "Lubuntu", "Ubuntu Budgie", "Ubuntu Cinnamon",
           "Ubuntu Kylin", "Ubuntu MATE", "Ubuntu Studio", "Ubuntu Unity", "Xubuntu"]
for key, value in poll.items():
    valid = False
    while valid == False:
        newvalue = input(f"Hello {key}, please enter your favorite flavour of Ubuntu: ")
        if newvalue in options:
            value = newvalue
            valid = True
        else:
            valid = False
            print("Enter a valid flavour")
    print(f"{key}'s favorite flavour is {value}")

