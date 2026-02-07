from easygui import *

message = "Write case notes here: "
title = "Case notes"
notes = textbox(message, title)

if ccbox("See case notes?"):
    print(notes)
