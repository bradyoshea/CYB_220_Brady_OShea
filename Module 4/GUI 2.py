from easygui import *

if ynbox("Do you object to this testimony?"):
    print("Objection")
else:
    print("The witness may continue")