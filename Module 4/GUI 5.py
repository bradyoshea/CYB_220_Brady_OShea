from easygui import *

question = "Enter names below: "
title = "Character naming"
fields = ["Prosecution attorney (you):", "Defense attorney (your rival):", "Judge:"]
names = multenterbox(question, title, fields)
print(names)
