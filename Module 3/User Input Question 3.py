message = "n"
while message == "n":
    num = input("Enter a number (type exit to stop): ")
    if num.isdigit():
        num = int(num)
        if num %2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    elif num == "exit":
        message = "y"
    else:
        print("Please enter a number")