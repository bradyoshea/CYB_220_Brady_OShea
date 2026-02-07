from easygui import *

message = "Where would you like to save this file?"
title = "Save file"
save = filesavebox(message,title)
print(save)