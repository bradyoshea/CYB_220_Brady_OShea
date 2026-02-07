from easygui import *

message = "Select a file to open"
title = "File selection"
file = fileopenbox(message,title)
print(file)