from easygui import *

message = "Enter level 2 code"
title = "Level 2 Code"
password = passwordbox(message, title)

if password == "Secret code":
    print("Start level 2")
else:
    print("Incorrect code")