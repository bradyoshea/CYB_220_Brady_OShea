from easygui import *

message = "Does this picture match the defendants description?"
title = "Defendant Identification"
answers = ["Yes","No"]
image = "defendant_picture.png"

buttonbox(message, title, answers, image)